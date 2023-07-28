# DeleteFolder メソッド (Shell オブジェクト)

指定するフォルダとその中身を削除します。指定したフォルダが空でなくも削除されます。

## 

### \[JavaScript\]

```
shell.DeleteFolder( strFolder );
```

### \[VBScript\]

```
shell.DeleteFolder strFolder
```

## パラメータ

_strFolder_

削除するフォルダの名前を指定します。パスの最後の要素にはワイルドカード文字を含めることができます。

## 例

### \[JavaScript\]

```
shell.DeleteFolder( "C:\\\Test\\\folder" );
```

### \[VBScript\]

```
shell.DeleteFolder "C:\\Test\\folder"
```

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。
