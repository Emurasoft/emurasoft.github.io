# Q. When I write a Java class with EmEditor and compile it I get an error that states that there are three invalid characters at the beginning of my class. This happens every time and I do not have any characters before the class keyword, which is where the error says they are.

The three characters at the top of your file are the "Byte Order Mark" of a
UTF-8 file. By default, a Java file is created as UTF-8 with BOM. You can change
the default code page for new files from **Java Properties** \> **File**
tab > **New Files**
button, and change the code page to Normal ANSI, or uncheck the **Add a Unicode**
**Signature** (BOM) box.
