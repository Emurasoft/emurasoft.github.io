# String/Character Range dialog box

This dialog box appears when the [Add button](../../properties/char_check/index)
on the [Fuzzy Matching Options dialog box](../index) is selected.

## String radio button/text box

Selects a string, and specifies a string to match.

## Character Range radio button

Selects a character range.

## Unicode Script list box

Selects Unicode scripts.

## Unicode General Category list box

Selects Unicode general category.

## Minimum character text box

Enter the minimum character of a range. You may enter at least 4-digit character code value in a hexadecimal value with or without "U+" prefix, or actual one character. For instance, you may enter: "U+0061", "0061", or "a".

## Maximum character text box

Enter the maximum character of a range as the same format as theMinimum character text box.

## Treat as - Ignore radio button

Ignores the matched string or character.

## Treat as - A string text box

Enter a character or a string to be substituted for. If this is empty, the specified string or character range is ignored. The string or character can include the following escape sequences.

|     |     |
| --- | --- |
| \\a | Warning (Bell) |
| \\b | Backspace |
| \\t | Horizontal tab |
| \\v | Vertical tab |
| \\\ | Backslash |
| \\xhhhh | Unicode character in hexadecimal notation |

