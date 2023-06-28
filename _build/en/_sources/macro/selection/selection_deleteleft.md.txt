# DeleteLeft 方法

刪除所選內容。如果選定內容是空的，那么刪除游標左邊的指定字元數。

#### \[JavaScript\]

document.selection. **DeleteLeft**( \[ _nCount_ \] );

#### \[VBScript\]

document.selection. **DeleteLeft** \[ _nCount_ \]

## 參數

_nCount_

可選項。指定游標左邊要刪除的字元數。預設值為 1。如果指定的是負數，那這個方法與 [**Delete** \
方法](selection_delete) 的行為相同。如果指定的是 0，會刪除游標往左的 1 個字元數。

## 版本

支持 EmEditor 4.00 或之後的版本。