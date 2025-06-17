# Supported File Types

EmEditor can open and edit any text files written with Unicode, Unicode big endian, UTF-8, UTF-7,  Baltic, Central European, Chinese Simplified,
Chinese Traditional, Cyrillic, Greek, Japanese (Shift-JIS), Japanese (JIS), Japanese (EUC), Korean, Thai, Turkish,
Vietnamese, Western European, or any other encodings available on Windows.

In Windows 2000/XP/2003/Vista, more encodings are available by checking additional
languages under **Supplemental language support** on the **Languages** page
of **Regional and Language Options** in the Control Panel. You can also check
encoding you want to use under **code page conversion tables** on the **Advanced** page.

Encodings you want to use can be added on the [**File Encodings** page](../../dlg/customize/encodings/index) of the **Customize** dialog box.

Newline Characters can be CRs only, LFs
only, or CR and LF pairs.

## Notes

- You can edit Unicode text files but languages that are written from
right to left such as Arabic and Hebrew may be edited incorrectly. Not all
Unicode control characters are supported.
- You can edit Unicode text files but it depends on the font. Some display
characters are not supported. You need to choose an appropriate font for the
language you wish to use.
- When a file contains [null characters](../../glossary/index), the [null characters](../../glossary/index) will be converted into spaces.
