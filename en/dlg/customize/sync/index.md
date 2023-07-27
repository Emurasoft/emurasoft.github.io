# Sync page

TheSync page allows you to customize sync settings.

## Sync Settings checkbox

Enable setting synchronization.

## Bidirectional radio button

This option updates EmEditor settings in other computers, and also updates EmEditor settings in the current computer. EmEditor uses the last saved settings when two computers are opening EmEditor at the same time.

## Send only radio button

Sends the settings to EmEditor in other computers, but does not update EmEditor settings in the current computer.

## Receive only radio button

Receives EmEditor settings from other computers, but does not send the settings to other computers.

## Microsoft Account radio button

Uses Microsoft Account to sync settings. Available only on the Store App versions.

## Network Folder radio button

Specifies a shared folder on the network to be shared by all computers. This can be a UNC (Universal Naming Convention) path, for instance, \\\computer1\\sharedFolder\\EmEditorSync, or a local folder, for instance, C:\\Users\\name\\OneDrive\\EmEditorSync.

## Monitor Interval text box

Specifies how often EmEditor checks if new settings become available in the shared folder. This option only affects the sending frequency and not the receiving frequency.

## Include supported plug-ins checkbox

If this is checked, plug-ins settings are also synced as long as the sync feature is supported to those plug-ins.

## Send Now button

Sends all settings to the shared folder.

## Receive Now button

Receives all settings from the shared folder.

## Reset button

Resets to default settings.

