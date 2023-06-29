# File page

The **File** tab allows you to set properties related to file
operations.

### Prompt if Null Character Found check box

Show warning message if the file contains
[Null characters](../../../glossary/nullcharacter) when opening
a file. Null characters are converted into spaces when a file is opened. You
must be careful since files containing Null characters may corrupt the
original file.

### Prompt if Invalid Character Found check box

When open a file containing a Unicode character that
cannot be converted into the specified encoding, a warning message will be
displayed: "Some characters cannot be
converted using the specified encoding. The file will be corrupted if you
continue editing and save the file." For
instance, if you try to open a Japanese EUC file with the Japanese Shift-JIS
encoding, and if the file contains a character code value not in the range of
the Japanese Shift JIS encoding, the warning message will be displayed.

**Notice**

Even if this check box is checked, some encodings will not display the
warning message. For instance, trying to open a Japanese Shift-JIS file with the
Japanese EUC encoding will not display the warning message.

### Prompt at Inconsistent Newline Characters check box

Show warning message if the return style in the file is not consistent when
opening a file.

### Except for Binary Files check box

Disables the **Prompt at Inconsistent Newline Characters** option if Binary (ASCII View) is selected for the encoding.

### Show File Name with Full Path check box

Show the file name with the full path on the EmEditor window title.

### Without Full Path if Not Active check box

Will not show the file name with the full path on the EmEditor window title, unless window is active.

### Notepad-Compatible Diary check box

Enable the Notepad-like diary function. If you save with .LOG on the first line, it will automatically insert time and
date at the end of document each time you open the file.

### Detect HTML/XML Charset check box

Find "charset=..." from HTML files, "encoding=..." from XML files, or "#coding=..." from Python and Ruby files, and use the corresponding encoding. If you open HTML, XML, Python, or Ruby files, check only this option and clear the other options.

### Detect All check box

Statistically
detect code page from all available code pages. The detection can make mistakes especially when the file is very small. This option does not include HTML/XML charset detection.

### Detect Unicode Signature (BOM) check box

Detect whether the file contains a Byte Order Mark (BOM) signature, and if it detects
the BOM signature, EmEditor will open the file as UTF-16LE, UTF-16BE, or UTF-8 file.

### Detect UTF-8 check box

Statistically detect UTF-8.

### Prefer UTF-8 check box

When this is checked and the Detect UTF-8 check box is also checked, UTF-8 takes precedence if the file can be interpreted both as UTF-8 and the selected encoding. For example, a
file contains only ANSI characters (alphabets and numbers), it can be opened without any problems both as UTF-8 and Western European. In this situation, EmEditor opens the file as UTF-8. EmEditor also
opens an empty file as UTF-8 if this is checked.

### CSV files to Detect list box

CSV formats checker here are detected when EmEditor opens a file. CSV formats can be defined in the [**CSV** page](../../customize/csv/index) of the **Customize** dialog box.

In order to be detected, the CSV file must be at least two lines long, and the same number of delimiters must be used at each line of the file.

### Opening Encoding drop-down list box

Select the encoding to open.

### Changed by Another Program drop-down list box

Select what to do if the file you are editing is changed by another program.

|     |     |
| --- | --- |
| Ignore | Does not reload the file even if the file is modified by another <br> program. This option does not change the read-only status of EmEditor <br> even if the read-only attribute of the file is changed. |
| Prompt | Displays a message box to ask whether it is OK to reload the file. <br> This option allows changes to the read-only status of EmEditor when <br> the read-only attribute of the file is changed. |
| Auto-Reload | Always reloads the file unless it has been modified. This option <br> allows changes to the read-only status of EmEditor when the read-only <br> attribute of the file is changed. |
| Keep Locked | Exclusively opens the file with EmEditor and prohibits another <br> program to write the file while the file is open. This option  <br> allows changes to the read-only status of EmEditor when the read-only <br> attribute of the file is changed. |

### Default Extension text box

If you save a file as a different name, with **All Files (\*.\*)** selected in
the **File Type** combo box, and do not specify the file extension, the
file extension will be the one you selected in this text box.

### Monitor Interval text box

Specifies the time interval in seconds to monitor file changes. This text box is enabled only when an item except **Ignore** is selected in the **Changed**
**by Another Program** drop-down list box.

### New Files button

Click this button to display the [**New File**\
**Details** dialog box](new_details/index), which allows you to configure the encodings and other
settings when you create a new file.

### Saving button

Click this button to display the [**Save**\
**Details** dialog box](save_details/index), which allows you to configure the encodings and other
settings when you save files.

### Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed
and will allow you to copy from another configuration.

You can also move to the following dialog box from this page.

(Select **New Files**
button)

(Select **Savings**
button)

```{toctree}
:maxdepth: 1
new_details/index
save_details/index
```
