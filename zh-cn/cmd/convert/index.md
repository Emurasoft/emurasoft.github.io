# 转换类别

|     |     |
| --- | --- |
| **[插入换行符](../edit/insert_cr_wrap)** | 在当前选定区域的换行点插入换行符。 |
| **[移除换行符](../edit/delete_cr_wrap)** | 在当前选定区域的换行点移除换行符。 |
| **[分割行](../edit/split_lines)** | 通过插入换行符和移除行尾空格来分割行。 |
| **[连接行](../edit/join_lines)** | 通过移除换行符和在行尾插入空格来连接行。 |
| **[大写](../edit/make_upper)** | 把选定文本全部转换为大写字符。 |
| **[小写](../edit/make_lower)** | 把选定文本全部转换为小写字符。 |
| **[首字母大写](../edit/capitalize)** | 让选区中每一个单词的首字母大写。 |
| **[半角](../edit/zen_to_han)** | 转换全角字符为半角字符。 |
| **[全角](../edit/han_to_zen)** | 转换半角字符为全角字符。 |
| **[制表位化](../edit/tabify)** | 将空格转换为制表符（tab）。 |
| **[非制表位化](../edit/untabify)** | 将制表符（tab）转换为空格。 |
| **[增加行缩进](../edit/indent)** | 增加选定区域的行缩进。 |
| **[减少行缩进](../edit/unindent)** | 减少选定区域的行缩进。 |
| **[注释](../edit/edit_comment)** | 注释选定区域或当前行。 |
| **[取消注释](../edit/edit_uncomment)** | 取消选定区域或当前行的注释标记。 |
| **[删除前导空格](../edit/sel_trim_left)** | 删除选区内前导的空格，tab，以及全角空格。 |
| **[删除尾随空格](../edit/sel_trim_right)** | 删除选区内尾随的空格，tab，以及全角空格。 |
| **[删除空行](../edit/remove_empty_lines)** | 删除选区内或整个文档中的空行。 |
| **[删除空列](../edit/remove_empty_columns)** | 删除 CSV 文档中的空列。 |
| **[重新转换](../edit/reconvert)** | 使用可以进行重新转换的输入法重新转换选定区域。 |
| **[格式化文档](format_document.md)** | Formats the entire document using the Language Server Protocol. |
| **[格式化选区](format_selection.md)** | Formats the selection using the Language Server Protocol. |
| **[将 HTML/XML 字符引用转换为 Unicode](../edit/decode_html_char_ref)** | 解码选中的 HTML/XML 字符引用文本。 |
| **[将 Unicode 转换为 HTML/XML 数字字符引用](../edit/encode_html_char_ref)** | 把选中的文本编码为 HTML/XML 数字字符引用。 |
| **[将 Unicode 转换为 HTML 字符实体引用](../edit/encode_html_char_entity_ref)** | 把选中的文本编码为 HTML/XML 数字字符引用。 |
| **[将通用字符名称转换为 Unicode](../edit/decode_ucn)** | 解码选中的选中的通用字符名称文本。 |
| **[将 Unicode 转换为通用字符名称](../edit/encode_ucn)** | 将选中的文本用通用字符名称编码。 |
| **[将百分比编码字符转换为 Unicode (当前编码)](../edit/decode_percent)** | 用当前编码把选中的百分比编码文本解码为 Unicode。 |
| **[将 Unicode 转换为百分比编码 (当前编码)](../edit/encode_percent)** | 用当前编码对选中的文本进行百分比编码。 |
| **[将百分比编码字符转换为 Unicode (UTF-8)](../edit/decode_percent_utf8)** | 用UTF-8编码把选中的百分比编码文本解码为 Unicode。 |
| **[将 Unicode 转换为百分比编码 (UTF-8)](../edit/encode_percent_utf8)** | 用 UTF-8 编码对选中的文本进行百分比编码。 |
| **[将 Base64 转换为纯文本 (当前编码)](../edit/decode_base64)** | 用当前编码把选取的 Base64 编码文本解码为纯文本。 |
| **[将纯文本转换为 Base64 (当前编码)](../edit/encode_base64)** | 用当前编码将选取的纯文本编码为 Base64 编码。 |
| **[将 Base64 转换为纯文本 (UTF-8)](../edit/decode_base64_utf8)** | 用 UTF-8 编码把选取的 Base64 编码文本解码为纯文本。 |
| **[将纯文本转换为 Base64 (UTF-8)](../edit/encode_base64_utf8)** | 用 UTF-8 编码将选取的纯文本编码为 Base64 编码。 |
| **[Base64 转换为二进制文件](../edit/decode_base64_binary)** | 把选取的 Base64 编码文本解码为一个二进制文件。 |
| **[二进制文件转换为 Base64](../edit/encode_base64_binary)** | 对一个二进制文件进行 Base64 编码。 |
| **[Unicode 标准化表单 C（规范组成）](../edit/unicode_norm_fc)** | 将 Unicode 标准化表单 C（规范组成）应用于所选字符串。 |
| **[Unicode 标准化表单 D（规范分解）](../edit/unicode_norm_fd)** | 将 Unicode 标准化表单 D（规范分解）应用于所选字符串。 |
| **[Unicode 标准化表单 KC（兼容性组成）](../edit/unicode_norm_fkc)** | 将 Unicode 标准化表单 KC（兼容性组成）应用于所选字符串。 |
| **[Unicode 标准化表单 KD（兼容性分解）](../edit/unicode_norm_fkd)** | 将 Unicode 标准化表单 KD（兼容性分解）应用于所选字符串。 |

```{toctree}
:maxdepth: 1
:hidden:
format_document
format_selection
```