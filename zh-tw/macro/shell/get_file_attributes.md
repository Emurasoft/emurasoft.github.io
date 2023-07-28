# GetFileAttributes 方法 (Shell 對象)

返回指定檔案或資料夾的屬性。

## 

### \[JavaScript\]

```
nAttr = shell.GetFileAttributes( strFile );
```

### \[VBScript\]

```
nAttr = shell.GetFileAttributes( strFile )
```

## 參數

_strFile_

用於檢索屬性的檔案或資料夾的完整路徑和名稱。

## 範例

### \[JavaScript\]

```
nAttr = shell.GetFileAttributes( "C:\\\Test\\\file.txt" );
```

### \[VBScript\]

```
nAttr = shell.GetFileAttributes( "C:\\Test\\file.txt" )
```

## 返回值

返回以下值的組合。

|     |     |
| --- | --- |
| 值 | 描述 |
| 0 | 正常 |
| 1 | 唯讀 |
| 2 | 隱藏 |
| 4 | 系統 |
| 8 | 數量 |
| 16 | 目錄 |
| 32 | 封存 |
| 1024 | 別名 |
| 2048 | 已壓縮 |

## 版本

支持 EmEditor Professional 22.1 或之後的版本。
