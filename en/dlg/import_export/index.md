# Import and Export Wizard

This wizard appears when the [**Import and Export** command](../../cmd/tools/import_export) is selected. You can then select to import settings from a file or to export current settings into a file.

To find more information about each control, such as a check box or a text
box in the wizard, select from the control list below, or press the **F1** key when a control is selected.

### Choose an action to perform list box

You can select an action to perform from the list.

|     |     |
| --- | --- |
| **Export all personal settings into a registry file.** | Export all the personal settings including configurations, menus, Toolbars, External Tools and the recently used file list to a Registration file. You can later use this file to import to restore the current settings, or copy the settings to another computer. |
| **Export all settings to INI files.** | Export all the personal and global settings to INI files. This option is disabled if INI files already exist in the EmEditor install folder. |
| **Import all personal settings from a registry file.** | Read a previously saved file by selecting **Export all personal settings into a file**. You can use this selection to restore previously saved settings. |
| **Set up a removable drive such as a USB drive with default settings.** | Copy EmEditor files and create INI files with default settings to a removable drive. This option is disabled if INI files already exist in the EmEditor install folder. |
| **Set up a removable drive such as a USB drive and export all settings into INI files.** | Copy EmEditor files and create INI files with the current settings to a removable drive. This option is disabled if INI files already exist in the EmEditor install folder. |
| **Import INI files to the Registry.** | Import all personal settings in INI files to the Registry. |

**Notes**

The following INI files will be created when you select one of options to create INI files:

- eeCommon.ini
- eeConfig.ini
- eeLM.ini

When EmEditor starts and finds eeUseIni.ini in its install folder, EmEditor uses these INI files instead of the Registry, and does not save any settings to the Registry.
