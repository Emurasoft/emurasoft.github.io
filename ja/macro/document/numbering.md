# Numbering メソッド (Document オブジェクト)

カーソル位置または垂直選択に番号を挿入します。

## 

### \[JavaScript\]

```
editor.Numbering( strFirst, strInc, nMaxLines [, nFlags ] );
```

### \[VBScript\]

```
editor.Numbering strFirst, strInc, nMaxLines [, nFlags ]
```

## パラメータ

_strFirst_

最初の行に挿入する初期値または文字を指定します。このテキストには、数字でない接頭語または接尾語 (または両方) を追加することができます ( _nFlags_ パラメータに eeNumOther が選択されていない場合に限る)。

_strInc_

増加量を 10 進数で指定します。これは最初の行と 2 番目の行の値の差になります。

_nMaxLines_

行数を 10 進数で指定します。

_nFlags_

次の値の組み合わせを指定することができます。0 を指定するか省略すると、このメソッドは 10 進数で番号を挿入します。

| 値 | 意味 |
| --- | --- |
| eeNumCapitalLetters | 16 進数を大文字で挿入します。 |
| eeNumSkipEmptyLines | 箱型選択または複数選択を行っている場合、空行をスキップして数字を挿入するかどうかを指定します。 |
| eeNumRestartNumEmpty | 箱型選択または複数選択を行っている場合、空行の後、番号を最初から数え直すかどうかを指定します。 |
| eeNumRestartNumDiscontinuous | 複数選択を行っている場合、不連続行で番号を最初から数え直すかどうかを指定します。 |
| eeNumHexadecimal | 番号を 16 進数で指定します。 |
| eeNumOctal | 番号を 8 進数で指定します。 |
| eeNumBinary | 番号を 2 進数で指定します。 |
| eeNumOther | 番号の代わりに文字を挿入します。\[最初の行\] テキスト ボックスで指定した文字から始まり、\[増加量\] テキスト ボックスで指定する Unicode の文字コード値の増加量で連続する文字を挿入します。1 行に 1 文字のみ挿入することができます。 |

## バージョン

EmEditor Professional Version 19.1 以上で利用できます。
