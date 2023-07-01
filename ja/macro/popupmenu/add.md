# Add メソッド ()

メニューの項目を追加します。

#### \[JavaScript\]

popupmenu. **Add**( _strText_, _id,_ \[ _flags_ \] );

#### \[VBScript\]

popupmenu. **Add** _strText_, _id,_ \[ _flags_ \]

## パラメータ

_strText_

表示する文字列を指定します。flags に eeMenuSeparator を指定する場合、空の文字列を指定する必要があります。

_id_

任意の整数を指定します。Track メソッドでは、ここで指定した値が戻り値になります。flags に eeMenuSeparator を指定する場合、0 を指定する必要があります。

_flags_

項目の状態を指定します。次の値を組み合わせて指定します。省略すると、0 を指定することになります。

|     |     |
| --- | --- |
| eeMenuChecked | 項目がチェックされた状態にします。 |
| eeMenuGrayed | 項目が無効であることを指定します。 |
| eeMenuSeparator | セパレータを指定します。 |

## バージョン

EmEditor Professional Version 5.00 以上で利用できます。
