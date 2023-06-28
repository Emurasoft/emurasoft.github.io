# WrapMode プロパティ

設定のプロパティの [**\[基本\]** タブ](../../dlg/properties/general/index) の
**\[折り返し方法\]** ドロップダウン リスト ボックスに相当します。

#### \[JavaScript\]

_nMode_ =
object. **WrapMode**;

object. **WrapMode** = _nMode_;

#### \[VBScript\]

_nMode_ =
object. **WrapMode**

object. **WrapMode** = _nMode_

## パラメータ

_nMode_

次の値から選択します。

|     |     |
| --- | --- |
| **eeWrapNone** | 行をまったく折り返さずに表示します。この場合は、論理行と表示行が常に一致します。 |
| **eeWrapByChar** | 指定する文字数で折り返します。指定する文字数は、 [**\[普通行の文字数\]** テキスト ボックス](../../dlg/properties/general/index) および <br> <br> [**\[引用行の文字数\]** テキスト ボックス](../../dlg/properties/general/index) で指定します。 |
| **eeWrapByWindow** | 行をウィンドウの右端に合わせて折り返します。ウィンドウのサイズを変更すると、折り返し位置もウィンドウに合わせて変更します。 |
| **eeWrapByPage** | 行をページの右端に合わせて折り返します。この場合、印刷時の折り返し位置と表示中の折り返し位置が一致します。 |

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。