# File page

The **File** page allows you to customize settings related to file
operations.

## Remember Last Folder check box

In the **Open** and **Save As** dialogs, show the most recently used folder.

## Prompt when Opening a New File check box

Shows a warning message if trying to open non-existent files.

## Prompt when creating a new file in a network path check box

Shows an additional warning message if trying to open non-existent files in a network path.

## Always Add to Recent Documents Folder check box

Save the shortcuts to the Windows **My Recent Documents** folder when you
open or save files. This check box must be on in order for the recent category in the Windows 7 jump list to include the recently used items.

## Use uchardet to detect file encodings when the Detect All option is set check box

When the **Detect All** option is used to open files, EmEditor will use **[uchardet](https://github.com/BYVoid/uchardet)** (C++ fork of Mozilla Charset Detectors) to detect file encoding.

## Open US-ASCII as System Default Encoding check box

If the detected file encoding was US-ASCII, EmEditor will open the file as the system default encoding.

## Always Show Detect All Result check box

Always displays the
[**Detect All Result** dialog box](../../detect_result/index) when the **Detect**
**All** check box is selected when opening a file, or when the **[Reload Detect All](../../../cmd/file/file_reload_detect_all)** command is selected. However, if UTF-16 with
signature, UTF-16 without signature or UTF-8 with signature is detected, the file will be loaded immediately without displaying the dialog box.

## Show only when Multiple Encodings Detected check box

Displays the
[**Detect All Result** dialog box](../../detect_result/index) only if multiple encodings are detected when the **Detect**
**All** check box is selected when opening a file, or when the **[Reload Detect All](../../../cmd/file/file_reload_detect_all)** command is selected.

## Show Detect All Result also during Find in Files check box

Displays the
[**Detect All Result** dialog box](../../detect_result/index) during Find in Files when the **Detect**
**All** check box is selected.

## Avoid Printer Access check box

Avoids access to a printer. If this is checked, when EmEditor is launched, even if the
**Show Page Numbers** check box is checked, page numbers will not be displayed until the
[**Print** command](../../../cmd/file/file_print) or the [**Print Preview** command](../../../cmd/file/print_preview) is selected. This option is recommended if the printer access is slow.

## Displays Large File Controller when a large file is opened check box

If this is checked, EmEditor automatically displays the Large File Controller when it opens a large file (larger than the size specified in Minimum File Size to Open Asynchronously text box in the
[Advanced page](../advanced/index) of the Customize dialog box).

## Prompt when only a specified portion of file is opened check box

If this is checked, EmEditor will display a prompt dialog box if EmEditor loads only a portion of a file specified in the **From (default)** and **To (default)** text boxes.

## Prompt when default Open Filter exists check box

If this is checked, EmEditor will display a prompt dialog box if the **Open Filter** exists. The **Open Filter** can be set in the **Large File Controller**.

## Prompt if a Unicode (UTF-16) file size is an odd number in bytes check box

If this is checked, EmEditor will display a prompt dialog box if a Unicode (UTF-16) file size is an odd number in bytes.

## Enable file mapping when saving a large file check box

If this is checked, EmEditor will enable file mapping when saving a very large file if possible.

## Monitor files only while EmEditor is active check box

If this is checked, EmEditor will monitor files only while EmEditor is active.

## From (default)

Specifies the place where EmEditor starts loading a file. By default, 0 is specified.

## To (default)

Specifies the place where EmEditor ends loading a file. A blank means unlimited. By default, unlimited is specified.

## Custom File Filter text box

Set the custom file filter shown in the **File Type** combo box in the **Open**
dialog box and the **Save As** dialog box.

## Maximum bytes to detect UTF-8 text box

Set the maximum bytes to detect UTF-8 files.

## File access timeout text box

Set the timeout period in seconds when accessing files. This option becomes important especially when accessing slow storage media or network folders.

## Associate with EmEditor button

Displays the [**Associate with EmEditor** dialog box](../../file_associate/index),
where the user can specify which file extensions to associate with EmEditor.

## Reset button

Resets to default settings.

The following dialog box is also available through this dialog box.

<a href="../../file_associate/index.htm"><b>Associate with EmEditor </b>dialog box</a> (Select **Associate with EmEditor** button)

