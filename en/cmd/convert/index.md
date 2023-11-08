# Convert category

|     |     |
| --- | --- |
| **[Insert newline characters](../convert/insert_cr_wrap)** | Inserts newline characters at wrap points in the current selection. |
| **[Remove newline characters](../convert/delete_cr_wrap)** | Removes newline characters at wrap points in the current selection. |
| **[Split Lines](../convert/split_lines)** | Splits lines by inserting newline characters and removing trailing spaces. |
| **[Join Lines](../convert/join_lines)** | Joins lines by removing newline characters and inserting spaces at the end of each line. |
| **[Uppercase](../convert/make_upper)** | Converts the selection to all uppercase characters. |
| **[Lowercase](../convert/make_lower)** | Converts the selection to all lowercase characters. |
| **[Capitalize](../convert/capitalize)** | Capitalizes the first letter of each word in the selection. |
| **[Half-Width](../convert/zen_to_han)** | Converts full-width characters to half-width characters. |
| **[Full-Width](../convert/han_to_zen)** | Converts half-width characters to full-width characters. |
| **[Tabify](../convert/tabify)** | Converts equivalent spaces to tabs. |
| **[Untabify](../convert/untabify)** | Converts tabs to equivalent spaces. |
| **[Increase Line Indent](../convert/indent)** | Increases the line indent in the selection. |
| **[Decrease Line Indent](../convert/unindent)** | Decreases the line indent in the selection. |
| **[Comment](../convert/edit_comment)** | Comments out the selection or current line. |
| **[Uncomment](../convert/edit_uncomment)** | Removes comment marks in the selection or current line. |
| **[Remove Leading Spaces](../convert/sel_trim_left)** | Removes leading spaces, tabs, and full-width spaces in the selection. |
| **[Remove Trailing Spaces](../convert/sel_trim_right)** | Removes trailing spaces, tabs, and full-width spaces in the selection. |
| **[Remove Empty Lines](../convert/remove_empty_lines)** | Removes empty lines in the selection or the whole document. |
| **[Remove Empty Columns](../convert/remove_empty_columns)** | Removes empty columns in the CSV document. |
| **[Reconvert](../convert/reconvert)** | Reconverts the selection using an IME capable of re-conversion. |
| **[Format Document](format_document.md)** | Formats the entire document using the Language Server Protocol. |
| **[Format Selection](format_selection.md)** | Formats the selection using the Language Server Protocol. |
| **[HTML/XML Character Reference to Unicode](../convert/decode_html_char_ref)** | Decodes the selected text from HTML/XML Character Reference. |
| **[Unicode to HTML/XML Numeric Character Reference](../convert/encode_html_char_ref)** | Encodes the selected text to HTML/XML Numeric Character Reference. |
| **[Unicode to HTML Character Entity Reference](../convert/encode_html_char_entity_ref)** | Encodes the selected text to HTML Character Entity Reference. |
| **[Universal Character Names to Unicode](../convert/decode_ucn)** | Decodes the selected text from Universal Character Names. |
| **[Unicode to Universal Character Names](../convert/encode_ucn)** | Encodes the selected text to Universal Character Names. |
| **[Percent-encoding to Unicode (Current Encoding)](../convert/decode_percent)** | Decodes the selected text from the percent-encoding to Unicode using the current encoding. |
| **[Unicode to Percent-encoding (Current Encoding)](../convert/encode_percent)** | Encodes the selected text to the percent-encoding using the current encoding. |
| **[Percent-encoding to Unicode (UTF-8)](../convert/decode_percent_utf8)** | Decodes the selected text from the percent-encoding to Unicode using the UTF-8 encoding. |
| **[Unicode to Percent-encoding (UTF-8)](../convert/encode_percent_utf8)** | Encodes the selected text to the percent-encoding using the UTF-8 encoding. |
| **[Base64 to Plain Text (Current Encoding)](../convert/decode_base64)** | Decodes the selected Base64 encoded text to plain text using the current encoding. |
| **[Plain Text to Base64 (Current Encoding)](../convert/encode_base64)** | Encodes the selected plain text to the Base64 encoding using the current encoding. |
| **[Base64 to Plain Text (UTF-8)](../convert/decode_base64_utf8)** | Decodes the selected Base64 encoded text to plain text using the UTF-8 encoding. |
| **[Plain Text to Base64 (UTF-8)](../convert/encode_base64_utf8)** | Encodes the selected plain text to the Base64 encoding using the UTF-8 encoding. |
| **[Base64 to Binary File](../convert/decode_base64_binary)** | Decodes the selected Base64 encoded text to a binary file. |
| **[Binary File to Base64](../convert/encode_base64_binary)** | Encodes a binary file to the Base64 encoding. |
| **[Unicode Normalization Form C (Canonical Composition)](../convert/unicode_norm_fc)** | Apply Unicode Normalization Form C (Canonical Composition) to the selected string. |
| **[Unicode Normalization Form D (Canonical Decomposition)](../convert/unicode_norm_fd)** | Apply Unicode Normalization Form D (Canonical Decomposition) to the selected string. |
| **[Unicode Normalization Form KC (Compatibility Composition)](../convert/unicode_norm_fkc)** | Apply Unicode Normalization Form KC (Compatibility Composition) to the selected string. |
| **[Unicode Normalization Form KD (Compatibility Decomposition)](../convert/unicode_norm_fkd)** | Apply Unicode Normalization Form KD (Compatibility Decomposition) to the selected string. |

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
```