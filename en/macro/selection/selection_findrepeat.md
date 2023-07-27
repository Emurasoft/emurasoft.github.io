# FindRepeat Method (Selection Object)

Repeats the previous search for the same string.

## 

### \[JavaScript\]

```
document.selection.FindRepeat( nFlags );
```

### \[VBScript\]

```
document.selection.FindRepeat nFlags
```

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeFindRepeatNext | Searches downward from the cursor position. |
| eeFindRepeatPrevious | Searches upward from the cursor position. |
| eeFindRepeatWord | Searches for the word at the cursor position if the selection is empty. |

## Version

Supported on EmEditor Professional Version 4.00 or later.
