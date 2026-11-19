"""Tests for strip_unused_markup.py.

Run with: python test_strip_unused_markup.py
"""

import unittest

from strip_unused_markup import strip_in


def strip(html: bytes) -> bytes:
    stripped, _ = strip_in(html)
    return stripped


class StripUnusedMarkupTest(unittest.TestCase):
    def test_reference_classes_removed(self):
        self.assertEqual(
            strip(b'<a class="reference internal" href="#">x</a>'),
            b'<a href="#">x</a>')

    def test_unknown_tokens_kept(self):
        html = b'<a class="image-reference download" href="f.pdf">f</a>'
        self.assertEqual(strip(html), html)

    def test_toctree_level_one_removed(self):
        self.assertEqual(
            strip(b'<li class="toctree-l1"><a href="#">x</a></li>'),
            b'<li><a href="#">x</a></li>')

    def test_toctree_current_kept(self):
        html = b'<li class="toctree-l1 current"><a href="#">x</a></li>'
        self.assertEqual(strip(html), html)
        self.assertEqual(strip(b'<ul class="current">'), b'<ul class="current">')

    def test_row_classes_removed(self):
        self.assertEqual(
            strip(b'<tr class="row-odd"><th class="head"><p></p></th></tr>'),
            b'<tr><th class="head"><p></p></th></tr>')
        self.assertEqual(strip(b'<tr class="row-even"></tr>'), b'<tr></tr>')

    def test_code_classes_simplified(self):
        self.assertEqual(
            strip(b'<code class="docutils literal notranslate">x</code>'),
            b'<code class="notranslate">x</code>')

    def test_table_keeps_docutils(self):
        self.assertEqual(
            strip(b'<table class="docutils align-default">'),
            b'<table class="docutils">')

    def test_list_classes_removed(self):
        self.assertEqual(
            strip(b'<ul class="simple"><li>x</li></ul>'),
            b'<ul><li>x</li></ul>')
        self.assertEqual(
            strip(b'<ol class="arabic simple"><li>x</li></ol>'),
            b'<ol><li>x</li></ol>')

    def test_wrapper_classes_removed(self):
        for name in (b'bodywrapper', b'searchformwrapper', b'page_toc', b'compound'):
            with self.subTest(name=name):
                self.assertEqual(
                    strip(b'<div class="' + name + b'"></div>'),
                    b'<div></div>')
        self.assertEqual(
            strip(b'<div class="toctree-wrapper compound"></div>'),
            b'<div></div>')

    def test_role_spans_unwrapped(self):
        self.assertEqual(
            strip(b'<a href="#"><span class="doc std std-doc">Title</span></a>'),
            b'<a href="#">Title</a>')
        self.assertEqual(
            strip(b'<span class="std std-ref"><strong>Bold</strong></span>'),
            b'<strong>Bold</strong>')
        self.assertEqual(
            strip(b'<span class="xref myst">x</span>'),
            b'x')

    def test_pre_span_unwrapped(self):
        self.assertEqual(
            strip(b'<code class="notranslate"><span class="pre">x</span></code>'),
            b'<code class="notranslate">x</code>')

    def test_pygments_spans_kept(self):
        html = b'<pre><span class="p">(</span><span class="n">x</span></pre>'
        self.assertEqual(strip(html), html)

    def test_nested_span_not_unwrapped(self):
        html = b'<span class="doc std std-doc">a<span class="p">b</span></span>'
        self.assertEqual(strip(html), html)

    def test_empty_span_removed(self):
        self.assertEqual(
            strip(b'<pre><span></span>x</pre>'),
            b'<pre>x</pre>')

    def test_clearer_div_removed(self):
        self.assertEqual(strip(b'<div class="clearer"></div>'), b'')
        self.assertEqual(strip(b'<div class="clearer">  \n</div>'), b'')

    def test_text_outside_tags_untouched(self):
        html = b'<p>toctree-l1 class="simple" &lt;span class="pre"&gt;</p>'
        self.assertEqual(strip(html), html)

    def test_idempotent(self):
        html = (
            b'<li class="toctree-l1"><a class="reference internal" href="#">'
            b'<span class="doc std std-doc">x</span></a></li>'
            b'<div class="clearer"></div><pre><span></span>y</pre>')
        once, first = strip_in(html)
        twice, second = strip_in(once)
        self.assertEqual(twice, once)
        self.assertGreater(sum(first.values()), 0)
        self.assertEqual(sum(second.values()), 0)


if __name__ == '__main__':
    unittest.main()
