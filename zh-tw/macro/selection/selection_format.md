# Format 方法 (Selection 對象)

插入或刪除選定內容中的新行。

## 

### \[JavaScript\]

```
document.selection.Format( nFlags );
```

### \[VBScript\]

```
document.selection.Format nFlags
```

## 參數

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eeFormatInsertNL | 在選區的換行處插入換行符號。 |
| eeFormatDeleteNL | 在選區的換行處移除換行符號。 |
| eeFormatSplitLines | 通過插入新行并刪除尾隨空白來分割行 (適用於 EmEditor 4.10 或之後的版本) 。 |
| eeFormatJoinLines | 通過插入新行并刪除尾隨空白來合併行 (適用於 EmEditor 4.10 或之後的版本) 。 |

## 版本

支持 EmEditor 4.00 或之後的版本。
