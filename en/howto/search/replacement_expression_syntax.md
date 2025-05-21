# Replacement Expression Syntax

Replacement expressions can be used when using regular expression or number range to replace.

The following expressions are available for the **Replace With** box in
the **Replace** dialog box and in the **Replace in Files** dialog box.

| | |
| --- | --- |
| \\0 | Indicates a back reference to the entire regular expression. |
| \\1 - \\9 | Indicates a back reference - a back reference is a reference to a previous sub-expression that has already been matched. The reference is to what the sub-expression matched, not to the expression itself. A back reference consists of the escape character "\\" followed by a digit "1" to "9", "\\1" refers to the first sub-expression, "\\2" to the second etc. |
| $10, $11, $12, ... | Indicates a back reference more than 9. Equivalent to \\k<10>, \\k<11>, \\k<12>, .... |
| \\k<name> | Indicates a named back reference. A named back reference is a reference to a previously matched named capturing group using this form: (?<name>expression). If "name" is a number, it indicates a numbered back reference, equivalent to \\1, \\2, \\3, ... |
| \\n | A newline character. |
| \\r | A carriage return in case of **Replace in Files**. See also [To Specify newline characters](search_nl). |
| \\t | A tab. |
| \\L | Forces all subsequent substituted characters to be in lowercase. |
| \\U | Forces all subsequent substituted characters to be in uppercase. |
| \\H | Forces all subsequent substituted characters to be in half-width characters. |
| \\F | Forces all subsequent substituted characters to be in full-width characters. |
| \\Nc | Forces all subsequent substituted characters to be converted using [Unicode Normalization Form C (Canonical Composition)](../../cmd/convert/unicode_norm_fc). |
| \\Nd | Forces all subsequent substituted characters to be converted using [Unicode Normalization Form D (Canonical Decomposition)](../../cmd/convert/unicode_norm_fd). |
| \\NC | Forces all subsequent substituted characters to converted using [Unicode Normalization Form KC (Compatibility Composition)](../../cmd/convert/unicode_norm_fkc). |
| \\ND | Forces all subsequent substituted characters to be converted using [Unicode Normalization Form KD (Compatibility Decomposition)](../../cmd/convert/unicode_norm_fkd). |
| \\E | Turns off previous \\L, \\U, \\F, \\H, \\Nc, \\Nd, \\NC, or \\ND. |
| \\J | Specifies that JavaScript is used as the expression. \\J must be placed at the beginning of the replacement expression. Can be combined with back references. The **cell** function can also be used in the script. See {ref}`cell-function-beta`.
| \\V | Same as \\J except that \\V uses the **V8 JavaScript** engine instead of the **Chakra** engine. |
| \\D | If the Date/Time type of a [**Number Range Expression**](number_range_syntax) is used to match a string, this expression specifies a date format. It can be combined with **\\T**. [See available day, month, and year format pictures.](https://docs.microsoft.com/en-us/windows/win32/intl/day--month--year--and-era-format-pictures) See {ref}`date-format-example`
| \\T | If the Date/Time type of a [**Number Range Expression**](number_range_syntax) is used to match a string, this expression specifies a time format. It can be combined with **\\D**. [See available hour, minute, and second format pictures.](https://docs.microsoft.com/en-us/windows/win32/intl/hour--minute--and-second-format-pictures) See {ref}`time-format-example`
| (?Ntrue\_expression:false\_expression) | If sub-expression N was matched, then true\_expression is evaluated and sent to output, otherwise false\_expression is evaluated and sent to output. For example, (?1foo:bar) will replace each match found with foo if the sub-expression \\1 was matched, and with bar otherwise. Alternatively, you can write the expression in this form: (?{1}foo:bar) |
| $(Path) | File path. |
| $(Dir) | File directory. |
| $(Filename) | File name without extension. |
| $(FilenameEx) | File name with extension. |
| $(Ext) | File extension. |
| $(Lines) | Number of lines (cannot be used in **Replace in Files**). |
| $(CsvColumns) | Number of CSV columns (cannot be used in **Replace in Files**). |

(cell-function-beta)=
## cell function (beta)

The **cell** function can be used in JavaScript if **\\J** is also specified. This function retrieves the text in the specified CSV cell.

<table><tbody><tr><th>Replacement Expression</th><th>Meaning</th></tr><tr><td>\J &quot;\0&quot; + &quot;abc&quot;</td><td>joins the matched string and &quot;abc&quot;</td></tr><tr><td>\J &quot;\0&quot;.substr( 0, 5 );</td><td>returns the first 5 characters of the matched string</td></tr><tr><td>\J \0 * 100;</td><td>multiply a matched number with 100</td></tr><tr><td>\J parseFloat( \0 ).toFixed(2);</td><td>rounds a matched number to 2 decimal places</td></tr><tr><td>\J cell( -1 )</td><td>returns the text in the left neighbor cell, relative to the matched cell.</td></tr><tr><td>\J parseFloat( cell( -1 ) ) <br>+ parseFloat( cell( -2 ) ) </td><td>returns the sum of the two neighboring cells on the left</td></tr></tbody></table>

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

(date-format-example)=
## Date format example

If the matched date/time is "2022-03-31 21:30": <table><tbody><tr><th>Replacement Expression</th><th>Result</th></tr><tr><td>\DM/d/yyyy</td><td>3/31/2022</td></tr><tr><!-- cspell:disable-next-line --><td>\DMMMM, d, yyyy</td><td>March 31, 2022</td></tr><tr><td>\D'month='M 'day='d \THH:mm</td><td>month=3 day=31 21:30</td></tr></tbody></table>

(time-format-example)=
## Time format example

If the matched date/time is "2022-03-31 21:30": <table><tbody><tr><th>Replacement Expression</th><th>Result</th></tr><tr><td>\THH:mm</td><td>21:30</td></tr><tr><td>\Th:mm tt</td><td>9:30 PM</td></tr><tr><td>\THH:mm\D-yyyy-MM-dd</td><td>21:30-2022-03-31</td></tr></tbody></table>

## Notes

Many new methods in modern JavaScript/ECMAScript are not available in EmEditor. The Replace Expressions use Chakra (equivalent to Microsoft Edge Legacy), and support up to ECMAScript 5.1, thus newer methods introduced after ECMAScript 5.1 are not supported.

## See Also

- [Regular Expression Syntax](search_regexp_syntax)
