# Q. When reading Macintosh text files, some characters are converted to different characters. How can I read Macintosh text files correctly?

Macintosh uses slightly different code pages than Windows
does. In Windows 2000/XP/2003/Vista, where Macintosh code pages are installed, you can
convert Macintosh text files into Windows text files. First, select the [**File Encodings** page](../../dlg/customize/encodings/index.md) of the **Customize** dialog, press
the **New** button, and select a Macintosh encoding, for example, "10001 (MAC -
Japanese)". Select an appropriate character set, for example, Japanese. Click **OK** to close the dialog box.

Next, select the [**Open** command](../../cmd/file/file_open) under the
**File** menu, select your defined
encoding, for
example, "10001 (MAC - Japanese)" from the **Code Page** combo box, and then select a
Macintosh file that you would like to read.

In Windows 98/Me, where Macintosh code pages are not installed, you cannot
read Macintosh text files correctly if they contain special characters that
cannot be read by Windows code pages.
