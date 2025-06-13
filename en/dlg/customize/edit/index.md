# Edit page

The **Edit** page allows you to customize settings related to edit
operations.

## Specify Tag Format using Regular Expressions check box

Uses regular expressions to specify the tag format.

## Find text box

Specifies a regular expression to match a tag.

## File Name text box

Specifies a regular expression to match a file name.

## Line text box

Specifies a regular expression to match a line number.

## Column text box

Specifies a regular expression to match a column number.

## Save Insert/Overwrite Mode check box

If this box is checked, **Insert/Overwrite** mode will be saved, and the next time
you start a new EmEditor window, the **Insert/Overwrite** mode will restored. If
this box is not checked, EmEditor always starts with the insert mode.

## Enable Multiple Selections check box

Specifies whether you want to enable multiple selections. To make multiple selections, after making one selection, make another selection with the mouse while pressing the CTRL key. Alternatively, you can press the F8 key, move the cursor to extend the selection, press the F8 key again to finish the selection, move the cursor again to go to the next selection position, and repeat this procedure until you make all selections.

## Read Only when a temporary file is opened with View Source on Internet Explorer check box

Read Only when a temporary file is opened with View Source in Internet Explorer.

## Prompt when EmEditor cannot open the Clipboard check box

Displays a dialog box to prompt users when EmEditor cannot open the Clipboard.

## Keep Horizontal Cursor Position check box

After inserting a string and moving the cursor up or down, returns the cursor position to the same horizontal position as the position before inserting the string.

## Undo Character by Character (need to restart EmEditor) check box

If this box is checked, the [**Undo** command](../../../cmd/edit/edit_undo) will undo the word, character by character.
This action will also affect macros which record an insert command, character by character. To activate the new settings, you need to restart EmEditor.

## Always Discard Lengthy Undo Information to Accelerate check box

Always discards lengthy undo information. EmEditor determines that Undo information is
lengthy enough to discard if one of the following conditions is met: (1) the number of lines is greater than 3,000,000 lines. (2) the number of characters is greater than 100,000,000. (3) the percentage of the system physical memory in use is greater than the **Maximum Memory Size** specified in the **Advanced** page of the **Customize** dialog box.

## Prompt when No Undo Information is Available check box

Displays a dialog box to prompt users when no Undo information is available.

## Auto Copy check box

This option allows you to copy the selection automatically to the Clipboard without selecting the Copy command (CTRL + C). While the **Auto Copy** mode is on, the selection will be copied to the Clipboard immediately before the selection is deselected or deleted, immediately before the active document is switched, or the editor loses the keyboard focus. However, it does not work during the CSV cell mode.

## Prompt when Very Long Lines Exist check box

Displays a dialog box to prompt users when very long lines exist in the document.

## Treat Ambiguous Width Characters as Fullwidth check box

Treats ambiguous characters defined in " [Unicode Standard Annex #11 - East Asian Width](http://www.unicode.org/reports/tr11/)" as Fullwidth.

## Add Additional Information to the Undo/Redo History check box

If this is checked, EmEditor will add additional information, such as command name and bookmarks positions, in the comment when you export the Undo/Redo history.

## Always insert newlines when copying multiple selections check box

If this is checked, EmEditor will insert newline characters when you copy multiple selections so that it can paste to another multiple selections.

## Keep selections while typing in multiple selections check box

If this is checked, EmEditor will keep selections while typing in multiple selections, and confine the cursors to the multiple selection range when you move the cursor via arrow keys.

## Alternative behavior of the Word Right command check box

If this is checked, EmEditor will use an alternative behavior of the [**Word Right**](../../../cmd/edit/right_word) command.

## Alternative behavior of the Word Left command check box

If this is checked, EmEditor will use an alternative behavior of the [**Word Left**](../../../cmd/edit/left_word) command.

## Ignore the last character in the selection on the Insert/Remove Newline Characters commands check box

If this is checked, EmEditor will ignore the last character in the selection when executing the Insert/Remove Newline Characters commands.

## Inspect only selected strings when vertical selection or multiple selections exist (Delete Duplicates command) check box

If this is checked, EmEditor will inspect only selected strings for duplication when vertical selection or multiple selections exist.

## Extend selection on the Duplicate Lines/Columns commands check box

If this is checked, EmEditor will extend selection when you run Duplicate Lines/Columns commands.

## Locale-dependent Uppercase/Lowercase check box

If this is checked, the **Uppercase**, **Lowercase**, and **Capitalize** commands will depend on the locale specified in the **Sort** page of the **Customize** dialog box.

## Use .editorconfig

Uses .editorconfig file to format coding styles. If this option is turned on, some of EmEditor features will be disabled. See [EditorConfig](https://editorconfig.org/).

## Treat the following characters as alphanumeric text box

Treats the following characters as alphanumeric when editing. For instance, when you double-click a word, these characters are treated as a part of the word. However, this setting does not apply to the regular expression \\w operator in the Find dialog box.

## Reset button

Resets to default settings.

