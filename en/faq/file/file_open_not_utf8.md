# Q. How can I open an XML file as Western European, not as UTF-8?

If an XML file is opened as Unicode, display the **Current Configuration**
**Properties**, select
the [**File** page](../../dlg/properties/file/index), and check **Opening**
**Encoding** drop-down list box. If this is **Unicode**, select **System Default**. If
**Detect**
**HTML/XML Charset** check box is checked, an "encoding=" directive specified within
an XML file is searched, and EmEditor uses the specified encoding if the
directive is found. Note that the encoding specified for opening files is
different from the encoding specified for new files or for saving files.

## See Also
