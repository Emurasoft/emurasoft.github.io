"""Tests for help_urls.py.

Run with: python test_help_urls.py
"""

import unittest

from help_urls import served_path, served_url


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


if __name__ == '__main__':
    unittest.main()
