# OpenFile メソッド (Editor オブジェクト)

既存のファイルを開きます。

## 

### \[JavaScript\]

```
editor.OpenFile( strFileName, [ nEncoding, [ nFlags
] ]
);
```

### \[VBScript\]

```
editor.OpenFile strFileName, [ nEncoding, [ nFlags ] ]
```

## パラメータ

_strFileName_

開く既存のファイル名を完全パスで指定します。

_nEncoding_

開くファイルのエンコードを指定します。 [エンコード定数](../const/const_encoding) から選択するか、または
Windows で使用されるエンコードを指定します。0 を指定するか、または省略すると、開くファイルの拡張子に関連付けられた設定のプロパティで指定されているエンコードで開きます。

_nFlags_

次の値の組み合わせを指定します。nEncoding が 0 または省略されている場合は、eeOpenAllowNewWindow 以外の値は無視されます。

|     |     |
| --- | --- |
| eeOpenAllowNewWindow | 既に開かれている文書が無題でないか、または変更されている場合、新しいウィンドウで開きます。 |
| eeOpenDetectUnicode | Unicode サイン (BOM) を検出します。 |
| eeOpenDetectUTF8 | UTF-8 を自動検出します。 |
| eeOpenDetectCharset | HTML/XML の Charset を検出します。 |
| eeOpenDetectAll | すべて自動検出します。 |
| eeUseDiskMode | ファイルを開く際、ディスク モードを使用します。 |
| eeDontUseDiskMode | ファイルを開く際、ディスク モードを使用しません。eeUseDiskMode も eeDontUseDiskMode も指定されていない場合、EmEditor は開こうとするファイルのサイズによって自動的にディスク モードを使用するかどうかを選択します。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。ただし、Version 5.00 以上で nEncoding、nFlags を省略することができます。
