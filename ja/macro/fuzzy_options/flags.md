# Flags プロパティ ()

フラグを設定または取得します。

この値は、0 または以下の値の組み合わせになります。

|     |     |
| --- | --- |
| eeFuzzyIgnoreCombining | 発音区分符号、濁点、半濁点などの前進を伴わない結合文字を区別しません。 |
| eeFuzzyIgnoreEmoji | 絵文字シーケンスの違いは無視されます。 |
| eeFuzzyIgnoreKanaSize | 仮名の大小は無視されます。 |
| eeFuzzyIgnoreKanaType | ひらがなとカタカナの違いを無視します。 |
| eeFuzzyIgnoreVS | 異字体セレクタは無視されます。 |
| eeFuzzyIgnoreWidth | 半角文字と全角文字の違いは無視されます。 |

## 

### \[JavaScript\]

```
n = obj.Flags;
obj.Flags = n;
```

### \[VBScript\]

```
n = obj.Flags;
obj.Flags = n;
```

## バージョン

EmEditor Professional Version 22.0 以上で利用できます。
