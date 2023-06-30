#### [Editor Home](https://www.emeditor.com/) - [EmEditor Help](../../index) \- [EmEditor Macro Reference](../index) \- [Document Object](index) (Document Object)

# MemorySize Property

Retrieves or sets the maximum memory size per large chunk for the document. The default value can be specified in the **Memory Size** text box in the [**Advanced** page](../../dlg/customize/advanced/index) of the **Customize** dialog box. The property getter (n = document.MemorySize) always succeeds, however the setter (document.MemorySize = n) may throw an exception if the document is already using a higher memory size than the specified size.

#### \[JavaScript\]

_n_ = document. **MemorySize**;

document. **MemorySize** = _n_;

#### \[VBScript\]

_n_ = document. **MemorySize**

document. **MemorySize** = _n_

## Version

Supported on EmEditor Professional Version 17.8 or later.