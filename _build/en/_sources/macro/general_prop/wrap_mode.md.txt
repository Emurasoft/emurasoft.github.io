# WrapMode 屬性

與組態屬性中 [**一般** 頁面](../../dlg/properties/general/index) 上的 **自動換行** 下拉清單方塊相對應。

#### \[JavaScript\]

_nMode_ =
object. **WrapMode**;

object. **WrapMode** = _nMode_;

#### \[VBScript\]

_nMode_ =
object. **WrapMode**

object. **WrapMode** = _nMode_

## 參數

_nMode_

從下列值中選擇。

|     |     |
| --- | --- |
| eeWrapNone | 不換行。 |
| eeWrapByChar | 按指定字元長度 (字節數) 換行。字元長度能在 [**標準行邊距** 文字方塊](../../dlg/properties/general/index) 或 [**引用行邊距** 文字方塊](../../dlg/properties/general/index) 中指定。 |
| eeWrapByWindow | 按視窗寬度換行。如果視窗的大小被重新調整，換行的位置也會被調整。 |
| eeWrapByPage | 按列印的頁面寬度換行。 |

## 版本

支持 EmEditor 7.00 或之後的版本。