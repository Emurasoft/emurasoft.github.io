# MemorySize 属性

检索或设置文档的每个大块的最大内存大小。可以在 **自定义** 对话框的 [**高级** 页面](../../dlg/customize/advanced/index) 上的 **内存大小** 文本框中指定默认值。 属性获取（n = document.MemorySize）总会成功，但设置（document.MemorySize = n）可能会抛出例外，如果文档已经使用比指定大小更大的内存大小。

#### \[JavaScript\]

_n_ = document. **MemorySize**;

document. **MemorySize** = _n_;

#### \[VBScript\]

_n_ = document. **MemorySize**

document. **MemorySize** = _n_

## 版本

支持 EmEditor v17.8 或之后的版本。