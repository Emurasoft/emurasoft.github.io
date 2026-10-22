# Installation and Registration guideline

## Per-user Microsoft Store download

This is the easiest way to get EmEditor, and it is recommended for individual users.

1. Download EmEditor from the [Microsoft Store](https://apps.microsoft.com/detail/9nblggh537df).
2. After the free trial, EmEditor will direct you to the Microsoft Store to purchase a subscription.

## Per-user installation and registration

This method downloads the app directly from us and is intended for individual users.

1. Download `emeditor64.appinstaller` from the [Download page](https://www.emeditor.com/download/).
2. Run the downloaded `emeditor64.appinstaller` to install per-user.
3. [Purchase an EmEditor subscription](https://www.emeditor.com/buy/).
4. In EmEditor, go to **Help** > **Registration Information**. Click **Sign In/Enter Registration Key**.
5. In **Register Product**, you can **Enter registration key** which is provided via email or **Sign in** with your Emurasoft Customer Center credentials.

- EmEditor will automatically update when a new update is available.
- You can unregister the license from **Registration Information**.

## Per-machine installation and registration

This method installs EmEditor per-machine to make it available to all users on the same Windows system. EmEditor is registered per-machine so that all users can use the same license. This method is intended for IT admins.

1. Download the newest `.msix` installer from the [Download page](https://www.emeditor.com/download/) in the **Other download options** section.
  - Alternatively, you can also find the latest installer from [Emurasoft Customer Center](https://support.emeditor.com/en/account/downloads).
2. Run the following command in **PowerShell with Administrator rights** to install per-machine.

```none
Add-AppxProvisionedPackage -PackagePath path\to\emed64_x.x.x.msix -Online -SkipLicense
```

3. Run the following command to register per-machine. The previous command should have put `emeditor.exe` in `PATH` so that it can be called from the command line. Confirm the User Account Control prompt to allow EmEditor to write registry entries to `HKEY_LOCAL_MACHINE\SOFTWARE\EmSoft\EmEditor v3\Common`.

```none
emeditor /register /regname "Your Name" /regkey "Registration Key" /reglabel "Device label" /regemail "example@example.com"
```

- When a user signs into their Windows user, EmEditor will automatically be provisioned to that user and will be available to use. Their settings will be saved to individual registry entries.
- When the user opens EmEditor, it will read the registration data from the machine-wide registry entries, allowing the app to be used.
- EmEditor must be manually installed using the `.msix` every time you would like to update it. 