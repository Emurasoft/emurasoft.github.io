# 文本属性（Document 对象）

检索文档文本。如果文本过长，该属性将失败。使用 V8 时，支持的最大长度（以 UTF-16 字符计）为 0x19fffffe；否则为 0x3ffffffe。

##

### \[JavaScript\]

```
str = document.Text;
```

### \[VBScript\]

```
str = document.Text
```

## 版本

支持 EmEditor Professional 26.3 或更高的版本。