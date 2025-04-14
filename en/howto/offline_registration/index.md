# Offline Registration

Registration using the [Register Product dialog box](../../dlg/regist/index) requires an internet connection.

If you encountered the error message "Request error: sending request for url…No such host is known." during online registration and your system requires specific proxy settings for internet access, you can configure them in [Customize Proxy](../../dlg/customize/proxy/index).

If you would like to register EmEditor without an internet connection, you can use the offline registration feature. Offline registration requires EmEditor version 24.4.2 or later.

Offline registration uses a license file during registration. The license file is delivered to customers by email. Follow these steps to register EmEditor using an offline license.

1. Request a license file using the [contact form](https://www.emeditor.com/support/#contact). In the form, please use the email address that you use for [Emurasoft Customer Center](https://support.emeditor.com/). Include your registration key or [Stripe subscription ID](https://support.emeditor.com/en/account/subscriptions).
2. We will respond to your request with an email message with the license file attached. Download the license file to a folder in a local disk that does not require administrator permissions to access.
3. If you have not installed EmEditor yet, install EmEditor. You do not need to add the [`REGKEY`](https://www.emeditor.com/faq/installation-faq/how-can-i-install-emeditor-without-displaying-dialog-boxes/) option when installing.
4. If you have already registered EmEditor, unregister using [Registration Information](../../dlg/registration_info/index).
5. Close EmEditor. Use the [command line option](https://www.emeditor.org/en/howto/file/file_commandline.html#options) `/ol "licenseFilePath"` where `licenseFilePath` is the absolute path to the license file. The following is an example of the command.

```
EmEditor.exe /ol "C:\Users\Example\emeditorLicenseFile-a7PT7Au3TOelfK1w.txt"
```

- You may use `/ola` instead of `/ol` if you need to register EmEditor per computer (administrative permissions are required).

6. Open EmEditor and view [Registration Information](../../dlg/registration_info/index) to confirm that offline registration was successful. The license file can be deleted now as it is no longer needed to use EmEditor.

- You do not need to register with the offline license again after you renew your subscription.

## Technical information

The internal details about offline registration can be viewed [here](https://www.emeditor.com/general/new-validation-system-explained/).