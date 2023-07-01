# Compare 方法 (Editor ��H)

比較兩個文檔。

#### \[JavaScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_\[, _strResultFileName_\] );

#### \[VBScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_\[, _strResultFileName_\] )

## 參數

_nFlags_

你可以指定以下值的組合。

|     |     |
| --- | --- |
| eeCompareGenerateReport | 生成一個報告檔案。必須在 strResultFileName 中指定路徑名。 |
| eeCompareOpenReport | 打開報告檔案。必須指定 eeCompareGenerateReport。 |
| eeCompareQuality1 | 搜索附近行的最快的方法。 |
| eeCompareQuality2 |  |
| eeCompareQuality3 |  |
| eeCompareQuality4 |  |
| eeCompareQuality5 | 搜索整個檔案最精確的方法（有一定的限制）。 |
| eeCompareQuick | 快速比較，不會亮顯差異。此旗標不能與除 eeCompareQuiet 之外的其他選項結合使用。 |
| eeCompareQuiet | 不顯示任何匯出消息。 |
| eeCompareReport3Col | 使用 3 欄格式匯出報告。 |
| eeCompareReportDiffOnly | 僅報告不相同的行。 |
| eeCompareReset | 重設比較或同步捲動模式並清除比較結果。 |
| eeCompareResetAfter | 重設比較或同步捲動模式並在比較和報告生成後清除比較結果。另外，必須被指定 eeCompareGenerateReport。 |
| eeCompareRestorePos | 完成後恢復視窗位置。 |
| eeCompareSplitVert | 垂直分割視窗以顯示文檔。 |
| eeCompareSwitchNoWrap | 切換到不換行。 |
| eeCompareSyncCaret | 同步游標位置。 |
| eeCompareSyncScrollHorz | 同步水平捲動。 |
| eeCompareSyncScrollOnly | 顯示比較文檔但不用亮顯顯示差異。 |
| eeCompareSyncScrollVert | 同步垂直捲動。 |
| eeCompareTileHorz | 水平平鋪檔案。 |
| eeCompareTileVert | 垂直平鋪檔案。 |
| eeIgnoreCases | 忽略大小寫。 |
| eeIgnoreComments | 忽略組態標記為注釋的文字。 |
| eeIgnoreEmbeddedSpaces | 忽略一行中第一個和最後一個非空格字元之間的空格。 |
| eeIgnoreEncodings | 忽略編碼差異。 |
| eeIgnoreLeadSpaces | 忽略一行中第一個非空格字元之前的空格。 |
| eeIgnoreNewlines | 忽略換行符的差異。 |
| eeIgnoreTrailingSpaces | 忽略一行中最後一個非空格字元後的空格。 |

_strDocument1_

指定用於標識第一個文檔的字串。該值可以是檔案名，帶完整路徑的檔案名或一個冒號 (:) 後跟目前的組中的文檔索引。 例如，"filename.csv"，"C:\\data\\filename.csv" (在 JavaScript 中是"C:\\\data\\\filename.csv")，或 ":2"。

_strDocument2_

指定用於標識第二個文檔的字串。該值的格式與 strDocument1 相同。

_strResultFileName_

如果指定了此參數和 eeCompareGenerateReport，EmEditor 會儲存比較報告到此路徑，包括名稱。

## 返回值

返回值是以下值之一。

|     |     |
| --- | --- |
| eeDiff | 兩個文檔不相同。 |
| eeMatched | 兩個文檔相同。 |
| eeMatchedIgnored | 除了被忽略的地方外，兩個文檔是相同的。 |

## 版本

支持 EmEditor Professional v17.7 或之後的版本。
