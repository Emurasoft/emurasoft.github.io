# 文件验证结果对话框

**文件验证结果**对话框提供有关文件验证过程结果的信息。当您选择**验证**命令时，会出现此对话框。

在**文件验证结果**对话框中，您会看到以下详细信息：

1. 验证后两个文件是否匹配。
2. 原始文件的路径、大小和 SHA256 哈希值。
3. 临时文件的路径、大小和 SHA256 哈希值。

如果文件不匹配，可能是由于以下几个原因：

- 原始文件在打开后可能已被更改。只有在文件未被修改的情况下，您才能运行此命令。然而，宏或插件可以重置指示文件已更改的标志。
- 原始文件可能包含无法转换为 Unicode 的 NULL 或无效字符。
- 原始文件可能包含不直接映射到指定编码中的 Unicode 的字符。例如，在 Shift-JIS 编码中，某些字符会重复列为“IBM 扩展字符”和“NEC 选定的 IBM 扩展字符”。例如，在 Shift-JIS 文件中代码为 0xFA58 的字符（IBM 扩展字符“㈱”），在 EmEditor 中打开时，其 Unicode 字符代码将变为 U+3231。此外，如果以 Shift-JIS 保存，那么它会被存储为代码为 0x878A 的相同字符（即“NEC 选定的 IBM 扩展字符”）。
- 文件可能是使用**高级打开**命令打开的，并带有诸如**在每个指定字节数处插入换行符**或**确保每个文件末尾都有换行符**的选项。
- 硬盘或内存可能存在问题。如果您尝试打开网络上的文件，可能是网络问题。

## 删除临时文件复选框

选取此选项将删除保存的临时文件。