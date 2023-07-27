# ConvertCsv 方法 (Document ��H)

轉換 CSV 格式。

## 

### \[JavaScript\]

```
document.ConvertCsv( iDestMode, nFlags, strSepPos );
```

### \[VBScript\]

```
document.ConvertCsv( iDestMode, nFlags, strSepPos );
```

## 參數

_iDestMode_

指定要將目前的文檔轉換為 CSV 格式的索引。0 表示固定寬度的欄格式（非 CSV）。1 表示「自訂」對話方塊中 「CSV」 頁面上的第一個定義的格式（預設情況下是「逗號分隔」）。

_nFlags_

你能指定一個下列值的組合。

| 值 | 含義 |
| --- | --- |
| eeCsvHalfWidth | 假定所有字元為半形字元以提高速度。 |
| eeCsvDiscardUndo | 丟棄復原信息以提高速度。 |

_strSepCount_

如果目前的文檔是非 CSV 文檔，並且要將目前的固定欄寬的文檔轉換為 CSV 文檔，則此字串指定分隔符號之間的寬度，以逗號分隔。例如，「10，8」 表示 2 個以 10 和 8 個半形字元分隔的分隔符號。如果目前的文檔是 CSV 文檔，則忽略此參數。

## 範例

以下範例將固定寬度的欄轉換為逗號分隔的 CSV 格式。原始的固定欄寬格式為：

Madrid Spain   100

Paris  France  101

目標 CSV 文檔會變為：

Madrid,Spain,100

Paris,France,101

### \[JavaScript\]

```
document.ConvertCsv( 1, 0, "7,8" );
```

### \[VBScript\]

```
document.ConvertCsv 1, 0, "7,8"
```

## 版本

支持 EmEditor Professional 19.8 或之後的版本。
