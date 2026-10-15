# Fast View page

The **Fast View** page allows you to customize settings related to Fast View mode, and to manage the diff files that store the edits and the line positions of huge files. See [To Open and Edit Huge Files in Fast View Mode](../../../howto/file/file_fast_view) for details about Fast View mode.

## Options list box

### Prompt when saving a huge file in Fast View mode

If this is checked, saving a document with edits in Fast View mode asks whether to merge the edits into the file now, or to save only the changes to a diff file and leave the original file untouched. This option is checked by default.

### Save only the changes to a diff file when saving a huge file in Fast View mode

If this is checked, saving a document with edits in Fast View mode saves only the changes to a diff file. If this is cleared, the changes are merged into the file. This option can be changed only when the **Prompt when saving a huge file in Fast View mode** option is cleared. It is also used when macros save a document. This option is cleared by default.

### Save the line positions of huge files so they open instantly next time

If this is checked, EmEditor saves the positions of the lines of a file opened in Fast View mode to a diff file after the positions are found, and when the file is saved, if the file is larger than the **Minimum file size to enable Fast View mode**. The next time the file is opened, EmEditor uses the saved positions instead of finding the positions of the lines again. This option is checked by default.

## Minimum file size to enable Fast View mode text box

Specifies the minimum file size in megabytes (MB). Files of this size or larger are opened in Fast View mode automatically. The default is 4,096 MB. If **0** is specified, files are not opened in Fast View mode automatically.

## Diff files list

Lists the diff files that store the edits and the line positions of files opened in Fast View mode. Each item shows the **File Name** and **Folder** of the original file, the number of **Edits** (0 if the diff file has only line positions), the **Size** of the diff file, and the date and time it was **Last Saved**. Files that no longer exist are grayed. Click a column header to sort the list.

Right-click an item to display a menu, where you can select **Open Folder** to open the folder of the file, or **Copy Path** to copy the path of the file to the Clipboard. Press **Delete** to clear the selected items, and press **Ctrl+A** to select all items.

## Clear button

Clears the selected items from the list.

## Clear All button

Clears all items from the list.

## Clear Missing button

Clears the items whose files no longer exist.

The diff files of the cleared items are deleted when you click **OK**. If some of the cleared diff files store edits, EmEditor asks for confirmation, because those edits will be permanently erased. Click **Cancel** to keep all the diff files.

## Folder link

Opens the folder where the diff files are saved (the **FastView** folder in the local application data folder of EmEditor).

## Reset button

Resets the options and the minimum file size to default settings. The diff files are not deleted.
