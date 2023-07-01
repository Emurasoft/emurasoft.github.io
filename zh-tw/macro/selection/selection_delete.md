# Delete 方法 (Selection ��H)

刪除選取內容。如果選定內容是空的，刪除游標右邊的指定字元數。

#### \[JavaScript\]

document.selection. **Delete**( \[\[ _nCount_ \], _bComplete_ \] );

#### \[VBScript\]

document.selection. **Delete** \[\[ _nCount_ \], _bComplete_ \]

## 參數

_nCount_

可選項。指定游標右邊要刪除的字元數。預設值為 1。如果指定的是負數，那這個方法與 [**DeleteLeft** \
方法](selection_deleteleft) 的行為相同。如果指定的是 0，會刪除游標往右的 1 個字元數。

_bComplete_

可選項。指定在儲存格選擇模式中是否要完全刪除選區。如果省略，指定 True。

## 版本

支持 EmEditor 4.00 或之後的版本。
