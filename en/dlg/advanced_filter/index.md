# Advanced Filter dialog box

This dialog box appears when the
**Advanced Filter** command or the
**Advanced Filter** button is selected in the **Filter** toolbar.

## Find \| Columns \| Conditions list box

Shows the list of defined filters.

## Enable/Disable All check box

Enables or disables all items in the list.

## Column drop down list box

Changes the column for the items selected in the list.

## Begin text box

Specifies the one-based index of the character where the search begins.

## End text box

Specifies the one-based index of the character where the search ends. The specified ending character is exclusive. For instance, if you specify 1 in the Begin text box, and 2 in the End text box, only one character (2-1=1) will be searched.

## Count Last check box

If this is checked, the search range is counted from the end of the line.

## All the Rest check box

If this is checked, the search range is up to the end of the line.

## Match Case check box

Match cases when searching for a string.

## Match Whole Word check box

Search words only. A word is defined as a string that begins and ends with
any of these characters: A – Z, a – z, 0 – 9, or an underscore. Strings
surrounded by full-width characters are considered words. When using regular expressions, this check box may not work correctly. When using regular expressions, please use word boundary expressions (\\<, \\>, and \\b) instead.

## Match Whole String check box

This matches the whole item in the selected column, character positions, or the whole line. It is recommended to set this option whenever possible to optimize the filter for speed. When multiple filter conditions are defined with the Logical Disjunction, set this option for all conditions to increase the filter speed extremely faster.

## Negative check box

This negates the match condition. Therefore, the lines matched to the specified string will be hidden from the document when displayed. This option does not affect the **Bookmarked Lines Only**, **Unbookmarked Lines Only**, or **Match Newline Characters** options.

## Bookmarked Lines Only check box

Matches bookmarked lines only.

## Unbookmarked Lines Only check box

Matches unbookmarked lines only.

## (None) radio button

Specifies that the string should match literally.

## **Regular Expressions** radio button

Enables [regular expressions](../../howto/search/search_regexp).

## **Escape Sequence** radio button

Enables escape sequences. You can use the following characters as escape
sequences.

|     |     |
| --- | --- |
| **\\a** | Warning (Bell) |
| **\\b** | Backspace |
| **\\f** | Form feed |
| **\\n** | Newline character |
| **\\t** | Horizontal tab |
| **\\v** | Vertical tab |
| **\\\** | Backslash |
| **\\oooooo** | Unicode character in octal notation |
| **\\xhhhh** | Unicode character in hexadecimal notation |

A null character (\\0) may not be used. \\n must be used instead of \\r.

## **Number Range** radio button

Enables [number range expressions](../../howto/search/number_range_syntax).

## Match Newline Characters check box

Matches specified newline characters. This option should be combined with **CR Only**, **LF Only**, **CR+LF Only**, and/or **Others** check boxes.

## CR Only check box

Matches lines of which the newline character is CR only. This option should be combined with the **Match Newline Characters** option.

## LF Only check box

Matches lines of which the newline character is LF only. This option should be combined with the **Match Newline Characters** option.

## CR+LF check box

Matches lines of which the newline character is CR and LF. This option should be combined with the **Match Newline Characters** option.

## Others check box

Matches lines without a newline character. These lines includes the last line of the file and very long lines that continue to the next line without a newline character. This option should be combined with the **Match Newline Characters** option.

## Begin Filter check box

Specifies a begin filter. If both an item with the begin filter and another item with the end filter exist, EmEditor shows only the lines between the line that matches the begin filter and the line that matches the end filter.

## End Filter check box

Specifies an end filter.

## Logical Disjunction (OR) to the Previous Condition check box

Specifies a logical disjunction (logical OR) to the previous condition. If this is not checked, a logical conjunction (logical AND) is specified.

## Filter button

Applies the specified conditions.

## Bookmark button

Bookmark lines that satisfy the specified conditions.

## Abort button

Aborts the current filters.

## Import button

Imports a previously exported TSV file containing the filter conditions.

## Export button

Exports defined filter conditions into a file. The file format can be a TSV, JavaScript or VBScript macro format.

