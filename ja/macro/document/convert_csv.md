# ConvertCsv メソッド (Document オブジェクト)

CSV形式を変換します。

## 

### \[JavaScript\]

```
document.ConvertCsv( iDestMode, nFlags, strSepPos );
```

### \[VBScript\]

```
document.ConvertCsv( iDestMode, nFlags, strSepPos );
```

## パラメータ

_iDestMode_

変換先の CSV フォーマットのインデックスを指定します。0 は CSV でなく固定幅列のフォーマットを意味します。1 は [カスタマイズ] ダイアログの [CSVフォーマット] ページで定義された最初のフォーマットを意味します (既定では、カンマ区切り)。

_nFlags_

次の値の組み合わせを指定することができます。

| 値 | 意味 |
| --- | --- |
| eeCsvHalfWidth | すべて半角文字とみなします |
| eeCsvDiscardUndo | 元に戻す情報を破棄します |
| eeCsvTruncateUnfit | 列の幅よりも長い文字列は切り詰めます |
| eeCsvPromptInvalid | 文字列の長さが列の幅を超えると警告します |

_strSepCount_

現在の文書が CSV フォーマットでない場合で、固定幅列のフォーマットを CSV 文書に変換したい場合、この文字列は列幅の配列をカンマで区切って指定します。例えば、「10, 8」は、2 本のセパレーターが 10 と 8 の半角文字幅で区切られていることを示します。現在の文書が CSV 文書の場合、このパラメータは無視されます。

## 例

次の例は、固定幅列フォーマットをカンマ区切り CSV フォーマットに変換します。元の固定幅列フォーマット:

```
Madrid Spain   100
Paris  France  101
```

変換先の CSV 文書:

```
Madrid,Spain,100
Paris,France,101
```

### \[JavaScript\]

```
document.ConvertCsv( 1, 0, "7,8" );
```

### \[VBScript\]

```
document.ConvertCsv 1, 0, "7,8"
```

## バージョン

EmEditor Professional Version 19.8 以上で利用できます。
