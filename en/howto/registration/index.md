# Installation and Registration Guide

EmEditor can be installed and registered in several ways. Choose the method that matches your environment, and follow the steps in that section.

| Method | Deployment type | Updates | Intended for |
|---|---|---|---|
| Microsoft Store | Per user | Automatic | Quick set up |
| Per-user installer | Per user | Automatic | Power users |
| Per-machine installer | Per machine | Manual | IT admins |

## Microsoft Store (per-user)

This is the easiest way to start using EmEditor, and we recommend it for individual users.

1. Open the [EmEditor page in the Microsoft Store](https://apps.microsoft.com/detail/9nblggh537df) and install it.
2. Use the free trial. When it ends, EmEditor will take you to the Microsoft Store where you can buy a subscription.

- EmEditor updates automatically when a new version is available.

## Per-user installation

This method installs EmEditor for the current Windows user only. It is intended for individual users who prefer to download directly from Emurasoft.

1. Download `emeditor64.appinstaller` from the [Download page](https://www.emeditor.com/download/).
2. Run `emeditor64.appinstaller` to install EmEditor for the current user.
3. [Purchase an EmEditor subscription](https://www.emeditor.com/buy/).
4. In EmEditor, select **Help** > **Registration Information**, and click **Sign In/Enter Registration Key**.
5. In the **Register Product** dialog, do one of the following.
   - Select **Enter registration key**, and enter the key sent to you by email.
   - Select **Sign in**, and sign in with your Emurasoft Customer Center credentials.

Notes

- EmEditor updates automatically when a new version is available.
- To unregister the license, use **Help** > **Registration Information**.

## Per-machine installation

This method installs EmEditor for the whole machine, making it available to every user on the same Windows system. The license is registered per machine, so that only one registration is necessary for one machine.

1. Download the latest `.msix` installer from the **Other download options** section of the [Download page](https://www.emeditor.com/download/). You can also get the latest installer from the [Emurasoft Customer Center](https://support.emeditor.com/en/account/downloads).
2. In **PowerShell with administrator rights**, run the following command to provision the package for all users.

```powershell
Add-AppxProvisionedPackage -PackagePath path\to\emed64_x.x.x.msix -Online -SkipLicense
```

3. Register the license for the machine by running the following command. The previous step would have made `emeditor.exe` available in `PATH`. When the User Account Control (UAC) prompt appears, confirm it so that EmEditor can write the registration data to `HKEY_LOCAL_MACHINE\SOFTWARE\EmSoft\EmEditor v3\Common`.

```powershell
emeditor /register /regname "Your Name" /regemail "example@example.com" /regkey "Registration Key" /reglabel "Device label"
```

Notes

- When a user signs in to Windows, EmEditor is provisioned for that user automatically. User settings are stored in the user's own registry entries.
- When the user launches EmEditor, it reads the registration data from the machine-wide registry entries, so no per-user registration is required.
- Per-machine installations do not update automatically. To update, repeat step 2 with the newer `.msix` installer.
- To unregister the license, use `emeditor /unregister`.