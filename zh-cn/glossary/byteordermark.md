# 字节顺序标记 (BOM)

一个字节顺序标记 (BOM) 是在码位 FEFF 处的字符。它被用来代表在怎样编码一个 Unicode，Unicode big endian，或 UTF-8 文件中的数据。在 Unicode (little endian)，文件的第一个字节是 FF，第二个字节是 FE。在 Unicode big endian 中，文件的第一个字节是 FE，第二个字节是 FF。在 UTF-8 中，文件的第一个字节是 EF，第二个字节是 BB，第三个字节是 BF。
