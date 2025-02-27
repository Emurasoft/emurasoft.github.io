# 轉換類別

|     |     |
| --- | --- |
| **[插入換行字元](../convert/insert_cr_wrap)** | 在目前的選取範圍內的文字區端點處插入換行字元。 |
| **[移除換行字元](../convert/delete_cr_wrap)** | 在目前的選取範圍內移除文字區端點處的換行字元。 |
| **[分割行](../convert/split_lines)** | 通過插入換行符號和移除行尾空格來分割行。 |
| **[連接行](../convert/join_lines)** | 通過移除換行符號和在行尾插入空格鍵來連接行。 |
| **[大寫](../convert/make_upper)** | 把選定文字全部轉換為大寫字元。 |
| **[小寫](../convert/make_lower)** | 把選定文字全部轉換為小寫字元。 |
| **[首字母大寫](../convert/capitalize)** | 讓選區中每一個單字的首字母大寫。 |
| **[半形](../convert/zen_to_han)** | 轉換全形字元為半形字元。 |
| **[全形](../convert/han_to_zen)** | 轉換半形字元為全形字元。 |
| **[定位點化](../convert/tabify)** | 將空白字元轉換為 Tab 字元。 |
| **[非定位點化](../convert/untabify)** | 將 Tab 字元轉換為空白字元。 |
| **[增加行縮排](../convert/indent)** | 增加選定區域的行縮排。 |
| **[減少行縮排](../convert/unindent)** | 減少選定區域的行縮排。 |
| **[註解](../convert/edit_comment)** | 註解選定區域或目前的行。 |
| **[取消註解](../convert/edit_uncomment)** | 取消選定區域或目前的行的註解標記。 |
| **[刪除開頭空格](../convert/sel_trim_left)** | 刪除選區內開頭的空格，tab，以及全形空格。 |
| **[刪除尾端空格](../convert/sel_trim_right)** | 刪除選區內尾端的空格，tab，以及全形空格。 |
| **[刪除空行](../convert/remove_empty_lines)** | 刪除選區內的空行。 |
| **[刪除空欄](../convert/remove_empty_columns)** | 刪除 CSV 文檔中的空欄。 |
| **[重新轉換](../convert/reconvert)** | 使用可以進行重新轉換的輸入法重新轉換選定區域。 |
| **[格式化文檔](format_document.md)** | 用語言伺服器協議格式化整個文檔。 |
| **[格式化選區](format_selection.md)** | 用語言伺服器協議格式化選取區域。 |
| **[將 HTML/XML 字元參照轉換為 Unicode](../convert/decode_html_char_ref)** | 解碼選中的 HTML/XML 字元參照文字。 |
| **[將 Unicode 轉換為 HTML/XML 字元值參照](../convert/encode_html_char_ref)** | 將已選中的文字編碼為 HTML/XML 字元值參照的格式。 |
| **[將 Unicode 轉換為 HTML 字元實體參照](../convert/encode_html_char_entity_ref)** | 把選取的文字編碼為 HTML 字元實體參照。 |
| **[通用字元名稱轉換為 Unicode](../convert/decode_ucn)** | 解碼選中的選中的通用字元名稱文字。 |
| **[將 Unicode 轉換為通用字元名稱](../convert/encode_ucn)** | 將選中的文字用通用字元名稱編碼。 |
| **[將百分號編碼轉換為 Unicode (目前的編碼)](../convert/decode_percent)** | 用目前的編碼把選中的百分號編碼文字解碼為 Unicode。 |
| **[將 Unicode 轉換為百分號編碼 (目前的編碼)](../convert/encode_percent)** | 用當前編碼對選中的文字進行百分號編碼。 |
| **[將百分號編碼轉換為 Unicode (UTF-8)](../convert/decode_percent_utf8)** | 用UTF-8編碼把選中的百分比編碼文字解碼為 Unicode。 |
| **[將 Unicode 轉換為百分號編碼 (UTF-8)](../convert/encode_percent_utf8)** | 用 UTF-8 編碼對選中的文字進行百分號編碼。 |
| **[將 Base64 轉換為純文字 (目前的編碼)](../convert/decode_base64)** | 用目前的編碼把選取的 Base64 編碼文字解碼為純文字。 |
| **[將純文字轉換為 Base64 (目前的編碼)](../convert/encode_base64)** | 用目前的編碼將選取的純文字編碼為 Base64 編碼。 |
| **[將 Base64 轉換為純文字 (UTF-8)](../convert/decode_base64_utf8)** | 用 UTF-8 編碼把選取的 Base64 編碼文字解碼為純文字。 |
| **[將純文字轉換為 Base64 (UTF-8)](../convert/encode_base64_utf8)** | 用 UTF-8 編碼將選取的純文字編碼為 Base64 編碼。 |
| **[Base64 轉換為二進位檔案](../convert/decode_base64_binary)** | 把選取的 Base64 編碼文字解碼為一個二進位檔案。 |
| **[二進位檔案轉換為 Base64](../convert/encode_base64_binary)** | 對一個二進位檔案進行 Base64 編碼。 |
| **[Unicode 正規化表單 C (標準組合)](../convert/unicode_norm_fc)** | 將 Unicode 正規化表單 C (標準組合) 應用於所選字串。 |
| **[Unicode 正規化表單 D (標準分解)](../convert/unicode_norm_fd)** | 將 Unicode 正規化表單 D (標準分解) 應用於所選字串。 |
| **[Unicode 正規化表單 KC (相容性組合)](../convert/unicode_norm_fkc)** | 將 Unicode 正規化表單 KC (相容性組合) 應用於所選字串。 |
| **[Unicode 正規化表單 KD (相容性分解)](../convert/unicode_norm_fkd)** | 將 Unicode 正規化表單 KD (相容性分解) 應用於所選字串。 |
| **[Markdown 轉 HTML](../convert/markdown_to_html)** | 將選取的文字從 Markdown 轉換為 HTML。 |
| **[HTML 轉 Markdown](../convert/html_to_markdown)** | 將選取的文字從 HTML 轉換為 Markdown。 |
| **[Markdown 轉純文字](../convert/markdown_to_text)** | 將選取的文字從 Markdown 轉換為純文字。 |
| **[HTML 轉純文字](../convert/html_to_text)** | 將選取的文字從 HTML 轉換為純文字。 |

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
