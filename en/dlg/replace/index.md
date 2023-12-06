# Replace dialog box

This dialog box appears when the [Replace command](../../cmd/search/edit_replace) is selected. You can specify a string to find and a string to replace it with, as well
as other
options.

## Find drop-down list box

Enter a string to search for. If this is a multi-line text box, you can enter newline characters by pressing CTRL + ENTER. While the drop-down list is open, you may press ALT + DELETE to clear the selected history item.

## Replace with drop-down list box

Enter a string with which you want to replace the original string. If this is a multi-line text box, you can enter newline characters by pressing CTRL + ENTER. While the drop-down list is open, you may press ALT + DELETE to clear the selected history item.

## \> button

Click this button to show the list of available commands.

|     |     |
| --- | --- |
| **Selected Text or Word at Cursor** | When this is checked, the dialog box initializes the Find drop-down list box with the selected text or the word at the cursor. |
| **Selected Text** | When this is checked, the dialog box initializes the Find drop-down list box with the selected text. |
| **Word at Cursor** | When this is checked, the dialog box initializes the Find drop-down list box with the word at the cursor. |
| **Last Used Value** | When this is checked, the dialog box initializes the Find drop-down list box with the last used string. |
| **Fixed Value** | When this is checked, the dialog box initializes the Find drop-down list box with the string set as the fixed value. |
| **Auto Save** | Saves the option (Selected Text or Word at Cursor, Selected Text, Word at Cursor, Last Used Value or Fixed Value) as the default for the next time the dialog box is displayed. |
| **Multiline** | Toggles between singleline and multiline of the drop-down list boxes. |
| **Use editor font** | When this is checked, the **Find**/**Replace** drop-down list boxes uses the same font as the editor. |
| **Select from Batch List** | Selects a string to search for from the batch list. |
| **Swap Find and Replace strings** | Swaps Find and Replace strings. |
| **Synchronize with Find** | Remembers Find and Replace with strings as a pair, and automatically updates the Replace with string when the Find string is changed. |

The commands also include the list of available escape sequences or regular expressions. Selecting an item from the list will insert the selected item into the text box next to the button.

## Match Case check box

Match cases when searching for a string.

## Match Whole Word check box

Search words only. A word is defined as a string that begins and ends with any of these characters: A – Z, a – z, 0 – 9, or an underscore. Strings surrounded by full-width characters
are considered words. When using regular expressions, this check box may not work correctly. When using regular expressions, please use word boundary expressions (\\<, \\>, and \\b) instead.

## Incremental Search check box

When this is checked, the search immediately starts as you type in the **Find** drop-down list box.

## Search All Documents in the Group check box

Searches all open documents in the same frame window.

## In the Selection Only check box

Replace within the selected text only.

## Wrap Around check box

Search down from the current position by choosing **Find Next** or **Replace**. If the word is not found by the end of the file, it will continue searching from the top of the file.

## Close when Finished check box

Close the dialog box when finished replacing.

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

## Find Next button

Search next from the current position.

## Replace button

Replace and search for the next occurrence of the string.

## Replace All button

Replace all strings in the document.

## Extract button

Find and extract all occurrences of the search term. The exact behavior depends on which option is selected in the context menu displayed when the ▼ button on the right is clicked.

|     |     |
| --- | --- |
| **New Document** | Finds and extracts all occurrences of the search term using regular expressions, and replace them with replace expressions. EmEditor displays the search results as a list in a new document. |
| **Use Output Bar** | Finds and extracts all occurrences of the search term using regular expressions, and replace them with replace expressions. EmEditor displays the search results as a list in the Output Bar. |
| **To New CSV Column** | Creates a new CSV column filled with the replaced strings, while the original column remains unchanged. If the **Use Regular Expression** option is not set, the text specified in the **Replace with** drop-down list box must be empty, and the new column will be filled with the matched terms without any <br> changes. The new column is inserted just to the right of the original. |

## << Find button

Click this button to display the [**Find** dialog box](../find/index) for the specified string with selected options.

## Advanced button

Click this button to display the [**Advanced** dialog box](../advanced/index).

## Close button

Click this button to close the dialog box.

## Add to Batch button

Adds the current settings to the batch list.

## Batch >> button

Toggles between the **Replace** dialog box and the **Batch Replace** dialog box.

The following controls appear only when the dialog box extends to the
**Batch Replace** dialog box.

## Save to Batch button

Saves the current settings to the batch list.

## List box

Displays the list of find and replace combinations to be used for the batch process. The following abbreviations are used for the Condition column.

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

## Enable/Disable All check box

Enables or disables all items in the list.

## Import button

Imports a previously exported TSV file containing the Find strings, Replace with strings and conditions.

## Export button

Exports defined replace conditions into a file. The file format can be a TSV, JavaScript or VBScript macro format.

## Multi-Find Next button

Search multiple selected items from the batch list after the current position.

## Bulk Replace All button

Replaces all strings in the document using the batch list simultaneously. See [**Difference between Batch and Bulk**](../../howto/search/batch_vs_bulk) for more information.

## Batch Replace All button

Replaces all strings in the document using the batch list.

## Batch Extract button

Click this button to extract the selected item in the batch list. Clicking the ▼ button on the right will display a context menu, where you can access the [**Batch Options** dialog box](../batch_options/index).

## Filter All button

Click this button to filter the selected item in the batch list.

## Abort Filter button

Click this button to abort filtering the selected item in the batch list.

## << Batch button

Toggles between the **Batch Replace** dialog box and the **Replace** dialog box.

This dialog box can be resized by dragging the right-bottom corner of the dialog box. When the dialog box becomes larger, a multi-line string can be entered as a search term. While multi-line text box is enabled, CTRL + ENTER key can be used to
insert newline characters.

The following dialog box is also available through this dialog box.

<a href="../advanced/index.htm"><b>Advanced</b> dialog box</a> (Select **Advanced** button)

<a href="../extract_options/index.htm"><b>Extract Options</b> dialog box</a> (Select **Extract Options**)

<a href="../batch_options/index.htm"><b>Batch Options</b> dialog box</a> (Select **Batch Options**)

