# clearData メソッド ()

クリップボードを空にします。

#### \[JavaScript\]

clipboardData. **clearData**( \[ _sDataFormat_, \[ _iPos_ \] \] );

#### \[VBScript\]

clipboardData. **clearData** \[ _sDataFormat_, \[ _iPos_ \] \]

## パラメータ

_sDataFormat_

空にするクリップボードのフォーマットを文字列で指定します。次の文字列を指定することができます。空の文字列を指定するか、または省略した場合は、テキストを含むすべてのフォーマットを消去します。

|     |     |
| --- | --- |
| Text | テキストを含むすべてのフォーマットを消去します。 |
| LineText | 行テキストのフォーマットを指定します。 |
| BoxText | 箱型テキストのフォーマットを消去します。 |

_iPos_

任意指定。古いクリップボードのデータを削除したい場合は、クリップボード履歴の位置を指定します。これに 0 を指定するか、または省略すると、現在のデータが削除されます。

## 例

#### \[JavaScript\]

clipboardData.clearData();

#### \[VBScript\]

clipboardData.clearData

## バージョン

EmEditor Professional Version 5.00 以上で利用できます。