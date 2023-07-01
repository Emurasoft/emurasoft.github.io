# Extract Frequent Strings dialog box

This dialog box appears when the
[**Extract Frequent Strings** command](../../cmd/search/extract_frequent) is selected. It creates a list of frequently used strings as a CSV document.

### Whole Lines radio button

Creates a list of frequent lines.

### Words radio button

Creates a list of frequent words. A word is a string surrounded by non-alphanumeric characters, which can be customized by the **Treat the following characters as alphanumeric** text box in the [**Edit** page](../customize/edit/index) of the **Customize** dialog box.

### Cells radio button

Creates a list of frequent cells.

### IPv4 Addresses radio button

Creates a list of frequent IPv4 addresses.

### IPv6 Addresses radio button

Creates a list of frequent IPv6 addresses.

### Match Case check box

Match cases while counting frequent strings.

### Search All Documents in the Group check box

Searches all open documents in the same frame window.

### In the Selection Only check box

Extract frequent strings within the selected text only.

### Number of Lines text box

Specifies the maximum number of strings to be extracted. The actual output may exceed this number in order to include all multiple strings detected for the same frequency.

### CSV Format drop-down list box

Specifies the CSV format to display as.

### Strings to Ignore list box

Displays the list of strings to be ignored while counting frequent strings.

### Add button

Adds an item to the list.

### Delete button

Deletes the selected item(s) from the list.

## Tips

To count and extract strings matching a specific pattern, set the **Count Frequent Strings** check box in the [**Extract Options** dialog box](../extract_options/index), use a regular expression to match specific strings, and use the **Extract** button in the [**Find** dialog box](../find/index).

