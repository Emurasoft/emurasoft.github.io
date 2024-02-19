# SetFileAttributes 方法 (Shell 對象)

設定指定檔案或資料夾的屬性。

## 

### \[JavaScript\]

```
shell.SetFileAttributes( strFile, nAttr );
```

### \[VBScript\]

```
shell.SetFileAttributes strFile, nAttr
```

## 參數

_strFile_

要設定屬性的檔案或資料夾的完整路徑和名稱。

_nAttr_

以下值的組合。

|     |     |
| --- | --- |
| 值 | 描述 |
| 0 | 正常 |
| 1 | 唯讀 |
| 2 | 隱藏 |
| 4 | 系統 |
| 32 | 封存 |

## 範例

### \[JavaScript\]

```
shell.SetFileAttributes( "C:\\\\Test\\\\file.txt", 1 );
```

### \[VBScript\]

```
shell.SetFileAttributes "C:\\Test\\file.txt", 1
```

## 版本

支持 EmEditor Professional 22.1 或之後的版本。
