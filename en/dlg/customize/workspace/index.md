# Workspace page

TheWorkspace page allows you to customize settings related to EmEditor
workspaces.

## Automatic Workspace drop-down list box

Specifies the save and load behavior. Select one of the following options:

|     |     |
| --- | --- |
|None | Does not save or restore the workspace. |
|Save Only | The workspace will be saved automatically when the last group is about to close, but will not restore the workspace automatically when EmEditor is launched. |
|Load Only | The workspace will be restored automatically when EmEditor is launched, but will not save the workspace automatically when the last group is about to close. |
|Save and Restore | The workspace will be saved automatically when the last group is about to close, and restored automatically when EmEditor is launched. |
|Save, Restore and Keep Undo Information | The workspace will be saved automatically when the last group is about to close, and restored automatically when EmEditor is launched. The undo and redo information is also saved and restored. |
|Save, Restore and Keep Undo Information, and No Prompt to Save Files | The workspace will be saved automatically when the last group is about to close, and restored automatically when EmEditor is launched. The undo and redo information is also saved and restored, and no prompt to save files is displayed when you close the last group. |

## Do not ask before exiting check box

If this box is checked, a dialog box to select workspace options will not be displayed when exiting.

## Do not include files that are using temporary folder check box

Specifies that a workspace should not include files that are using the temporary folder.

## Do not include files of which the number of lines exceed check box

Specifies that a workspace should not include files of which the number of lines exceed the specified number.

## Save workspace on crash check box

If this is checked, EmEditor saves the workspace on crash, and allows you to restore the workspace next time EmEditor is launched.

## Save workspace periodically check box

If this is checked, EmEditor saves the workspace periodically at the specified interval, and allows you to restore the workspace when EmEditor is launched.

## Do not display the Save Workspace button in the "Save Changes?" dialog box check box

If this is checked, EmEditor does not display the Save Workspace button in the "Save Changes?" dialog box.

## Reset button

Resets to default settings.

