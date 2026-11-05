# DeleteFolder メソッド (Shell オブジェクト)

指定するフォルダーとその中身を削除します。指定したフォルダーが空でなくも削除されます。

## 

### \[JavaScript\]

```
shell.DeleteFolder( strFolder );
```

### \[VBScript\]

```
shell.DeleteFolder strFolder
```

## パラメーター

_strFolder_

削除するフォルダーの名前を指定します。パスの最後の要素にはワイルドカード文字を含めることができます。

## 例

### \[JavaScript\]

```
shell.DeleteFolder( "C:\\\\Test\\\\folder" );
```

### \[VBScript\]

```
shell.DeleteFolder "C:\\Test\\folder"
```

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。
