# Sync page

The **Sync** page allows you to customize sync settings.

## Sync settings checkbox

Enables setting synchronization.

## Bidirectional radio button

This option updates EmEditor settings in other computers, and also updates EmEditor settings in the current computer. When two computers change settings before they receive each other's settings, EmEditor keeps the changes of both computers: each setting comes from the computer that changed it. If both computers changed the same setting, the later change is used.

## Send only radio button

Sends the settings to EmEditor in other computers, but does not update EmEditor settings in the current computer.

## Receive only radio button

Receives EmEditor settings from other computers, but does not send the settings to other computers.

## Network folder text box

Specifies a shared folder on the network to be shared by all computers. This can be a UNC (Universal Naming Convention) path, for instance, \\\\computer1\\sharedFolder\\EmEditorSync, or a local folder, for instance, C:\\Users\\name\\OneDrive\\EmEditorSync.

When you turn on the sync or change the folder, and the folder already has settings from another computer, EmEditor asks whether to use the settings in the Sync folder or to replace the Sync folder with the settings on this computer. Sync via a Microsoft account is no longer available.

## Monitor interval text box

Specifies how often EmEditor checks if new settings become available in the shared folder. This option only affects the receiving frequency and not the sending frequency.

## Include supported plug-ins checkbox

If this is checked, plug-ins settings are also synced as long as the sync feature is supported to those plug-ins.

## Send Now button

Sends all settings to the shared folder. The settings in the shared folder are replaced, including changes from other computers that this computer has not received yet.

## Receive Now button

Receives all settings from the shared folder. The settings on this computer are replaced, including changes that have not been sent yet.

## Reset button

Resets to default settings.

