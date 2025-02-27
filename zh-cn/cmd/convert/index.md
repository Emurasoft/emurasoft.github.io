# 转换类别

|     |     |
| --- | --- |
| **[插入换行符](../convert/insert_cr_wrap)** | 在当前选定区域的换行点插入换行符。 |
| **[移除换行符](../convert/delete_cr_wrap)** | 在当前选定区域的换行点移除换行符。 |
| **[分割行](../convert/split_lines)** | 通过插入换行符和移除行尾空格来分割行。 |
| **[连接行](../convert/join_lines)** | 通过移除换行符和在行尾插入空格来连接行。 |
| **[大写](../convert/make_upper)** | 把选定文本全部转换为大写字符。 |
| **[小写](../convert/make_lower)** | 把选定文本全部转换为小写字符。 |
| **[首字母大写](../convert/capitalize)** | 让选区中每一个单词的首字母大写。 |
| **[半角](../convert/zen_to_han)** | 转换全角字符为半角字符。 |
| **[全角](../convert/han_to_zen)** | 转换半角字符为全角字符。 |
| **[制表位化](../convert/tabify)** | 将空格转换为制表符（tab）。 |
| **[非制表位化](../convert/untabify)** | 将制表符（tab）转换为空格。 |
| **[增加行缩进](../convert/indent)** | 增加选定区域的行缩进。 |
| **[减少行缩进](../convert/unindent)** | 减少选定区域的行缩进。 |
| **[注释](../convert/edit_comment)** | 注释选定区域或当前行。 |
| **[取消注释](../convert/edit_uncomment)** | 取消选定区域或当前行的注释标记。 |
| **[删除前导空格](../convert/sel_trim_left)** | 删除选区内前导的空格，tab，以及全角空格。 |
| **[删除尾随空格](../convert/sel_trim_right)** | 删除选区内尾随的空格，tab，以及全角空格。 |
| **[删除空行](../convert/remove_empty_lines)** | 删除选区内或整个文档中的空行。 |
| **[删除空列](../convert/remove_empty_columns)** | 删除 CSV 文档中的空列。 |
| **[重新转换](../convert/reconvert)** | 使用可以进行重新转换的输入法重新转换选定区域。 |
| **[格式化文档](format_document.md)** | 用语言服务器协议格式化整个文档。 |
| **[格式化选区](format_selection.md)** | 用语言服务器协议格式化选取区域。 |
| **[将 HTML/XML 字符引用转换为 Unicode](../convert/decode_html_char_ref)** | 解码选中的 HTML/XML 字符引用文本。 |
| **[将 Unicode 转换为 HTML/XML 数字字符引用](../convert/encode_html_char_ref)** | 把选中的文本编码为 HTML/XML 数字字符引用。 |
| **[将 Unicode 转换为 HTML 字符实体引用](../convert/encode_html_char_entity_ref)** | 把选中的文本编码为 HTML/XML 数字字符引用。 |
| **[将通用字符名称转换为 Unicode](../convert/decode_ucn)** | 解码选中的选中的通用字符名称文本。 |
| **[将 Unicode 转换为通用字符名称](../convert/encode_ucn)** | 将选中的文本用通用字符名称编码。 |
| **[将百分比编码字符转换为 Unicode (当前编码)](../convert/decode_percent)** | 用当前编码把选中的百分比编码文本解码为 Unicode。 |
| **[将 Unicode 转换为百分比编码 (当前编码)](../convert/encode_percent)** | 用当前编码对选中的文本进行百分比编码。 |
| **[将百分比编码字符转换为 Unicode (UTF-8)](../convert/decode_percent_utf8)** | 用UTF-8编码把选中的百分比编码文本解码为 Unicode。 |
| **[将 Unicode 转换为百分比编码 (UTF-8)](../convert/encode_percent_utf8)** | 用 UTF-8 编码对选中的文本进行百分比编码。 |
| **[将 Base64 转换为纯文本 (当前编码)](../convert/decode_base64)** | 用当前编码把选取的 Base64 编码文本解码为纯文本。 |
| **[将纯文本转换为 Base64 (当前编码)](../convert/encode_base64)** | 用当前编码将选取的纯文本编码为 Base64 编码。 |
| **[将 Base64 转换为纯文本 (UTF-8)](../convert/decode_base64_utf8)** | 用 UTF-8 编码把选取的 Base64 编码文本解码为纯文本。 |
| **[将纯文本转换为 Base64 (UTF-8)](../convert/encode_base64_utf8)** | 用 UTF-8 编码将选取的纯文本编码为 Base64 编码。 |
| **[Base64 转换为二进制文件](../convert/decode_base64_binary)** | 把选取的 Base64 编码文本解码为一个二进制文件。 |
| **[二进制文件转换为 Base64](../convert/encode_base64_binary)** | 对一个二进制文件进行 Base64 编码。 |
| **[Unicode 标准化表单 C（规范组成）](../convert/unicode_norm_fc)** | 将 Unicode 标准化表单 C（规范组成）应用于所选字符串。 |
| **[Unicode 标准化表单 D（规范分解）](../convert/unicode_norm_fd)** | 将 Unicode 标准化表单 D（规范分解）应用于所选字符串。 |
| **[Unicode 标准化表单 KC（兼容性组成）](../convert/unicode_norm_fkc)** | 将 Unicode 标准化表单 KC（兼容性组成）应用于所选字符串。 |
| **[Unicode 标准化表单 KD（兼容性分解）](../convert/unicode_norm_fkd)** | 将 Unicode 标准化表单 KD（兼容性分解）应用于所选字符串。 |
| **[Markdown 转 HTML](../convert/markdown_to_html)** | 将选取的文本从 Markdown 转换为 HTML。 |
| **[HTML 转 Markdown](../convert/html_to_markdown)** | 将选取的文本从 HTML 转换为 Markdown。 |
| **[Markdown 转纯文本](../convert/markdown_to_text)** | 将选取的文本从 Markdown 转换为纯文本。 |
| **[HTML 转纯文本](../convert/html_to_text)** | 将选取的文本从 HTML 转换为纯文本。 |

```{toctree}
:maxdepth: 1
:hidden:
insert_cr_wrap
delete_cr_wrap
split_lines
join_lines
make_upper
make_lower
capitalize
zen_to_han
han_to_zen
tabify
untabify
indent
unindent
edit_comment
edit_uncomment
sel_trim_left
sel_trim_right
remove_empty_lines
remove_empty_columns
reconvert
format_document
format_selection
decode_html_char_ref
encode_html_char_ref
encode_html_char_entity_ref
decode_ucn
encode_ucn
decode_percent
encode_percent
decode_percent_utf8
encode_percent_utf8
decode_base64
encode_base64
decode_base64_utf8
encode_base64_utf8
decode_base64_binary
encode_base64_binary
unicode_norm_fc
unicode_norm_fd
unicode_norm_fkc
unicode_norm_fkd
markdown_to_html
html_to_markdown
markdown_to_text
html_to_text
```