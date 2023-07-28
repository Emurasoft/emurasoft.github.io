# Find in Files dialog box

This dialog box appears when the [**Find in Files** command](../../cmd/search/grep)
is selected. You can specify a string to find and other options to find in
files.

## Find drop-down list box

Enter a string to search for. If this is a multi-line text box, you can enter newline characters by pressing CTRL + ENTER. While the drop-down list is open, you may press ALT + DELETE to clear the selected history item.

## >button

Click this button to show the list of available commands.

|     |     |
| --- | --- |
| **Selected Text or Word at Cursor** | When this is checked, the dialog box initializes the Find <br> drop-down list box with the selected text or word at the cursor. |
| **Selected Text** | When this is checked, the dialog box initializes the Find drop-down list box with the selected text. |
| **Word at Cursor** | When this is checked, the dialog box initializes the Find drop-down list box with the word at the cursor. |
| **Last Used Value** | When this is checked, the dialog box initializes the Find drop-down list box with the last used string. |
| **Fixed Value** | When this is checked, the dialog box initializes the Find drop-down list box with the string set as the fixed value. |
| **Auto Save** | Saves the option (Selected Text, Word at Cursor, Last Used Value or Fixed Value) as the default for the next time the dialog box is displayed. |
| **Multiline** | Toggles between singleline and multiline of the drop-down list box. |
| **Use editor font** | When this is checked, the **Find** drop-down list box uses the same font as the editor. |
| **Select from Batch List** | Selects a string to search for from the batch list. |

The commands also include the list of available escape sequences or regular expressions. Selecting an item from the list will insert the selected item into the text box next to the button.

## File Types drop-down list box

File types to search within. Wild cards (\* and ?) can be used. Also multiple
file types can be separated with semicolons (;).

## \> button

Click this button to show the list of available commands.

|     |     |
| --- | --- |
| **Current File Type** | When this is checked, the dialog box initializes the File Types drop-down list using the current file type. |
| **Current File Extension** | When this is checked, the dialog box initializes the File Types drop-down list using the current file extension. |
| **Current File** | When this is checked, the dialog box initializes the File Types drop-down list using the current file. |
| **Last Used Value** | When this is checked, the dialog box initializes the File <br> Types drop-down list box with the last used string. |
| **Fixed Value** | When this is checked, the dialog box initializes the File <br> Types drop-down list box with the string set as the fixed value. |
| **Auto Save** | Saves the option (Current File Type, Current File Extension, Current <br> File or Last Used Value) as the default for the next time the dialog box is displayed. |

The commands also includes the list of available escape sequences or regular expressions. Selecting an item from the list will insert the selected item into the text box next to the button.

## In Folder drop-down list box

Specify the folder to be searched.

## \> button

Click this button to show the list of available commands.

|     |     |
| --- | --- |
| **Current Folder** | When this is checked, the dialog box initializes the In Folder drop-down list box with the current folder. |
| **Parent Folder** | When this is checked, the dialog box initializes the In Folder drop-down list box with the current parent folder. |
| **Grand Parent Folder** | When this is checked, the dialog box initializes the In Folder drop-down list box with the current grandparent folder. |
| **Root Folder** | When this is checked, the dialog box initializes the In Folder drop-down list box with the current root folder. |
| **Last Used Value** | When this is checked, the dialog box initializes the In <br> Folder drop-down list box with the last used string. |
| **Fixed Value** | When this is checked, the dialog box initializes the In <br> Folder drop-down list box with the string set as the fixed value. |
| **Browse** | Allows you to browse or search for the desired folder. |
| **Browse and Add** | Allows you to browse or search for the desired folder, and add to the existing specified folders. |
| **Auto Save** | Saves the option (Current Folder, Parent Folder, Grand Parent Folder, <br> Root Folder, Last Used Value or Browse) as the default for the next time the dialog box is displayed. |

The commands also includes the list of available escape sequences or regular expressions. Selecting an item from the list will insert the selected item into the text box next to the button.

## Match Case check box

Match cases when searching for a string.

## Look in Subfolders check box

Looks in subfolders of **In Folder** drop-down list box.

## Match Whole Word check box

Search words only. A word is defined as a string that begins and ends with
any of these characters: A – Z, a – z, 0 – 9, or an underscore. Strings
surrounded by full-width characters are considered as words. When using regular expressions, this check box may not work correctly. When using regular expressions, please use word boundary expressions (\\<, \\>, and \\b) instead.

## Close when Finished check box

Close the dialog box when finished searching.

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

## Encoding drop-down list box

Select the encoding. If you select **Configured Encoding**, the encoding associated with the opened file extension will be selected.

## Detect All check box

Statistically detect code page from all available code pages. The detection can make
mistakes especially when the file is very small. This option does not include HTML/XML charset detection.

## Detect HTML/XML Charset check box

Find "charset=..." from HTML files, "encoding=..." from XML files, or "#coding=..." from Python and Ruby files, and use the corresponding encoding. If you open HTML, XML, Python, or Ruby files, check only this option and clear the other options.

## Detect UTF-8 check box

Statistically detect UTF-8.

## Save Settings check box

Saves the encoding-related options ( **Encoding** drop-down list box, and **Detect All**, **Detect HTML/XML Charset**, and **Detect UTF-8** check boxes) as default so that these options will be restored next time when you open this dialog box.

## Output As drop-down list box

Selects how results are displayed.

|     |     |
| --- | --- |
| **Document** | Displays the Find in Files results as a list as a new document. |
| **Output Bar** | Displays the Find in Files results as a list in the Output Bar. |
| **Directly Open** | Directly open the document that includes the specified string. |
| **Directly Open and Filter** | Directly open the document that includes the specified string, and set the specified string as the filter. |

## Output Options drop-down list box

Selects how results are displayed.

|     |     |
| --- | --- |
| **Display File Names, Lines, and Matched Lines** | File names, line numbers, and the whole lines containing the searched string will be displayed as results. |
| **Display File Names Only** | Only file names will be displayed and the whole lines containing the searched string will not be displayed as results. |
| **Display Matched Lines Only** | Only the whole lines containing the searched string will be displayed as results. |
| **Display Matched Strings Only** | Only the matched strings will be displayed as results. |
| **Display File Names, Lines, and Matched Strings** | File names, line numbers and matched strings will be displayed. |
| **Display File Names and Matched Strings** | File names and matched strings will be displayed. |

## Stop if number of matches reaches check box/text box

EmEditor will stop searching files if the number of matches reaches the specified value when this check box is set.

## Find button

Start searching with the specified condition.

## Extract button

Extract the lines that match the specified string by creating a new document. Clicking the ▼ button on the right will display a context menu, where you can access the [**Extract Options** dialog box](../extract_options/index).

## Replace >> button

Click this button to save the current string to find and options, close the
current dialog box, and display the [**Replace in Files** dialog box](../replace_in_files/index).

## Close button

Click this button to close the dialog box.

## Advanced button

Click this button to display the [**Advanced** dialog box](../advanced/index) to set advanced options.

The following dialog box is also available through this dialog box.

## Add to Batch button

Adds the current settings to the batch list.

## Batch >> button

Toggles between the **Find in Files** dialog box and the **Batch Find in Files** dialog box.

The following controls appear only when the dialog box extends to the
**Batch Find in Files** dialog box.

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

## Enable/Disable All check box

Enables or disables all items in the list.

## Import button

Imports a previously exported TSV file containing the Find strings, Replace with strings and conditions.

## Export button

Exports defined find conditions into a file. The file format can be a TSV, JavaScript or VBScript macro format.

## Bulk Find button

Click this button to search for the selected items simultaneously.

## Batch Find button

Click this button to find the selected items. Clicking the ▼ button on the right will display a context menu, where you can access the [**Batch Options** dialog box](../batch_options/index).

## << Batch button

Toggles between the **Batch Find in Files** dialog box and the **Batch Find** dialog box.

This dialog box can be resized by dragging the right-bottom corner of the dialog box. When the dialog box becomes larger, a multi-line string can be entered as a search term. While multi-line text box is enabled, CTRL + ENTER key can be used to
insert newline characters.

The following dialog box is also available through this dialog box.

 (Select **Advanced** button)

 (Select **Extract Options**)

 (Select **Batch Options**)

