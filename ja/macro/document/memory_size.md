# MemorySize プロパティ ()

文書で使用されている1かたまりのメモリ サイズを取得します。既定値は、\[カスタマイズ\] ダイアログ ボックスの [\[高度\] ページ](../../dlg/advanced/index) の \[メモリ サイズ\] テキスト ボックスで指定された値になります。プロパティの取得 (n = document.MemorySize) は常に成功しますが、設定 (document.MemorySize = n) は、文書が既に指定されたサイズより大きなメモリ サイズを使用している場合、例外を発生させることがあります。

## 

### \[JavaScript\]

```
n = document.MemorySize;
document.MemorySize = n;
```

### \[VBScript\]

```
n = document.MemorySize
document.MemorySize = n
```

## バージョン

EmEditor Professional Version 17.8 以上で利用できます。
