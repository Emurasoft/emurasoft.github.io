# FolderExists 方法 (Shell 對象)

如果指定資料夾存在則返回 true；如果沒有，則為 false。

## 

### \[JavaScript\]

```
b = shell.FolderExists( strFolder );
```

### \[VBScript\]

```
b = shell.FolderExists( strFolder )
```

## 參數

_strFolder_

要確定其存在的資料夾的名稱。

## 範例

### \[JavaScript\]

```
b = shell.FolderExists( "C:\\\Test\\\folder" );
```

### \[VBScript\]

```
b = shell.FolderExists( "C:\\Test\\folder" )
```

## 版本

支持 EmEditor Professional 22.1 或之後的版本。
