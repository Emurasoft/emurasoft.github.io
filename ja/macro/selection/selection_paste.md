# Paste メソッド ()

クリップボードの中身をカーソル位置に貼り付けます。

## 

### \[JavaScript\]

```
document.selection.Paste( nFlags );
```

### \[VBScript\]

```
document.selection.Paste nFlags
```

## 引数

_nFlags_

次の値の組み合わせになります。

|     |     |
| --- | --- |
| eeCopyUnicode | Unicode で貼り付けます (既定)。 |
| eeCopyQuotes | 引用マークを付けて貼り付けます。 |
| eeCopyNL | 改行コードを付けて貼り付けます。 |
| eeCopySystemDefault | [システム既定のエンコード](../../glossary/systemdefaultencoding) で貼り付けます。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
