# Q. When I open a file using the default settings, it becomes unreadable, and if I choose another character set from the Font Category sub menu under the View menu, it becomes worse. But if I select a proper encoding when I open the file, it works. Why?

EmEditor's internal processing is Unicode. EmEditor
converts ANSI text to Unicode text when you open an ANSI file. When opening a
file, you should select an encoding in
the **Open dialog** box. If you don't select an encoding, EmEditor defaults
the file to the
[system default encoding](../../glossary/systemdefaultencoding).
In order to open a file with a different encoding, you need to select the
desired encoding when you open the file. You can later change the encoding by
choosing the [**Reload** \
command](../../cmd/file/file_reload_defined) under the **File** menu and selecting a different encoding option.
