# SetFileAttributes メソッド (Shell オブジェクト)

指定するファイルまたはフォルダの属性を設定します。

## 

### \[JavaScript\]

```
shell.SetFileAttributes( strFile, nAttr );
```

### \[VBScript\]

```
shell.SetFileAttributes strFile, nAttr
```

## パラメータ

_strFile_

属性を設定するファイルまたはフォルダの完全パス。

_nAttr_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| 値 | 説明 |
| 0 | 通常 |
| 1 | 書き換え禁止 |
| 2 | 隠しファイル |
| 4 | システム |
| 32 | アーカイブ |

## 例

### \[JavaScript\]

```
shell.SetFileAttributes( "C:\\\\Test\\\\file.txt" );
```

### \[VBScript\]

```
shell.SetFileAttributes "C:\\Test\\file.txt"
```

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。
