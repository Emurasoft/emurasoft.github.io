# Backup page

The **Backup** page allows you to set properties related to backup
operations.

## Save Backups to Backup Folder check box

When saving existing files, save the original files into the folder specified
in the **Backup Folder** text box.

## Save Backups to the Same Folder check box

When saving existing files, save the original files in the same folder.

## Use Recycle Bin to Backup check box

When saving existing files, the original files will be saved into the Recycle
Bin. However, the network drives and removable disk drives do not have Recycle
Bins and therefore this check will be ignored for those drives. In addition,
files whose sizes are greater than the Recycle Bin capacity will not be saved.

## Save to Backup Folder if Recycle Bin not Available check box

If the **Use Recycle Bin to Backup** check box
is checked, save the original file to the backup folder if saving to network
drives or removable disk drives. However, if the file size is greater than the
Recycle Bin capacity, the file will not be saved to the backup folder.

## Rename if the Same File Name Exists check box

Rename the original files if the same file name already exists in the backup
folder or the same folder.

## Use ISO date time format for rename check box

Use ISO date time format for rename if the same file name already exists in the backup
folder or the same folder.

## Backup Folder text box

Set the backup folder if the **Save Backup to**
**Backup Folder** check box or the
**Save**
**to Backup Folder if Recycle Bin not Available** check box is checked. If the
folder name does not contain the path separating mark "\\", the sub folder name
is specified. For instance, if "backup" is specified and if the opened file is "C:\\work\\test.txt",
the backup will be made onto "C:\\work\\backup\\test.txt".
If the folder name contains the path separating mark "\\", the full path is
specified.

## ... button

Click this button to find the specified file.

## Set Hidden attribute check box

Sets the Hidden attribute to the new backup files and folder.

## Set Read-only attribute check box

Sets the Read-only attribute to the new backup files and folder.

## Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed
and will allow you to copy from another configuration.

