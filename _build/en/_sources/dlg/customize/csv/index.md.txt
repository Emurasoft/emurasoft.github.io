# CSV Formats page

The **CSV Formats** page allows you to customize settings related to the CSV formats.

### CSV Formats list box

Displays the list of defined CSV formats. In order to be detected when a file is opened, CSV formats must be checked in the **CSV files to Detect** list box in the
[**File** page](../../properties/file/index) of configuration properties. The priority order of the detection is the order specified in this list box.

### Add button

Adds an item to the list.

### Delete button

Click this button to delete the selected item from the list.

### Up button

Move the selected item up on the list.

### Down button

Move the selected item down on the list.

### Select All button

Select the entire list.

### Toolbar button title check box and text box

Specifies the title separately from the CSV format name.

### Delimiter text box

Specifies a delimiter to separate the data items. The delimiter can include the following escape sequences. The delimiter is a string up to 39 character long.

|     |     |
| --- | --- |
| \\a | Warning (Bell) |
| \\b | Backspace |
| \\t | Horizontal tab |
| \\v | Vertical tab |
| \\\ | Backslash |
| \\xhhhh | Unicode character in hexadecimal notation |

### Quotation Mark text box

Specifies a quotation mark to quote data items. The quotation mark can include the above escape sequences. The quotation mark must be exactly one character.

### Allow delimiters in quotes check box

Specifies whether the delimiters should be allowed in quotes.

### Allow newlines in quotes check box

Specifies whether newline characters should be allowed in quotes.

### Use Escape Character check box

Specifies whether delimiters and backslashes should be escaped by a backslash. This option allows a nonstandard CSV format, which does not allow delimiters in quotes.

### Column headings text box

Specifies the number of lines that are column headings in a CSV document.

### Row headings text box

Specifies the number of columns that are row headings in a CSV document.

### Min lines to detect text box

The number specifies the minimum number of lines to detect as a CSV document. When a file is opened, EmEditor counts the number of delimiters in the number of lines specified here,
and if all lines have the equal number of delimiters, the file is detected as the CSV document. Regardless of this option, the CSV document must be at least two lines. Moreover, CSV formats must be
checked in the **CSV files to Detect** list box in the [**File** page](../../properties/file/index) of configuration properties.

### Max lines to detect text box

The number specifies the maximum number of lines to detect as a CSV document. When a file is opened, EmEditor counts the number of delimiters in the number of lines specified here,
and if all lines have the equal number of delimiters, the file is detected as the CSV document. Regardless of this option, the CSV document must be at least two lines. Moreover, CSV formats must be
checked in the **CSV files to Detect** list box in the [**File** page](../../properties/file/index) of configuration properties.

### Min delimiters to detect text box

The number specifies the minimum number of delimiters to detect as a CSV document. For example, if one line contains only 3 delimiters in a CSV document, if the number in this text
box is 3, this file would be detected as the CSV file. However, if the number in this text box is 4, the file would not be detected as the CSV file. Moreover, CSV formats must be checked in the
**CSV files to Detect** list box in the [**File** page](../../properties/file/index) of configuration properties.

### First line to detect text box

The number specifies the line number of the first line to detect as a CSV document. For example, if the first 3 lines of a document do not contain delimiters, and if the number in this text box is 3, EmEditor would ignore the first 3 lines and detect the rest of the document as the CSV file.

### Max newlines in a cell text box

Specifies the maximum number of newlines that can be embedded in a cell. This option is only available if the **Allow newlines in quotes** option is set.

### Reset button

Resets to default settings.
