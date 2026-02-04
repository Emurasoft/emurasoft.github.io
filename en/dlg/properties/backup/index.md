# Backup page

The **Backup** page allows you to set properties related to backup
operations.

## Save backups to backup folder check box

When saving existing files, save the original files into the folder specified
in the **Backup Folder** text box.

## Save backups to the same folder check box

When saving existing files, save the original files in the same folder.

## Use Recycle Bin for backup check box

When saving existing files, the original files will be saved into the Recycle
Bin. However, the network drives and removable disk drives do not have Recycle
Bins and therefore this check will be ignored for those drives. In addition,
files whose sizes are greater than the Recycle Bin capacity will not be saved.

## Save to backup folder if the Recycle Bin is not available check box

If the **Use Recycle Bin for backup** check box
is checked, save the original file to the backup folder if saving to network
drives or removable disk drives. However, if the file size is greater than the
Recycle Bin capacity, the file will not be saved to the backup folder.

## Rename if the file name already exists check box

Rename the original files if the same file name already exists in the backup
folder or the same folder.

## Use ISO date/time format when renaming check box

Use ISO date time format for rename if the same file name already exists in the backup
folder or the same folder.

## Backup folder text box

Set the backup folder if the **Save backup to**
**Backup folder** check box or the **Save to backup folder if the Recycle Bin is not available** check box is checked. If the
folder name does not contain the path separating mark "\\", the sub folder name
is specified. For instance, if "backup" is specified and if the opened file is "C:\\work\\test.txt",
the backup will be made onto "C:\\work\\backup\\test.txt".
If the folder name contains the path separating mark "\\", the full path is
specified.

## ... button

Click this button to find the specified file.

## Set hidden attribute check box

Sets the hidden attribute to the new backup files and folder.

## Set read-only attribute check box

Sets the read-only attribute to the new backup files and folder.

## Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed and will allow you to copy from another configuration.

