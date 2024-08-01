# Offline Registration

Registration using the [Register Product dialog box](../../dlg/regist/index) requires an internet connection.

If you experienced the error message "Request error: sending request for url…No such host is known." during online registration, please ensure that your firewall allows `EmEditor.exe` to access `support.emeditor.com` via ports 80 and 443.

If you would like to register EmEditor without an internet connection, you can use the offline registration feature. Offline registration requires EmEditor version 24.3.0 or later.

Offline registration uses a license file during registration. The license file is delivered to customers by email. Follow these steps to register EmEditor using an offline license.

1. Request a license file using the [contact form](https://www.emeditor.com/support/#contact). In the form, please use the email address that you use for [Emurasoft Customer Center](https://support.emeditor.com/). Include your registration key or [Stripe subscription ID](https://support.emeditor.com/en/account/subscriptions).
2. We will respond to your request with an email message with the license file attached. Download the license file to a folder in a local disk that does not require administrator permissions to access.
3. If you have already registered EmEditor, unregister using [Registration Information](../../dlg/registration_info/index).
4. Close EmEditor. Use the [command line option](https://www.emeditor.org/en/howto/file/file_commandline.html#options) `/ol "licenseFilePath"` where `licenseFilePath` is the path to the license file. The following is an example of the command.

```
EmEditor.exe /ol "C:\Users\Example\emeditorLicenseFile-a7PT7Au3TOelfK1w.txt"
```

5. Open EmEditor and view [Registration Information](../../dlg/registration_info/index) to confirm that offline registration was successful. The license file can be deleted now as it is no longer needed to use EmEditor.

## Technical information

The internal details about offline registration can be viewed [here](https://www.emeditor.com/general/new-validation-system-explained/).