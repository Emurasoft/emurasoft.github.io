# Advanced dialog box

This dialog box appears when the **Advanced** button is selected in the [**Find** dialog box](../find/index), [**Replace** dialog box](../replace/index), [**Find in Files** dialog box](../find_in_files/index) or the [**Replace in Files** dialog box](../replace_in_files/index).

## Match Only Embedded Newlines in CSV check box

If this box is checked, EmEditor matches only embedded newlines in CSV documents.

## Treat CR and LF Separately check box

If this box is checked, EmEditor will treat CR and LF separately. In case Find in Files and Replace in Files, EmEditor will treat CR and LF separately if the Use Regular Expressions is checked regardless of this option.

## Regular Expressions “.” Can Match Newline Characters check box

Specifies whether a period can match newline characters when searching for a string using a regular expression. A regular expression \\s can match newline characters when a number greater than zero is specified in the **Additional Lines to Search for Regular Expressions** text box even if this is not checked. Except for the [**Find in Files** command](../../cmd/search/grep), the actual number of lines that can be matched depends on the number specified in the **Additional Lines to Search for Regular Expressions** text box.

## Regular Expression Engine drop-down list box

Specifies the regular expression engine to use in **Find**, **Replace**, **Find in Files**, and **Replace in Files**. You can choose **Boost.Regex** or **Onigmo**.

The following option only appears in the **Find** dialog box and **Replace** dialog box.

## '^' and '$' can Match Beginning and End of the Selection check box

Allows you to use regular expressions that can match only at the beginning or ending of the selection. This option is valid only if the **In the Selection Only** option is enabled in the **Find** or **Replace** dialog box.

## Look Around during the Selection Only Search check box

Allows you to use lookahead/lookbehind expressions to look outside of the selection while matching only in the selection. For instance, "(?\<=a)b" will match "b" even if the selection begins at "b" in the line containing "ab". However, Enabling this option can slow down the search process because EmEditor will search the whole line including the selection. Moreover, this option can prevent a legitimate regular expression from matching the selection. For instance, ".\*" can't match any strings in the selection if the selection doesn't cover the whole line and if this option is enabled because EmEditor matches the whole line but the selection is only a portion of the line. This option is valid only if the **In the Selection Only** option is enabled in the **Find** or **Replace** dialog box.

## Find Next/Previous matches non-overlapping strings only check box

Does not match overlapping strings when finding a next or previous match.

## Additional Lines to Search for Regular Expressions text box

Specifies the number of additional lines to search for a string when using a regular expression. EmEditor passes a string line by line as a parameter to the regular expression function. By this method, however, the regular expression \<td\>.\*?\</td\> would not be able to match a string between \<td\> and \</td\> if the string contains a newline character. Specifying a number greater than zero in this text box and checking the **Regular Expressions “.” Can Match Newline Characters** check box will enable searching for the string with up to the specified number of new lines. On the other hand, the [**Find in Files** command](../../cmd/search/grep) always searches from the whole file independent of this option.

The following options only appear in the **Find in Files** dialog box and **Replace in Files** dialog box.

## Ignore Following Files or Folders check box

If this box is checked, EmEditor will not search for file or folder names
specified in the **Files or Folders to Ignore**
text box.

## Files or Folders to Ignore text box

Specifies the names of files or folders to ignore. To specify multiple names,
separate them with a semicolon (**;**).

## Ignore Binary Files check box

If this box is checked, EmEditor will not search binary files (files that contain NULL characters even though they are not UTF-16 files).

## Show Ignored Files in Results check box

If this box is checked, EmEditor will not show ignored files in the output when the **Ignore Following files or folders** check box or the **Ignore Binary Files** check box is checked.

## Prompt if the specified folder does not exist check box

Checks whether the folder specified in the **In Folder** drop-down list box, and if it doesn't exist, displays a dialog box so that a user can cancel the operation.

## Append encoding names to file names check box

If this box is checked, EmEditor will append encoding names to file names in the Find in Files results. This option is useful when the **Detect All** option is set in the [**File** page](../properties/file/index) of configuration properties, and when you want to check the encodings of searched files.

## Oldest date modified date box

Specifies the oldest date modified to search files if this check box is set.

## Newest date modified date box

Specifies the newest date modified to search files if this check box is set. If only the **Oldest date modified** is set, EmEditor searches files newer than the specified date. If only the **Newest date modified** is set, EmEditor searches files older than the specified date. If neither of them is set, EmEditor searches all files regardless of file dates.

