# Outline page

The **Outline** page allows you to set properties related to Outline.

## Display Outline as guide check box

If this is checked, EmEditor displays the outlining as a guide on the left side of the editor. This check box is enabled only if the **Toggle Outline Guide per configuration**
check box is checked in the [**Outline** page](../../customize/outline/index) of the Customize dialog box.

## Display Outline as custom bar check box

If this is checked, EmEditor displays the outlining in a custom bar. This check box is enabled only if the **Toggle Outline Bar per configuration** check box is checked in the
[**Outline** page](../../customize/outline/index) of the Customize dialog box.

## Max level drop-down list box

Specifies the maximum outlining level to be displayed.

## Initially drop-down list box

Specifies whether outlining should be expanded, collapsed, or expanded/collapsed to the specified level when a file is first opened.

## Type drop-down list box

Determines how outlining is calculated. Select one from the following:

|     |     |
| --- | --- |
| **Number of Braces {}** | Outlining is calculated by number of braces. This may be useful for many programming languages. |
| **Number of Spaces** | Outlining is calculated by number of spaces or tabs at the beginning of each line. This may be useful for general purposes. |
| **Custom** | Outlining is calculated according to the specified settings in the **Find** list box. If this is selected, click the **Add** button next to the **Find** <br> list box to add more than one item to the list. |
| **Number of Brackets \[\]** | Outlining is calculated by number of brackets. This may be useful for some programming languages. |
| **Custom (Specify Begin as Level 1/End as Level 2)** | Outlining is calculated according to the specified settings in the **Find** list box. If this is selected, click the **Add** button next to the **Find** <br> list box to add two items to the list. The first item in the **Find** list box is set as the begin string, and the second item as the end string. The XML configuration uses this as default. |
| **Number of Tabs** | Outlining is calculated by number of tabs at the beginning of each line. This may be useful for general purposes. |

## Make comments collapsible check box

Specifies whether comments should be collapsible.

## Hide matched strings/replace with regular expressions check box

Specifies whether matched strings should be hidden in the custom bar. If the **Regular Expression** check box is checked, this option specifies whether matched strings should be replaced with strings specified at the **Replace with**.

## Find drop-down list box

If the **Regular Expression** is unchecked, enter character(s) that a line should begin with. For instance, enter "." to match only the lines beginning with ".". If the "Regular Expression" is checked, enter a regular expression that should match
for the specified level. For instance, enter "^\\d.\*?$" to match only the lines beginning with a number.

## Regular Expression check box

Specifies whether the string entered in the **Find** text box is treated as a regular expression.

## Replace with text box

Specifies a string to replace with when the **Hide matched strings/replace with regular expressions** check box is checked.

## Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed
and will allow you to copy from another configuration.

