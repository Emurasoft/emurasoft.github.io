# FolderExists メソッド (Shell オブジェクト)

指定するフォルダが存在すれば true を、存在しなければ false を返します。

## 

### \[JavaScript\]

```
shell.FolderExists( strFolder );
```

### \[VBScript\]

```
shell.FolderExists strFolder
```

## パラメータ

_strFolder_

存在するかどうかを調べるフォルダの名前を指定します。

## 例

### \[JavaScript\]

```
b = shell.FolderExists( "C:\\\\Test\\\\folder" );
```

### \[VBScript\]

```
b = shell.FolderExists( "C:\\Test\\folder" )
```

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。
