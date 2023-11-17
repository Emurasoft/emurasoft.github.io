# Q. What are three invalid characters at the beginning of my file?

The three characters at the top of your file is the "Byte Order Mark" of a UTF-8 file. By default, a Java file is created as UTF-8 with BOM. You can change the default code page for new files from **Java Properties** \> **File** page > **New Files** button, and change the code page to Normal ANSI, or uncheck the **Add a Unicode Signature** (BOM) box.
