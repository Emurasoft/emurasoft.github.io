# Replacement Expression Syntax

Replacement expressions can be used when using regular expression or number range to replace.

The following expressions are available for the **Replace With** box in
the **Replace** dialog box and in the **Replace in Files** dialog box.

| \\0 | Indicates a back reference to the entire regular expression. |
| \\1 - \\9 | Indicates a back reference - a back reference is a reference to a <br> previous sub-expression that has already been matched. The reference is <br> to what the sub-expression matched, not to the expression itself. A back <br> reference consists of the escape character "\\" followed by a digit "1" <br> to "9", "\\1" refers to the first sub-expression, "\\2" to the second etc. |
| $10, $11, $12, ... | Indicates a back reference more than 9. Equivalent to \\k<10>, \\k<11>, \\k<12>, .... |
| \\k<name> | Indicates a named back reference. A named back reference is a reference to a previously matched named capturing group using this form: (?<name>expression). If "name" is a number, it indicates a numbered back reference, equivalent to \\1, \\2, \\3, ... |
| \\n | A newline character. |
| \\r | A carriage return in case of **Replace in Files**. See also [To Specify newline characters](search_nl). |
| \\t | A tab. |
| \\L | Forces all subsequent substituted characters to be in lowercase. |
| \\U | Forces all subsequent substituted characters to be in uppercase. |
| \\H | Forces all subsequent substituted characters to be in half-width <br> characters. |
| \\F | Forces all subsequent substituted characters to be in full-width <br> characters. |
| \\Nc | Forces all subsequent substituted characters to be converted using [Unicode Normalization Form C (Canonical Composition)](../../cmd/convert/unicode_norm_fc). |
| \\Nd | Forces all subsequent substituted characters to be converted using [Unicode Normalization Form D (Canonical Decomposition)](../../cmd/convert/unicode_norm_fd). |
| \\NC | Forces all subsequent substituted characters to converted using [Unicode Normalization Form KC (Compatibility Composition)](../../cmd/convert/unicode_norm_fkc). |
| \\ND | Forces all subsequent substituted characters to be converted using [Unicode Normalization Form KD (Compatibility Decomposition)](../../cmd/convert/unicode_norm_fkd). |
| \\E | Turns off previous \\L, \\U, \\F, \\H, \\Nc, \\Nd, \\NC, or \\ND. |
| \\J | Specifies that JavaScript is used as the expression. \\J must be placed at the beginning of the replacement expression. Can be combined with back references. The **cell** function can also be used in the script. For instance,

| Replacement Expression | Meaning |
| --- | --- |
| \\J "\\0" + "abc" | joins the matched string and "abc" |
| \\J "\\0".substr( 0, 5 ); | returns the first 5 characters of the matched string |
| \\J \\0 \* 100; | multiply a matched number with 100 |
| \\J parseFloat( \\0 ).toFixed(2); | rounds a matched number to 2 decimal places |
| \\J cell( -1 ) | returns the text in the left neighbor cell, relative to the matched cell. |
| \\J parseFloat( cell( -1 ) ) + parseFloat( cell( -2 ) ) | returns the sum of the two neighboring cells on the left | |
| \\V | Same as \\J except that \\V uses the **V8 JavaScript** engine instead of the **Chakra** engine. |
| \\D | If the Date/Time type of a [**Number Range Expression**](number_range_syntax) is used to match a string, this expression specifies a date format. It can be combined with **\\T**. [See available day, month, and year format pictures.](https://docs.microsoft.com/en-us/windows/win32/intl/day--month--year--and-era-format-pictures) For instance, if the matched date/time is "2022-03-31 21:30":

| Replacement Expression | Result |
| --- | --- |
| \\DM/d/yyyy | 3/31/2022 |
| \\DMMMM, d, yyyy | March 31, 2022 |
| \\D'month='M 'day='d \\THH:mm | month=3 day=31 21:30 | |
| \\T | If the Date/Time type of a [**Number Range Expression**](number_range_syntax) is used to match a string, this expression specifies a time format. It can be combined with **\\D**. [See available hour, minute, and second format pictures.](https://docs.microsoft.com/en-us/windows/win32/intl/hour--minute--and-second-format-pictures) For instance, if the matched date/time is  "2022-03-31 21:30":

| Replacement Expression | Result |
| --- | --- |
| \\THH:mm | 21:30 |
| \\Th:mm tt | 9:30 PM |
| \\THH:mm\\D-yyyy-MM-dd | 21:30-2022-03-31 | |
| (?Ntrue\_expression:false\_expression) | If sub-expression N was matched, then true\_expression is evaluated and sent to output, otherwise false\_expression is evaluated and sent to output. For example, (?1foo:bar) will replace each match found with foo if the sub-expression \\1 was matched, and with bar otherwise. Alternatively, you can write the expression in this form: (?{1}foo:bar) |
| $(Path) | File path. |
| $(Dir) | File directory. |
| $(Filename) | File name without extension. |
| $(FilenameEx) | File name with extension. |
| $(Ext) | File extension. |
| $(Lines) | Number of lines (cannot be used in **Replace in Files**). |
| $(CsvColumns) | Number of CSV columns (cannot be used in **Replace in Files**). |

## cell function (beta)

The **cell** function can be used in JavaScript if **\\J** is also specified. This function retrieves the text in the specified CSV cell.

### 

#### \[JavaScript\]

```
str =cell( iColumn [, yLine [, flags ] ] );
```

### Parameters

_iColumn_

Specifies the index of the column of the text you want to retrieve, expressed in the relative position from the current position unless 8 is specified in _flags_.

_yLine_

Specifies the line number of the text to retrieve, expressed in the relative position from the current position unless 8 is specified in _flags_. If omitted, 0 is specified.

_flags_

Specifies a combination of the following values. 0, 1, and 2 cannot be used together. If omitted, 1 is specified.

|     |     |
| --- | --- |
| 0 | The returned text may not include surrounded double-quotes or delimiters. |
| 1 | The returned text may include surrounded double-quotes but no delimiters. |
| 2 | The returned text may include surrounded double-quotes and delimiters. |
| 8 | _iColumn_ and _yLine_ parameters are expressed in 1-based absolute values. |

## Notes

Many new methods in modern JavaScript/ECMAScript are not available in EmEditor. The Replace Expressions use Chakra (equivalent to Microsoft Edge Legacy), and support up to ECMAScript 5.1, thus newer methods introduced after ECMAScript 5.1 are not supported.

## See Also

- [Regular Expression Syntax](search_regexp_syntax)
