# SetFileAttributes 方法 (Shell ����)

设置指定文件或文件夹的属性。

## 

### \[JavaScript\]

```
shell.SetFileAttributes( strFile, nAttr );
```

### \[VBScript\]

```
shell.SetFileAttributes strFile, nAttr
```

## 参数

_strFile_

要设置属性的文件或文件夹的完整路径和名称。

_nAttr_

以下值的组合。

|     |     |
| --- | --- |
| 值 | 描述 |
| 0 | 正常 |
| 1 | 只读 |
| 2 | 隐藏 |
| 4 | 系统 |
| 32 | 存档 |

## 示例

### \[JavaScript\]

```
shell.SetFileAttributes( "C:\\\Test\\\file.txt", 1 );
```

### \[VBScript\]

```
shell.SetFileAttributes "C:\\Test\\file.txt", 1
```

## 版本

支持 EmEditor Professional 22.1 或之后的版本。
