# Format メソッド (Selection オブジェクト)

選択範囲の折り返し位置に改行コードの挿入したり、改行コードを削除したりします。

## 

### \[JavaScript\]

```
document.selection.Format( nFlags );
```

### \[VBScript\]

```
document.selection.Format nFlags
```

## 引数

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeFormatInsertNL | 選択範囲の折り返し位置に改行コードを挿入します。 |
| eeFormatDeleteNL | 選択範囲の折り返し位置の改行コードを削除します。 |
| eeFormatSplitLines | 選択範囲の折り返し位置に改行コードを挿入して最後の空白を削除することにより行を分割します (EmEditor Professional Version 4.10 以上のみ)。 |
| eeFormatJoinLines | 選択範囲の折り返し位置の改行コードを削除して空白を挿入することにより行を結合します (EmEditor Professional Version 4.10 以上のみ)。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
