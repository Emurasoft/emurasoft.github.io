# InsertFromFile 方法 (Selection ��H)

在游標位置處插入指定檔案的內容。

## 

### \[JavaScript\]

```
document.selection.InsertFromFile( strFileName, nEncoding, nFlags );
```

### \[VBScript\]

```
document.selection.InsertFromFile strFileName, nEncoding, nFlags
strFileName
指定要打開的檔案的完整路徑以及名稱。
nEncoding
從[編碼常數](../const/constencoding) 中選擇或指定任何用於 Windows 操作系統的代碼頁。
nFlags
指定一個下列值的組合:
|     |     |
| --- | --- |
| eeOpenDetectUnicode | 偵測 Unicode 簽名 (BOM)。 |
| eeOpenDetectUTF8 | 偵測 UTF-8。 |
| eeOpenDetectCharset | 偵測 HTML/XML 字元集。 |
| eeOpenDetectAll | 偵測所有編碼。 |
```

## 版本

支持 EmEditor 4.00 或之後的版本。
