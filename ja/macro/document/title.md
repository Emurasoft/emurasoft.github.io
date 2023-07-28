# Title プロパティ (Document オブジェクト)

文書のタイトルを取得、または設定します。タイトルには長いタイトルと短いタイトルを LF で区切って指定することができます (\\n または Chr(10))。

## 

### \[JavaScript\]

```
strTitle = document.Title;document.Title = strTitle;
```

### \[VBScript\]

```
strTitle = document.Title
document.Title = strTitle
```

## 例

### \[JavaScript\]

```
document.Title = "This is a long title.\\nShort title";
```

### \[VBScript\]

```
document.Title = "This is a long title." & Chr(10) & "Short title"
```

## バージョン

EmEditor Professional Version 21.8 以上で利用できます。
