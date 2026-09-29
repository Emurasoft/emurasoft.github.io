# Text プロパティ (Document オブジェクト)

文書のテキストを取得します。テキストが長すぎる場合、このプロパティは失敗します。サポートされる最大長は UTF-16 文字数で、V8 を使用している場合は 0x19fffffe、それ以外の場合は 0x3ffffffe です。

## 

### \[JavaScript\]

```
str = document.Text;
```

### \[VBScript\]

```
str = document.Text
```

## バージョン

EmEditor Professional Version 26.3 以上で利用できます。
