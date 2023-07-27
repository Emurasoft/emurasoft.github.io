# DeleteFile 方法 (Shell ��H)

刪除一個或多個指定的檔案。

## 

### \[JavaScript\]

```
shell.DeleteFile( strFile );
```

### \[VBScript\]

```
shell.DeleteFile strFile
```

## 參數

_strFile_

要刪除的檔案的名稱。它可以在最後一個路徑組件中包含通配符。

## 範例

### \[JavaScript\]

```
shell.DeleteFile( "C:\\\Test\\\\*.txt" );
```

### \[VBScript\]

```
shell.DeleteFile "C:\\Test\\\*.txt"
```

## 版本

支持 EmEditor Professional 22.1 或之後的版本。
