# Regular Expression Syntax

EmEditor regular expression
syntax is based on Perl regular expression syntax.

## Literals

All characters are literals except: ".", "\*", "?", "+", "(", ")", "{", "}",
"\[", "\]", "^", "$", "\|", and "\\". These characters are literals when preceded by a
"\\". A literal is a character that matches itself. For example, searching for
"\\?" will match every "?" in the document, or searching for "Hello" will match
every "Hello" in the document.

## Metacharacters

The following tables contain the complete list of metacharacters
(non-literals) and their behavior in the context of regular expressions.

|     |     |
| --- | --- |
| \ | Marks the next character as a special character, a literal, or a back reference. For example, 'n' matches the character "n". '\\n' matches a newline character. The sequence '\\\\' matches "\\" and "\\(" matches "(". |
| ^ | Matches the position at the beginning of the input string. For example, "^e" matches any "e" that begins a string. |
| $ | Matches the position at the end of the input string. For example, "e$" matches any "e" that ends a string. |
| \* | Matches the preceding character or sub-expression zero or more times. For example, zo\* matches "z" and "zoo". \* is equivalent to {0,}. |
| + | Matches the preceding character or sub-expression one or more times. For example, 'zo+' matches "zo" and "zoo" , but not "z". + is equivalent to {1,}. |
| ? | Matches the preceding character or sub-expression zero or one time. For example, "do(es)?" matches the "do" in  "do"or "does".? is equivalent to {0,1} |
| {n} | n is a nonnegative integer. Matches exactly n times. For example, 'o{2}' does not match the "o" in "Bob" but matches the two o's in "food". |
| {n,} | n is a nonnegative integer. Matches at least n times. For example, 'o{2,}' does not match "o" in "Bob" and matches all the o's in "foooood". "o{1,}" is equivalent to 'o+'. 'o{0,}' is equivalent to 'o\*'. |
| {n,m} | m and n are nonnegative integers, where n <= m. Matches at least n and at most m times. For example, "o{1,3}" matches the first three o's in "fooooood". 'o{0,1}' is equivalent to 'o?'. Note that you cannot put a space between the comma and the numbers. |
| ? | When this character immediately follows any of the other quantifiers (\*, +, ?, {n}, {n,}, {n,m}), the matching pattern is non-greedy. A non-greedy pattern matches as little of the searched string as possible, whereas the default greedy pattern matches as much of the searched string as possible. For example, in the string "oooo", 'o+?' matches a single "o", while 'o+' matches all 'o's. |
| . | Matches any single character. For example, ".e" will match text where any character precedes an "e", like "he", "we", or "me". In EmEditor Professional, it matches a newline character within the range specified in the **Additional Lines to Search for Regular Expressions** text box if the<br> **Regular Expression "." Can Match Newline Characters** check box is checked. |
| (pattern) | Parentheses serve two purposes: to group a pattern into a sub-expression and to capture what generated the match. For example the expression "(ab)\*" would match all of the string "ababab". Each sub-expression match is captured as a back reference (see below) numbered from left to right. To match parentheses characters ( ), use '\\(' or '\\)'. |
| (?<name>pattern) | Captures the string matched by "pattern" into the group "name". |
| \\1 - \\9 | Indicates a back reference - a back reference is a reference to a previous sub-expression that has already been matched. The reference is to what the sub-expression matched, not to the expression itself. A back reference consists of the escape character "\\" followed by a digit "1" to "9", "\\1" refers to the first sub-expression, "\\2" to the second etc. For example, "(a)\\1" would capture "a" as the first back reference and match any text "aa". Back references can also be used when using the **Replace** feature under the **Search** menu. Use regular expressions to locate a text pattern, and the matching text can be replaced by a specified back reference. For example, "(h)(e)" will find "he", and putting "\\1" in the **Replace With** box will replace "he" with "h" whereas "\\2\\1" will replace "he" with "eh". |
| \\k<name> | Indicates a named back reference. A named back reference is a reference to a previous named capturing group using this form: (?<name>expression). If "name" is a number, it indicates a numbered back reference, equivalent to \\1, \\2, \\3, ... |
| (?:pattern) | A subexpression that matches pattern but does not capture the match, that is, it is a non-capturing match that is not stored for possible later use with back references. This is useful for combining parts of a pattern with the "or" character (\|). For example, 'industr(?:y\|ies) is a more economical expression than 'industry\|industries'. |
| (?=pattern) | A subexpression that performs a positive lookahead search, which matches the string at any point where a string matching pattern begins. For example, "x(?=abc)" matches an "x"only if it is followed by the expression "abc". This is a non-capturing match, that is, the match is not captured for possible later use with back references. pattern cannot contain a newline character. |
| (?!pattern) | A subexpression that performs a negative lookahead search, which matches the search string at any point where a string not matching pattern begins. For example, "x(?!abc)" matches an "x" only if it is not followed by the expression "abc". This is a non-capturing match, that is, the match is not captured for possible later use with back references. pattern cannot contain a newline character. |
| (?<=pattern) | A subexpression that performs a positive lookbehind search, which matches the search string at any point where a string matching pattern ends. For example, "(?<=abc)x" matches an "x" only if it is preceded by the expression "abc". This is a non-capturing match, that is, the match is not captured for possible later use with back references. pattern cannot contain a newline character. pattern must be of fixed length. |
| (?<!pattern) | A subexpression that performs a negative lookbehind search, which matches the search string at any point where a string not matching pattern ends. For example, "(?<!abc)x" matches an "x" only if it is not preceded by the expression "abc". This is a non-capturing match, that is, the match is not captured for possible later use with back references. pattern cannot contain a newline character. pattern must be of fixed length. |
| x\|y | Matches either x or y. For example, 'z\|food' matches "z" or "food". '(z\|f)ood' matches "zood" or "food". |
| \[xyz\] | A character set. Matches any one of the enclosed characters. For example, '\[abc\]' matches the 'a' in "plain". |
| \[^xyz\] | A negative character set. Matches any character not enclosed. For example, '\[^abc\]' matches the 'p' in "plain". |
| \[a-z\] | A range of characters. Matches any character in the specified range. For example, '\[a-z\]' matches any lowercase alphabetic character in the range 'a' through 'z'. |
| \[^a-z\] | A negative range characters. Matches any character not in the specified range. For example, '\[^a-z\]' matches any character not in the range 'a' through 'z'. |

## Character Classes

The following character classes are used within a character set such as "\[:classname:\]".
For instance, "\[\[:space:\]\]"
is the set of all whitespace characters.

|     |     |
| --- | --- |
| alnum | Any linguistic character and number: alphabetical, syllabary, or ideographic. |
| alpha | Any linguistic character: alphabetical, syllabary, or ideographic. |
| blank | Any blank character, either a space or a tab. |
| cntrl | Any control character. |
| digit | Any digit 0-9. |
| graph | Any graphical character. |
| lower | Any lowercase character a-z, and other lowercase character. |
| print | Any printable character. |
| punct | Any punctuation character. |
| space | Any whitespace character. |
| upper | Any uppercase character A-Z, and other uppercase character. |
| xdigit | Any hexadecimal digit character, 0-9, a-f and A-F. |
| word | Any word character - all alphanumeric characters plus the underscore. |
| unicode | Any character whose code is greater than 255. (Regex.Boost only) |

## Character Properties

Syntax:

\\p{property-name}

\\P{property-name}  (negative)

\\p{^property-name}  (negative)  (Onigmo only)

The following property names can be used. For instance, "\\p{alnum}" is any alphanumeric character, and "\\P{alnum}" is its negative form.

|     |     |
| --- | --- |
| alnum | Any linguistic character and number: alphabetical, syllabary, or ideographic. |
| alpha | Any linguistic character: alphabetical, syllabary, or ideographic. |
| blank | Any blank character, either a space or a tab. |
| cntrl | Any control character. |
| digit | Any digit 0-9. |
| graph | Any graphical character. |
| lower | Any lowercase character a-z, and other lowercase character. |
| print | Any printable character. |
| punct | Any punctuation character. |
| space | Any whitespace character. |
| upper | Any uppercase character A-Z, and other uppercase character. |
| xdigit | Any hexadecimal digit character, 0-9, a-f and A-F. |
| word | Any word character - all alphanumeric characters plus the underscore. |
| unicode | Any character whose code is greater than 255. (Regex.Boost only) |
| ascii | Any ASCII characters. (Onigmo only) |
| Hiragana | Any Hiragana character. (Onigmo only) |
| Katakana | Any Katakana character. (Onigmo only) |
| Han | Any Han character. (Onigmo only) |
| Hangul | Any Hangul character. (Onigmo only) |



## Single character escape sequences

The following escape sequences are aliases for single characters:

|     |     |     |
| --- | --- | --- |
| 0x07 | \\a | Bell character. |
| 0x0C | \\f | Form feed. |
| 0x0A | \\n | Newline character. |
| 0x0D | \\r | Carriage return. |
| 0x09 | \\t | Tab character. |
| 0x0B | \\v | Vertical tab. |
| 0x1B | \\e | ASCII Escape character. |
| 0dd | \\0dd | An octal character code, where dd is one or more octal digits (Boost.Regex only). |
| 0xXX | \\xXX | A hexadecimal character code, where XX is one or more hexadecimal digits (a Unicode character). |
| 0xXXXX | \\x{XXXX} | A hexadecimal character code, where XXXX is one or more hexadecimal digits (a Unicode character). |
| 0xXXXXXXXX | \\x{XXXXXXXX} | A hexadecimal character code, where XXXXXXXXis one or more hexadecimal digits (a Unicode character). (Onigmo only) |
| 0xXXXXXXXX | \\uXXXX | A hexadecimal character code, where XXXX is one or more hexadecimal digits (a Unicode character). (Onigmo only) |
| Z-'@' | \\cZ Z-'@' | An ASCII escape sequence control-Z, where Z is any ASCII character greater than or equal to the character code for '@'. |

## Word Boundaries

The following escape sequences match the boundaries of words:

|     |     |
| --- | --- |
| \\< | Matches the start of a word. (Boost.Regex only) |
| \\> | Matches the end of a word. (Boost.Regex only) |
| \\b | Matches a word boundary (the start or end of a word). |
| \\B | Matches only when not at a word boundary. |

## Character class escape sequences

The following escape sequences can be used to represent entire character
classes:

|     |     |
| --- | --- |
| \\w | Any word character - all alphanumeric characters plus the underscore. |
| \\W | Complement of \\w - find any non-word character |
| \\s | Any whitespace character. |
| \\S | Complement of \\s. |
| \\d | Any digit 0-9. |
| \\D | Complement of \\d. |
| \\l | Any lower case character a-z. |
| \\L | Complement of \\l. |
| \\u | Any upper case character A-Z. |
| \\U | Complement of \\u. |
| \\C | Any single character, equivalent to '.'. |
| \\Q | The begin quote operator, everything that follows is treated as a literal character until a \\E end quote operator is found. |
| \\E | The end quote operator, terminates a sequence begun with \\Q. |

## Replacement Expressions

See [Replacement Expression Syntax](replacement_expression_syntax).

## Notes

- In **Find in Files** and in **Replace in Files**, the carriage return (\\r) and the
line feed (\\n) must be specified carefully. See [To Specify newline characters](search_nl) for details.
- In order for some escape sequences to work in EmEditor, like "\\l", "\\u" and
their complements, the Match Case option has to be selected.
- Buffer boundaries ("\\`", "\\'", "\\A", "\\z", "\\Z") are not supported.

## Copyright Notice

The regular expression routines used in EmEditor use Boost library Regex++ and Onigmo.

Copyright (C) Dr John Maddock

Copyright (C) K. Takata, based on Oniguruma Copyright (C) by K. Kosako.

## See Also

- [Regular Expression Search Examples](search_reg_exp_ex)
- [To Specify newline characters](search_nl)
- [Boost.Regex: Regular Expression Syntax](https://www.boost.org/doc/libs/1_76_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html)
- [Onigmo: Regular Expression Syntax](https://github.com/k-takata/Onigmo/blob/master/doc/RE) (Notes: **\\nnn** and **\\xHH** are unsupported)
- [Onigmo: Unicode Properties](https://github.com/k-takata/Onigmo/blob/master/doc/UnicodeProps.txt)