# MemorySize Property

Retrieves or sets the maximum memory size per large chunk for the document. The default value can be specified in theMemory Size text box in the [Advanced page](../../dlg/customize/advanced/index) of theCustomize dialog box. The property getter (n = document.MemorySize) always succeeds, however the setter (document.MemorySize = n) may throw an exception if the document is already using a higher memory size than the specified size.

## 

### \[JavaScript\]

```
n = document.MemorySize;
document.MemorySize = n;
```

### \[VBScript\]

```
n = document.MemorySize
document.MemorySize = n
```

## Version

Supported on EmEditor Professional Version 17.8 or later.
