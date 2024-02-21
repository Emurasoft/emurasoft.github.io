# Registered Devices page

The [Registered Devices page](https://support.emeditor.com/en/account/devices) contains a list of all devices that you have registered EmEditor on.

## Columns

Each device record contains the following information.

1. **Device ID**: This is the identifier for this device. A device has a unique combination of registry key, user ID, and machine ID. When you register EmEditor to a new device, a new device record is created. When EmEditor is renewed, a new device is created.
2. **Registration key**: This is the registration key that was used to register this device.
3. **Machine ID**: This identifies a Windows installation. It is copied from the Windows registry value for `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\MachineGuid`.
4. **Registration date**: The date when you registered EmEditor on the device.
5. **Last validation date**: The date when EmEditor last connected to our server to validate the registration. Validation occurs once each time EmEditor is opened on your device. EmEditor may connect to our server during validation, but this does not happen every time. Therefore, the last validation date may not be when you last opened EmEditor.
6. **Installation type**: This value can be "Desktop," "Portable," or "Store App," depending on how you installed EmEditor.
7. **Label**: This value contains what you wrote in the **Label** field of the **Register Product** dialog box. The label helps you to know which of your computers corresponds with this device record.
8. **Edit/Unregister**: Clicking on "Edit" allows you to change the label, check if the device is registered, and unregister the device.

## Device limit

You may register a certain number of devices per license. The limit is stated on your EULA. If you register more devices than allowed, you will see a notification in EmEditor.

## Unregister

To unregister EmEditor from a device, please uninstall EmEditor from that device or click **Downgrade** in the **Help** menu. You can also click Edit in this table to unregister the device.

## Support

If you encounter issues on registration, you can [contact us](https://www.emeditor.com/support/#contact) for support.

## More information

[Read the blog](https://www.emeditor.com/emeditor-core/29683/) for technical information about the registration and validation process.
