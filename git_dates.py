"""Fill in Git timestamps for every page with one log call per build.

sphinx-sitemap loads sphinx_last_updated_by_git when sitemap_show_lastmod is
true. Both the "Last updated" footer and the sitemap <lastmod> read the dates
that extension stores in env.git_last_updated. It asks Git for one source
directory at a time, which costs hundreds of subprocesses per build because
the sources are spread over hundreds of directories. One repository-wide
`git log` answers the same question, so this extension fills in the dates
first and leaves the per-directory lookup nothing to do.

git_dates is registered before sphinx_sitemap in conf.py, and its handler runs
first because of its 400 priority (the upstream handler uses 500). If the bulk
lookup fails for any reason, the handler leaves the dates alone and the
per-directory lookup runs as before.
"""

import subprocess
from pathlib import Path

# The Sphinx imports live inside the functions that need them so this module
# and its pure helpers can be imported by the tests without Sphinx installed.

REPO_ROOT = Path(__file__).resolve().parent

TRACKED_FILES = ['git', 'ls-tree', '-r', '--name-only', '-z', 'HEAD']

# The flags match the "git log" that sphinx_last_updated_by_git runs, so its
# parse_log can read this output. Without a pathspec the whole history is
# streamed once, and parse_log stops as soon as every file has a date.
LOG = [
    'git', 'log', '--pretty=format:%n%at%x00%H%x00%P',
    '--author-date-order', '--name-only', '--no-show-signature',
    '-z', '-m', '--', '.',
]


def doc_dates(paths, dates):
    """Return env.git_last_updated values for the docs in paths.

    paths maps a docname to its source and dependency paths, relative to the
    repository root. dates maps each path to the (timestamp, too_shallow)
    pair parse_log found, or to None when the path is not in the log.
    """
    values = {}
    for docname, files in paths.items():
        found = [dates[path] for path in files if dates.get(path) is not None]
        if not found:
            values[docname] = (None, False)
            continue
        timestamp, too_shallow = max(found)
        if too_shallow:
            # The newest date was cut off by a shallow clone, so the real
            # last update of the page is unknown.
            timestamp = None
        values[docname] = (timestamp, too_shallow)
    return values


def repo_relative(path, root=REPO_ROOT):
    """Return path relative to the repository root, or None if outside it."""
    try:
        return Path(path).resolve().relative_to(root).as_posix()
    except ValueError:
        return None


def _tracked_files():
    output = subprocess.check_output(
        TRACKED_FILES, cwd=REPO_ROOT, stderr=subprocess.PIPE)
    return {name for name in output.decode('utf-8').split('\0') if name}


def _file_dates(paths, exclude_commits):
    from sphinx_last_updated_by_git import parse_log

    tracked = _tracked_files()
    requested = {path for files in paths.values() for path in files} & tracked
    dates = dict.fromkeys(requested)
    if not dates:
        return dates
    with subprocess.Popen(
            LOG, cwd=REPO_ROOT, stdout=subprocess.PIPE) as process:
        try:
            parse_log(process.stdout, requested, REPO_ROOT, exclude_commits,
                      dates)
        finally:
            # parse_log stops reading once every file has a date.
            process.terminate()
    return dates


def _unresolved_paths(app, env):
    from sphinx.util.matching import Matcher

    excluded = Matcher(app.config.git_exclude_patterns)
    paths = {}
    for docname in env.found_docs:
        if env.git_last_updated.get(docname) is not None:
            continue
        if excluded(env.doc2path(docname, False)):
            continue
        files = []
        source = repo_relative(env.doc2path(docname))
        if source is not None:
            files.append(source)
        for dependency in env.dependencies.get(docname, ()):
            if excluded(dependency):
                continue
            # Dependencies are relative to the source directory and may
            # contain "..".
            depfile = Path(env.srcdir, dependency)
            if not depfile.exists():
                continue
            path = repo_relative(depfile)
            if path is not None:
                files.append(path)
        paths[docname] = files
    return paths


def _env_updated(app, env):
    from sphinx.util import logging

    if not getattr(app.config, 'sitemap_show_lastmod', False):
        return
    if not hasattr(env, 'git_last_updated'):
        return
    paths = _unresolved_paths(app, env)
    if not paths:
        return
    exclude_commits = {
        commit.encode('utf-8') for commit in app.config.git_exclude_commits}
    try:
        dates = _file_dates(paths, exclude_commits)
    except (OSError, ValueError, subprocess.SubprocessError,
            AssertionError) as error:
        # Leave the dates unset so sphinx_last_updated_by_git falls back to
        # its own per-directory lookup. Info level keeps -W from failing the
        # build over the optimization.
        logging.getLogger(__name__).info(
            'Bulk Git timestamp lookup failed: %s', error,
            type='git', subtype='bulk_error')
        return
    logger = logging.getLogger(__name__)
    for docname, (timestamp, too_shallow) in doc_dates(paths, dates).items():
        if too_shallow:
            logger.warning('Git clone too shallow', location=docname,
                           type='git', subtype='too_shallow')
        # A tuple, even (None, False), stops the upstream handler from looking
        # the doc up again.
        show_sourcelink = timestamp is not None or too_shallow
        env.git_last_updated[docname] = (timestamp, show_sourcelink)


def setup(app):
    # The default priority is 500; this handler has to run before it.
    app.connect('env-updated', _env_updated, priority=400)
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
