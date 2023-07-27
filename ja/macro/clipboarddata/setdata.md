# setData メソッド ()

クリップボードに指定するデータを設定します。

## 

### \[JavaScript\]

```
bSuccess = clipboardData.setData( sDataFormat, sData, [ iPos ] );
```

### \[VBScript\]

```
bSuccess = clipboardData.setData( sDataFormat, sData, [ iPos ] )
```

## パラメータ

_sDataFormat_

設定するクリップボードのフォーマットを文字列で指定します。次の文字列を指定することができます。

|     |     |
| --- | --- |
| Text | テキストのフォーマットを指定します。 |
| LineText | 行テキストのフォーマットを指定します。 |
| BoxText | 箱型テキストのフォーマットを指定します。 |

_sData_

設定するテキストのデータを文字列で指定します。

_iPos_

任意指定。古いクリップボードのデータを設定したい場合は、クリップボード履歴の位置を指定します。これに 0 を指定するか、または省略すると、現在のデータが設定されます。

## 例

### \[JavaScript\]

```
clipboardData.setData("Text", "Hello!");
```

### \[VBScript\]

```
clipboardData.setData "Text", "Hello!"
```

## バージョン

EmEditor Professional Version 5.00 以上で利用できます。
