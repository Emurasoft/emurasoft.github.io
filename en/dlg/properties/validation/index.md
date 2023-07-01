# Syntax Check page

The **Syntax Check** page allows you to set properties related to Syntax Check.

### Enable Syntax Check check box

If this is checked, syntax check errors are displayed with red wiggly underlines (customizable), and hovering the mouse pointer causes a tooltip show information about the errors.

### Document Type drop-down list box

Specifies the document type to check syntax. Notes that syntax check will be enabled only while a CSV mode is selected if **CSV** is selected. If the **Language Server Protocol** is selected, the **Document Type** specified in the [**Language Server** page](../language_server/index) is used.

### Show List drop-down list box

|     |     |
| --- | --- |
| (None) | Syntax check results will not be displayed as a list. Even if results are not displayed as a list, syntax check errors will be displayed with red wiggly underlines if the **Enable Syntax Check** check box is set. |
| When a Document is Opened | Syntax check results will be displayed as a list when a document of this configuration is opened. |
| Only when Errors are Detected | Syntax check results will be displayed as a list only if errors are detected when a document of this configuration is opened. |

### Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed
and will allow you to copy from another configuration.

