# Workspace page

The **Workspace** page allows you to customize settings related to EmEditor
workspaces.

## Automatic workspace drop-down list box

Specifies the save and load behavior. Select one of the following options:

|     |     |
| --- | --- |
| **None** | Does not save or restore the workspace. |
| **Save only** | The workspace will be saved automatically when the last group is about to close, but will not restore the workspace automatically when EmEditor is launched. |
| **Load only** | The workspace will be restored automatically when EmEditor is launched, but will not save the workspace automatically when the last group is about to close. |
| **Save and restore** | The workspace will be saved automatically when the last group is about to close, and restored automatically when EmEditor is launched. |
| **Save, restore and keep undo information** | The workspace will be saved automatically when the last group is about to close, and restored automatically when EmEditor is launched. The undo and redo information is also saved and restored. |
| **Save, Restore and Keep Undo Information, and No Prompt to Save Files** | The workspace will be saved automatically when the last group is about to close, and restored automatically when EmEditor is launched. The undo and redo information is also saved and restored, and no prompt to save files is displayed when you close the last group. |

## Do not ask before exiting checkbox

If this box is checked, a dialog box to select workspace options will not be displayed when exiting.

## Do not include files in the temporary folder checkbox

Specifies that a workspace should not include files that are using the temporary folder.

## Do not include files with more than this many lines checkbox

Specifies that a workspace should not include files of which the number of lines exceed the specified number.

## Save workspace after a crash checkbox

If this is checked, EmEditor saves the workspace on crash, and allows you to restore the workspace next time EmEditor is launched.

## Save workspace periodically checkbox

If this is checked, EmEditor saves the workspace periodically at the specified interval, and allows you to restore the workspace when EmEditor is launched.

## Do not display the Save Workspace button in the "Save Changes?" dialog box checkbox

If this is checked, EmEditor does not display the Save Workspace button in the "Save Changes?" dialog box.

## Reset button

Resets to default settings.

