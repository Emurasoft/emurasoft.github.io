"""Tests for help_urls.py.

Run with: python test_help_urls.py
"""

import tempfile
import unittest
from pathlib import Path

from help_urls import find_problems, served_path, served_url


class ServedPathTest(unittest.TestCase):
    def test_root_index(self):
        self.assertEqual(served_path('index'), '')

    def test_section_index(self):
        self.assertEqual(served_path('cmd/index'), 'cmd/')

    def test_nested_section_index(self):
        self.assertEqual(served_path('howto/file/index'), 'howto/file/')

    def test_leaf_page(self):
        self.assertEqual(served_path('cmd/csv/align_center'),
                         'cmd/csv/align_center')

    def test_generated_page(self):
        self.assertEqual(served_path('genindex'), 'genindex')

    def test_index_in_name_is_not_an_index_page(self):
        self.assertEqual(served_path('reindex'), 'reindex')

    def test_non_ascii_docname_is_quoted(self):
        self.assertEqual(served_path('dlg/日本語'), 'dlg/%E6%97%A5%E6%9C%AC%E8%AA%9E')


class ServedUrlTest(unittest.TestCase):
    def test_root_index(self):
        self.assertEqual(served_url('https://help.emeditor.com/en/index.html'),
                         'https://help.emeditor.com/en/')

    def test_section_index(self):
        self.assertEqual(served_url('https://help.emeditor.com/en/cmd/index.html'),
                         'https://help.emeditor.com/en/cmd/')

    def test_generated_page(self):
        self.assertEqual(served_url('https://help.emeditor.com/en/genindex.html'),
                         'https://help.emeditor.com/en/genindex')

    def test_leaf_page(self):
        self.assertEqual(
            served_url('https://help.emeditor.com/en/cmd/csv/align_center.html'),
            'https://help.emeditor.com/en/cmd/csv/align_center')

    def test_url_without_html_unchanged(self):
        url = 'https://help.emeditor.com/en/cmd/'
        self.assertEqual(served_url(url), url)

    def test_relative_url(self):
        self.assertEqual(served_url('csv/align_center.html'), 'csv/align_center')


class FindProblemsTest(unittest.TestCase):
    def setUp(self):
        self._directory = tempfile.TemporaryDirectory()
        self.directory = Path(self._directory.name)
        self.addCleanup(self._directory.cleanup)

    def write(self, name: str, content: str) -> None:
        path = self.directory / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def test_internal_html_links_are_problems(self):
        self.write('served.html', '<a href="cmd/">cmd</a>')
        self.write('page.html', '<a href="cmd.html">cmd</a>')
        self.write('search.html',
                   '<form action="search.html"></form>')
        self.write('external.html', '<a href="https://example.com/x.html">x</a>')

        problems = find_problems(self.directory)

        self.assertEqual(sorted(value for _, value in problems),
                         ['cmd.html', 'search.html'])

    def test_absolute_site_links_are_problems(self):
        self.write('page.html',
                   '<a href="https://help.emeditor.com/en/cmd/index.html">x</a>')
        self.assertEqual(len(find_problems(self.directory)), 1)

    def test_clean_tree_has_no_problems(self):
        self.write('page.html', '<a href="cmd/">cmd</a><a href="#top">top</a>')
        self.write('sitemap.xml', '<loc>https://help.emeditor.com/en/cmd/</loc>')
        self.assertEqual(find_problems(self.directory), [])

    def test_sitemap_with_html_entries_is_a_problem(self):
        self.write('sitemap.xml', '<loc>https://help.emeditor.com/en/cmd/index.html</loc>')
        problems = find_problems(self.directory)
        self.assertEqual(len(problems), 1)
        self.assertEqual(problems[0][0].name, 'sitemap.xml')


if __name__ == '__main__':
    unittest.main()
