# Join 方法 (Editor 對象)

按指定索引鍵資料欄，用一個與 JOIN 操作類似的方法合併兩個 CSV 文檔，并創建一個新文檔。

## 

### \[JavaScript\]

```
n = editor.Join( nFlags, strDocument1, strColumn1, strDocument2, strColumn2, strSelect, strSeparator, nLimit );
```

### \[VBScript\]

```
n = editor.Join( nFlags, strDocument1, strColumn1, strDocument2, strColumn2, strSelect, strSeparator, nLimit)
```

## 參數

_nFlags_

您能從如下值中指定一個組合。不能組合 eeJoinSimpleMerge，eeJoinContain，eeJoinStartWith，和 eeJoinEndWith。

|     |     |
| --- | --- |
| eeJoinUniqueKey1 | 第一個文檔中指定的索引鍵資料欄包含一個唯一索引鍵。 |
| eeJoinUniqueKey2 | 第二個文檔中指定的索引鍵資料欄包含一個唯一索引鍵。 |
| eeJoinIncludeAll1 | 第一個文檔中的所有資料列都會被包括在輸出中。輸出文檔將包含空的資料格如果第一個文檔中的行沒有符合的結果。 |
| eeJoinIncludeAll2 | 第一個文檔中的所有資料列都會被包括在輸出中。輸出文檔將包含空的資料格如果第一個文檔中的行沒有符合的結果。 |
| eeJoinMatchCase | 大小寫符合。 |
| eeJoinSimpleMerge | 不比較索引鍵，直接合併兩個文檔。如果指定該選項，那么 _strColumn1_ 和 _strColumn2_ 的參數會被忽略。 |
| eeJoinIgnoreHeadings1 | 忽略第一個文檔中的標題，讓第一個文檔中的標題能在合併后的檔案中保留。 |
| eeJoinIgnoreHeadings2 | 忽略第二個文檔中的標題。 |
| eeJoinContain | Key1 包含 Key2。 |
| eeJoinStartWith | Key1 以 Key2 開始。 |
| eeJoinEndWith | Key1 以 Key2 結尾。 |
| eeJoinMatchSplitBoth | 兩個分割的字串都符合。 |
| eeJoinMatchSplitOne | Key1 符合分割的 Key2。 |
| eeJoinFuzzy | 使用模糊比對。 此旗標不能與 eeJoinEndWith、eeJoinMatchSplitBoth 或 eeJoinMatchSplitOne 結合使用。此旗標會使過程變慢。 |
| eeJoinSwap | Key1 和 Key2 互換，如果還指定了 eeJoinContain，eeJoinStatWith，eeJoinEndWith，或 eeJoinMatchSplitOne。 |

_strDocument1_

指定字串來識別第一個文檔。這個值可以是檔案名，檔案名以及路徑，或一個冒號 (:) 后跟目前的群組中指定文檔的索引號。例如，"filename.csv"，"C:\\data\\filename.csv" (如果是 JavaScript，"C:\\\\data\\\\filename.csv")，或 ":2"。

_strColumn1_

指定字串來識別第一個文檔的索引鍵資料欄。這個值可以是指定欄的第一行或一個冒號 (:) 后跟指定欄的索引號。例如，"first\_name"，":5"，"1-5"，或 "2-"。

_strDocument2_

指定字串來識別第二個文檔。這個值的格式與 strDocument1 格式相同。

_strColumn2_

指定字串來識別第二個文檔的索引鍵資料欄。這個值的格式與 strColumn1 格式相同。

_strSelect_

指定字串來選擇要包括在輸出文檔中的欄。例如，"file1.csv>column1,file2.csv>column2"。

_strSeperator_

在分割儲存格時，將字串指定為分隔符號。除非指定 eeJoinMatchSplitBoth 或 eeJoinMatchSplitOne，否則將忽略此參數。

_nLimit_

指定每個儲存格的最大分割次數。如果省略或指定為 0，則該方法將不限制分割次數。除非指定 eeJoinMatchSplitBoth 或 eeJoinMatchSplitOne，否則將忽略此參數。

## 返回值

返回值是與指定字串符合的行數。

## 版本

支持 EmEditor 14.8 或之後的版本。
