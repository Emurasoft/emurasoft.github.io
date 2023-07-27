# Flags Property (KeyboardItem Object)

Specifies the flags of the object.

## 

### \[JavaScript\]

```
n = item.Flags;
item.Flags = n;
```

### \[VBScript\]

```
n = item.Flags
item.Flags = n
```

## Parameters

_n_

Select a combination of the following values.

|     |     |
| --- | --- |
| eeVirtualKey | Specifies the Key member of the object is a virtual-key code. If this flag is not specified, the Key member of the object is assumed to specify a character code. |
| eeShift | Specifies the SHIFT key must be held down when the accelerator key is pressed. |
| eeCtrl | Specifies the CTRL key must be held down when the accelerator key is pressed. |
| eeAlt | Specifies the ALT key must be held down when the accelerator key is pressed. |

## Version

Supported on EmEditor Professional Version 7.00 or later.
