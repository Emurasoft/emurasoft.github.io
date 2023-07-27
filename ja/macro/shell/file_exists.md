# FileExists メソッド ()

指定するファイルが存在すれば true を、存在しなければ false を返します。

## 

### \[JavaScript\]

```
shell.FileExists( strFile );
```

### \[VBScript\]

```
shell.FileExists strFile
```

## パラメータ

_strFile_

存在するかどうかを調べるファイルの名前を指定します。

## 例

### \[JavaScript\]

```
b = shell.FileExists( "C:\\\Test\\\file.txt" );
```

### \[VBScript\]

```
b = shell.FileExists( "C:\\Test\\file.txt" )
```

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。
