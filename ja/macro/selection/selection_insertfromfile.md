# InsertFromFile メソッド ()

指定したファイルの中身をカーソル位置に挿入します。

## 

### \[JavaScript\]

```
selection.InsertFromFile( strFileName, nEncoding, nFlags );
```

### \[VBScript\]

```
selection.InsertFromFile strFileName, nEncoding, nFlags
strFileName
開く既存のファイル名を完全パスで指定します。
nEncoding
開くファイルのエンコードを指定します。 [エンコード定数](../const/constencoding) から選択するか、または
Windows で使用されるエンコードを指定します。
nFlags
次の値の組み合わせを指定します。
|     |     |
| --- | --- |
| eeOpenDetectUnicode | Unicode サイン (BOM) を検出します。 |
| eeOpenDetectUTF8 | UTF-8 を自動検出します。 |
| eeOpenDetectCharset | HTML/XML の Charset を検出します。 |
| eeOpenDetectAll | すべて自動検出します。 |
```

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
