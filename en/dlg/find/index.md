# Find dialog box

This dialog box appears when the [**Find** command](../../cmd/search/edit_find)
is selected. You can specify a string to find, as well as other options.

## Find drop-down list box

Enter a string to search for. If this is a multi-line text box, you can enter newline characters by pressing CTRL + ENTER. While the drop-down list is open, you may press ALT + DELETE to clear the selected history item.

## \> button

Click this button to show the list of available commands.

|     |     |
| --- | --- |
| **Selected text or word at the cursor** | When this is checked, the dialog box initializes the Find drop-down list box with the selected text or the word at the cursor. |
| **Selected Text** | When this is checked, the dialog box initializes the Find drop-down list box with the selected text. |
| **Word at the Cursor** | When this is checked, the dialog box initializes the Find drop-down list box with the word at the cursor. |
| **Last used value** | When this is checked, the dialog box initializes the Find drop-down list box with the last used string. |
| **Fixed value** | When this is checked, the dialog box initializes the Find drop-down list box with the string set as the fixed value. |
| **Auto Save** | Saves the option (Selected Text, Word at Cursor, Last Used Value or Fixed Value) as the default for the next time the dialog box is displayed. |
| **Multiline** | Toggles between singleline and multiline of the drop-down list box. |
| **Use editor font** | When this is checked, the **Find** drop-down list box uses the same font as the editor. |
| **Auto Highlight** | When this is checked, matched strings are highlighted automatically as you type in the **Find** drop-down list box. Highlighting will be disabled when you close this dialog box. This option also affects the **Find** toolbar. |
| **Select from Batch List** | Selects a string to search for from the batch list. |

The commands also include the list of available escape sequences or regular expressions. Selecting an item from the list will insert the selected item into the text box next to the button.

## Match case checkbox

Matches cases when searching for a string.

## Match whole word checkbox

Searches words only. A word is defined as a string that begins and ends with
any of these characters: A – Z, a – z, 0 – 9, or an underscore. Strings
surrounded by full-width characters are considered words. When using regular expressions, this checkbox may not work correctly. When using regular expressions, please use word boundary expressions (\\<, \\>, and \\b) instead.

## Incremental search checkbox

When this is checked, the search immediately starts as you type in the **Find** drop-down list box.

## Search all documents in the group checkbox

Searches all open documents in the same frame window.

## In the selection only checkbox

Searches only the selection of the document.

## Wrap around checkbox

Searches down from the current position by choosing **Find Next**. If the word is not found by the end of the file, it will continue searching from the top of the file. **Find Previous** will search from the current position up to the beginning of the file. If the word has not been found, it will continue searching from the bottom of the file.

## Count matches checkbox

If this is checked, EmEditor counts the occurrences of the matched string in the
document. The result will be displayed in the status bar. This option will be ignored if **linked files** are included in the **List box** and **Multi-Find Next** or **Multi-Find Previous** button is selected.

## Close when finished checkbox

Closes the dialog box when EmEditor finishes searching.

## (None) radio button

Specifies that the string should match literally.

## **Regular expressions** radio button

Enables [regular expressions](../../howto/search/search_regexp).

## **Escape sequence** radio button

Enables escape sequences. You can use the following characters as escape sequences.

|     |     |
| --- | --- |
| **\\a** | Warning (Bell) |
| **\\b** | Backspace |
| **\\f** | Form feed |
| **\\n** | Newline character |
| **\\t** | Horizontal tab |
| **\\v** | Vertical tab |
| **\\\\** | Backslash |
| **\\oooooo** | Unicode character in octal notation |
| **\\xhhhh** | Unicode character in hexadecimal notation |

A null character (\\0) may not be used. \\n must be used instead of \\r.

## **Number range** radio button

Enables [number range expressions](../../howto/search/number_range_syntax).

## **Fuzzy matching** checkbox

Enables [fuzzy matching options](../fuzzy_options/index). If **Fuzzy matching** is already selected, clicking the **...** button on the right will open the [**Fuzzy Matching Options**](../fuzzy_options/index) dialog box. 

## Find Previous button

Searches previous from the current position.

## Find Next button

Searches next from the current position.

## Select All button

Finds and selects all occurrences of the search term.

## Bookmark button

Bookmarks all lines that match the specified string.

## Extract button

Extracts the lines that match the specified string by creating a new document. Clicking the ▼ button on the right will display a context menu, where you can access the [**Extract Options** dialog box](../extract_options/index).

## Replace >> button

Click this button to display the [**Replace** dialog box](../replace/index) for the specified string with selected options.

## Close button

Click this button to close the dialog box.

## Advanced button

Click this button to display the [**Advanced** dialog box](../advanced/index).

## Add to Batch button

Adds the current settings to the batch list.

## Batch >> button

Toggles between the **Find** dialog box and the **Batch Find** dialog box.

The following controls appear only when the dialog box extends to the
**Batch Find** dialog box.

## Save to Batch button

Saves the current settings to the batch list.

## List box

Displays the list of find strings to be used for the batch process. The following abbreviations are used for the Condition column.

|     |     |
| --- | --- |
| **C** | Match Case |
| **R** | Use Regular Expressions |
| **W** | Search Only Word |
| **E** | Match Only Embedded Newlines in CSV |
| **S** | Treat CR and LF Separately |
| **D** | Regular Expression "." can Match Newlines |
| **B** | Use Boost.Regex as the Regular Expression Engine |
| **O** | Use Onigmo as the Regular Expression Engine |

## Enable/Disable All checkbox

Enables or disables all items in the list.

## Import button

Imports a previously exported TSV file containing the Find strings, Replace with strings and conditions.

## Export button

Exports defined find conditions into a file. The file format can be a TSV, JavaScript or VBScript macro format.

## Multi-Find Previous button

Search multiple selected items from the batch list before the current position.

## Multi-Find Next button

Search multiple selected items from the batch list after the current position.

## Batch Bookmark button

Click this button to bookmark all lines that match the selected items from the batch list.

## Batch Extract button

Click this button to extract the selected item in the batch list. Clicking the ▼ button on the right will display a context menu, where you can access the [**Batch Options** dialog box](../batch_options/index).

## Filter All button

Click this button to filter the selected item in the batch list.

## Abort Filter button

Click this button to abort filtering the selected item in the batch list.

## << Batch button

Toggles between the **Batch Find** dialog box and the **Find** dialog box.

This dialog box can be resized by dragging the right-bottom corner of the dialog box. When the dialog box becomes larger, a multi-line string can be entered as a search term. While multi-line text box is enabled, CTRL + ENTER key can be used to insert newline characters.

The following dialog boxes are also available through this dialog box.

[**Advanced** dialog box](../advanced/index) (Select **Advanced** button)

[**Extract Options** dialog box](../extract_options/index) (Select **Extract Options**)

[**Batch Options** dialog box](../batch_options/index) (Select **Batch Options**)

