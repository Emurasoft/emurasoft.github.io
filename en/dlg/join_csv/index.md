# Join CSV dialog box

This dialog box appears when the
[**Join CSV** command](../../cmd/edit/join_csv) or the Join CSV button is selected in a toolbar.

### CSV Document 1 drop-down list box

Selects the first document.

### CSV Document 2 drop-down list box

Selects the second document. The two CSV documents will be merged by matching the key columns, unless Simply Merge is toggled.

### Key1/Key2 Column drop-down list box

Selects the key column.

### Unique Key check box

If each line in the key column contains a unique value, this option reduces the speed of the Join operation.

### Include all non-matching rows check box

Include all non-matching rows when merged. This is equivalent to OUTER JOIN in SQL if both check boxes are checked, LEFT JOIN if only the left check box is checked, RIGHT JOIN if
only the right check box is checked, and INNER JOIN if neither are checked.

### Ignore Headings check box

If this is checked, headings in the key column are ignored, so that original headings are retained in the merged document.

### Conditions drop-down list box

Specifies a condition.

### Match Case check box

If this is checked, column comparisons are case sensitive.

### Separator text box

If _Both split strings match_, _Key1 matches split Key2_, or _Key2 matches split Key1_ is selected for Conditions, enter the separator to split strings.

### Limit splits check box and text box

Specifies the maximum number of limits.

### CSV Document/Column list box

This shows a list of all columns in both documents. The selected columns are included in the output, in this order.

### Enable/Disable All check box

This check box enables or disables all items in the list.

### Up button

Moves the selected item(s) up on the list.

### Down button

Moves the selected item(s) down on the list.

### Top button

Moves the selected item(s) to the top of the list.

### Bottom button

Moves the selected item(s) to the bottom of the list.

### Combine with previous column check box

This check box allows you to combine the current column with previous column.

### Concatenate radio button

If this button is checked, EmEditor concatenates the current column with the previous column.

### Use first non-empty value radio button

If this button is checked, EmEditor uses the first non-empty value to combine the current column with the previous column.

### Export button

Exports the current settings into a JavaScript or VBScript macro file. The exported macro file can be used to run the same operation.

### Join Now button

Merges the documents.

