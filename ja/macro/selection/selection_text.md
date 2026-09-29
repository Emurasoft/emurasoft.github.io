# Text プロパティ (Selection オブジェクト)

選択されたテキストを取得、またはテキストを挿入します。テキストを取得する際にテキストが長すぎる場合、プロパティの取得は失敗します。サポートされる最大長は UTF-16 文字単位で、V8 を使用している場合は 0x19fffffe、それ以外の場合は 0x3ffffffe です。

## 

### \[JavaScript\]

```
str = document.selection.Text;
document.selection.Text = str;
```

### \[VBScript\]

```
str = document.selection.Text
document.selection.Text = str
```

## 例

### \[JavaScript\]

```
str = document.selection.Text;
alert( "選択されていたテキストは " + str );
document.selection.Text = "こんにちは";
```

### \[VBScript\]

```
str = document.selection.Text
alert "選択されていたテキストは " & str
document.selection.Text = "こんにちは"
```

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
