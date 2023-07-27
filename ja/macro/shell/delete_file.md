# DeleteFile メソッド ()

指定するファイルを削除します。

## 

### \[JavaScript\]

```
shell.DeleteFile( strFolder );
```

### \[VBScript\]

```
shell.DeleteFile strFolder
```

## パラメータ

_strFile_

削除するファイルの名前を指定します。パスの最後の要素にはワイルドカード文字を含めることができます。

## 例

### \[JavaScript\]

```
shell.DeleteFile( "C:\\\Test\\\\*.txt" );
```

### \[VBScript\]

```
shell.DeleteFile "C:\\Test\\\*.txt"
```

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。
