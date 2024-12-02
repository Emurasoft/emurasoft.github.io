# File Verification Results Dialog Box

The **File Verification Results** dialog box provides information about the outcome of the file verification process. This dialog appears when you choose the **Verify** command.

In the **File Verification Results** dialog box, you'll find the following details:

1. Whether the two files match after verification.
2. The path, size, and SHA256 hash of the original file.
3. The path, size, and SHA256 hash of the temporary file.

If the files don't match, it could be due to several reasons:

- The original file might have been altered after being opened.
- The original file might contain NULL or invalid characters that can't be converted to Unicode.
- The original file might include characters that don't directly map to Unicode in the specified encoding. For instance, in Shift-JIS encoding, some characters are redundantly listed as both "IBM extended characters" and "NEC selected IBM extended characters." Thus, if a character with the code 0xFA58, an IBM extended character "㈱", is in a Shift-JIS file, its Unicode character code becomes U+3231 when opened in EmEditor. Moreover, if saved in Shift-JIS, it is stored as the same character with the code 0x878A, a "NEC selected IBM extended character."
- The file might have been opened using the **Open Advanced** command with options like **Insert line breaks every specified number of bytes** or **Ensure that a newline code exists at the end of each file**.

## Delete Temporary Files check box

When checked, this option will delete the saved temporary file.
