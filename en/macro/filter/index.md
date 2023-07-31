# Filter Object

## Properties

|     |     |
| --- | --- |
| [Enabled](enabled) | Specifies the flag indicating whether the object is enabled. |
| [Value](value) | Specifies a string to search for. |
| [Column](column) | Specifies the one-based index of the column of the text you want to search, 0 if you want to search for whole lines, or -1 if you want to specify the beginning and end of the text in characters as the _Begin_ and _End_ properties. |
| [Flags](flags) | Specifies a combination of flags. |
| [Begin](begin) | Specifies the index of beginning of the column (in logical characters) of the text you want to search, or 0 if you want to <br> count the last portion of the text and specify as _End_. The _Column_ property must be -1 to enable this field. |
| [End](end) | Specifies the index of end of the column (in logical characters) of the text you want to search, or 0 if you want to search <br> all the rest of the text. The _Column_ property must be -1 to enable this field. |
| [ExFlags](exflags) | Specifies a combination of flags. |
| [Replace](replace) | Specifies a string to replace with. |

## Version

Supported on EmEditor Professional Version 16.0 or later.


```{toctree}
:hidden:
:maxdepth: 1
begin
column
enabled
end
exflags
flags
replace
value
```
