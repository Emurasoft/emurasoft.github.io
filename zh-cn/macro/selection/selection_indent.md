# Indent 方法 (Selection 对象)

按指定的缩进等级数来缩进被选取的行。

## 

### \[JavaScript\]

```
document.selection.Indent( [ nCount ] );
```

### \[VBScript\]

```
document.selection.Indent [ nCount ]
```

## 参数

_nCount_

可选项。指定缩进等级数。默认值是 1。如果指定的是负数，该方法与 [**UnIndent** \
方法](selection_unindent) 的行为相同。如果指定值为 0，该方法的行为与指定值为 1 时的行为相同。

## 版本

支持 EmEditor 4.00 或之后的版本。
