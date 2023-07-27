# DeleteFolder 方法 (Shell ����)

删除一个或多个指定的文件夹及其内容。指定的文件夹即使不为空也会被删除。

## 

### \[JavaScript\]

```
shell.DeleteFolder( strFolder );
```

### \[VBScript\]

```
shell.DeleteFolder strFolder
```

## 参数

_strFolder_

要删除的文件夹的名称。它可以在最后一个路径组件中包含通配符。

## 示例

### \[JavaScript\]

```
shell.DeleteFolder( "C:\\\Test\\\folder" );
```

### \[VBScript\]

```
shell.DeleteFolder "C:\\Test\\folder"
```

## 版本

支持 EmEditor Professional 22.1 或之后的版本。
