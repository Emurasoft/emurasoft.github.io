# Unpivot メソッド (Document オブジェクト)

CSVデータを平らにして行に変換します。

## 

### \[JavaScript\]

```
document.Unpivot( strSelect, strAttrLabel, strValueLabel, nFooter );
```

### \[VBScript\]

```
document.Unpivot strSelect, strAttrLabel, strValueLabel, nFooter
```

## パラメータ

_strSelect_

ピボット解除する列を選択する文字列を指定します。例: "2-5"、"3-"、"1,3,5"。このパラメータが空または省略した場合には、"2-" が指定されたとみなされます。

_strAttrLabel_

属性として作成される列のヘディングのラベルを指定します。

_strValueLabel_

値として作成される列のヘディングのラベルを指定します。

_nFooter_

フッターの行数を指定します。フッターの領域は変換されません。

## 例

1 列目を除くすべての列をピボット解除します。最後の行は無視されます。

### \[JavaScript\]

```
document.Unpivot( "2-", "Attribute", "Value", 1 );
```

### \[VBScript\]

```
document.Unpivot( "2-", "Attribute", "Value", 1 )
```

## バージョン

EmEditor Professional Version 21.4 以上で利用できます。
