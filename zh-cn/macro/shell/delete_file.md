# DeleteFile 方法 (Shell 对象)

删除一个或多个指定的文件。

## 

### \[JavaScript\]

```
shell.DeleteFile( strFile );
```

### \[VBScript\]

```
shell.DeleteFile strFile
```

## 参数

_strFile_

要删除的文件的名称。它可以在最后一个路径组件中包含通配符。

## 示例

### \[JavaScript\]

```
shell.DeleteFile( "C:\\\\Test\\\\\*.txt" );
```

### \[VBScript\]

```
shell.DeleteFile "C:\\Test\\\*.txt"
```

## 版本

支持 EmEditor Professional 22.1 或之后的版本。
