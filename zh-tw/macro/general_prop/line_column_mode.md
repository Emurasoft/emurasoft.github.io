# LineColumnMode 屬性 (GeneralProp ��H)

與組態屬性中 [**一般** 頁面](../../dlg/properties/general/index) 上的 **行列顯示** 下拉清單方塊相對應。

#### \[JavaScript\]

_n_ _Mode_ =
object. **LineColumnMode**;

object. **LineColumnMode** = _nMode_;

#### \[VBScript\]

_nMode_ =
object. **LineColumnMode**

object. **LineColumnMode** = _nMode_

## 參數

_nMode_

從下列值中選擇。

|     |     |
| --- | --- |
| eeLineColumnView | 行號和列位置會以被顯示的方式計數。如果換行，那么被換行的位置也會被計算在內。列的位置會在換行處被還原為 1。一個全形的字元計為 2 。這是如同文字處理器一樣的顯示方式。 |
| eeLineColumnLogicalA | 用真正的邏輯行號來計算行號和列位置。行號與列位置不取決于換行方式。一個全形字元被計為 2 列。一個 Tab字元被計為 1 個字元。 |
| eeLineColumnLogicalW | 用真正的邏輯行行號來計算行號和列位置。行號與列位置不取決于換行方式。一個全形字元被計為 1 列。一個 Tab字元被計為 1 個字元。 |
| eeLineColumnTabA | 用真正的邏輯行行號來計算行號和列位置。行號與列位置不取決于換行方式。一個全形字元被計為 2 列。當計數一個 Tab字元時，就當它是用空格代替的。 |

## 版本

支持 EmEditor 7.00 或之後的版本。
