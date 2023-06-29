# Q. What are examples of regular expressions?

- strings surrounded by double-quotation marks

".\*?"
- strings surrounded by \[ \]

\\\[\[^\\\[\]\*?\\\]
- variable names

\[a-zA-Z\_\]\[a-zA-Z\_0-9\]\*
- IP addresses

(\[0-9\]{1,3})\\.(\[0-9\]{1,3})\\.(\[0-9\]{1,3})\\.(\[0-9\]{1,3})
- URL

(\\S+)://(\[^:/\]+)(:(\\d+))?(/\[^#\\s\]\*)(#(\\S+))?
- lines followed by a tab

\\t.\*$
- Hiragana

\[\\x{3041}-\\x{309e}\]
- Full-width Katakana

\[\\x{309b}-\\x{309c}\\x{30a1}-\\x{30fe}\]
- Half-width Kana

\[\\x{ff61}-\\x{ff9f}\]
- CJK ideographs

\[\\x{3400}-\\x{9fff}\\x{f900}-\\x{fa2d}\]
- CJK ideograph marks

\[\\x{3000}-\\x{3037}\]
- Hangul

\[\\x{1100}-\\x{11f9}\\x{3131}-\\x{318e}\\x{ac00}-\\x{d7a3}\]
- Insert // at start of lines

Find: ^

Replace with: //
- Remove // at start of lines

Find: ^//

Replace:
- Remove trailing whitespaces

Find: \\s+?$

Replace with:
- Replace (abc) with \[abc\]

Find: \\((.\*?)\\)

Replace: \\\[\\1\\\]
- Replace <H3 ...> with <H4 ...>

Find: <H3(.\*?)>

Replace: <H4\\1>
- Replace 9/13/2003 with 2003.9.13

Find: (\[0-9\]{1,2})/(\[0-9\]{1,2})/(\[0-9\]{2,4})

Replace: \\3\\.\\1\\.\\2
- Uppercase characters from a to z

Find: \[a-z\]

Replace: \\U\\0
- Capitalize all words

Find: (\[a-zA-Z\])(\[a-zA-Z\]\*)

Replace: \\U\\1\\L\\2