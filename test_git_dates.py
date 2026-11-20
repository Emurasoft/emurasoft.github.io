"""Tests for git_dates.py.

Run with: python test_git_dates.py
"""

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from git_dates import REPO_ROOT, _unresolved_paths, doc_dates, repo_relative


class DocDatesTest(unittest.TestCase):
    def test_source_date(self):
        values = doc_dates({'page': ['en/page.md']},
                           {'en/page.md': (b'100', False)})
        self.assertEqual(values, {'page': (b'100', False)})

    def test_newest_dependency_date(self):
        values = doc_dates(
            {'page': ['en/page.md', 'en/included.md']},
            {'en/page.md': (b'100', False), 'en/included.md': (b'200', False)})
        self.assertEqual(values['page'], (b'200', False))

    def test_missing_date_is_ignored(self):
        values = doc_dates(
            {'page': ['en/page.md', 'en/included.md']},
            {'en/page.md': None, 'en/included.md': (b'200', False)})
        self.assertEqual(values['page'], (b'200', False))

    def test_untracked_document(self):
        values = doc_dates({'page': ['en/page.md']}, {'en/page.md': None})
        self.assertEqual(values['page'], (None, False))

    def test_too_shallow_drops_the_date(self):
        values = doc_dates(
            {'page': ['en/page.md', 'en/included.md']},
            {'en/page.md': (b'100', False),
             'en/included.md': (b'200', True)})
        self.assertEqual(values['page'], (None, True))

    def test_too_shallow_ignored_when_it_is_not_the_newest(self):
        values = doc_dates(
            {'page': ['en/page.md', 'en/included.md']},
            {'en/page.md': (b'200', False),
             'en/included.md': (b'100', True)})
        self.assertEqual(values['page'], (b'200', False))

    def test_document_with_no_paths(self):
        self.assertEqual(doc_dates({'page': []}, {}), {'page': (None, False)})


class RepoRelativeTest(unittest.TestCase):
    def setUp(self):
        self._directory = tempfile.TemporaryDirectory()
        self.root = Path(self._directory.name).resolve()
        self.addCleanup(self._directory.cleanup)

    def test_path_inside(self):
        self.assertEqual(
            repo_relative(self.root / 'a' / '..' / 'a' / 'x.md', self.root),
            'a/x.md')

    def test_path_outside(self):
        self.assertIsNone(
            repo_relative(self.root.parent / 'elsewhere' / 'x.md', self.root))

    def test_sibling_with_common_prefix(self):
        self.assertIsNone(repo_relative(self.root / '..' / 'other' / 'x.md',
                                        self.root))


class FakeEnv:
    def __init__(self, docs, dependencies=None):
        self.srcdir = REPO_ROOT / 'en'
        self.found_docs = set(docs)
        self.dependencies = dependencies or {}
        self.git_last_updated = {docname: None for docname in docs}

    def doc2path(self, docname, base=True):
        path = Path(docname + '.md')
        if base:
            return self.srcdir / path
        return path


class UnresolvedPathsTest(unittest.TestCase):
    def setUp(self):
        config = SimpleNamespace(git_exclude_patterns=['excluded/**'],
                                 git_exclude_commits=[])
        self.app = SimpleNamespace(config=config)

    def test_source_and_dependencies(self):
        env = FakeEnv(['index'], {'index': [
            'glossary/index.md', 'excluded/dep.md', 'missing.md']})
        self.assertEqual(_unresolved_paths(self.app, env),
                         {'index': ['en/index.md', 'en/glossary/index.md']})

    def test_excluded_document_is_skipped(self):
        env = FakeEnv(['index', 'excluded/page'])
        self.assertEqual(_unresolved_paths(self.app, env),
                         {'index': ['en/index.md']})

    def test_resolved_document_is_skipped(self):
        env = FakeEnv(['index'])
        env.git_last_updated['index'] = (b'100', True)
        self.assertEqual(_unresolved_paths(self.app, env), {})


if __name__ == '__main__':
    unittest.main()
