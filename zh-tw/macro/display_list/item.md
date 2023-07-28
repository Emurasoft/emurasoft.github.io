# Item 屬性 (DisplayList 集合)

為指定索引檢索 [DisplayItem 對象](../display_item/index)。

## 

### \[JavaScript\]

```
item = list.Item( Index );
```

### \[VBScript\]

```
item = list.Item( Index )
```

## 參數

_Index_

指定以 1 為基準的整數為項目的索引。

如果對象是一個顏色清單，項目會是下列值之一。

|     |     |
| --- | --- |
| eeColorNormal | 常規 |
| eeColorSelection | 選取 |
| eeColorCurrentLine | 目前的行 |
| eeColorQuote | 引號行 |
| eeColorURL | URL |
| eeColorMailTo | 郵件地址 |
| eeColorTag | 包括「多檔尋找」結果的超連結的標籤 |
| eeColorSingleQuotes | 帶單引號 '...' 的字串 |
| eeColorDoubleQuotes | 帶雙引號 "..." 的字串 |
| eeColorComment | 註解 |
| eeColorScript | 指令碼 |
| eeColorBraces | 配對的圓括號/方括號 |
| eeColorInsideTag | HTML/XML 標籤 |
| eeColorHighlight1 | 亮顯 (1) |
| eeColorHighlight2 | 亮顯 (2) |
| eeColorHighlight3 | 亮顯 (3) |
| eeColorHighlight4 | 亮顯 (4) |
| eeColorHighlight5 | 亮顯 (5) |
| eeColorHighlight6 | 亮顯 (6) |
| eeColorHighlight7 | 亮顯 (7) |
| eeColorHighlight8 | 亮顯 (8) |
| eeColorHighlight9 | 亮顯 (9) |
| eeColorHighlight10 | 亮顯 (10) |
| eeColorReturn | 換行符號，Tab鍵，檔案結尾標記 |
| eeColorCursorLine | 水平/垂直行 |
| eeColorPageBreak | 分頁符/僅編輯選定區域 |
| eeColorLineNumbers | 行號 (數字) |
| eeColorRuler | 尺規/欄標題 (數字) |
| eeColorOutside | 超出區域 |
| eeColorCompareChange | 比較 \- 變更的行 |
| eeColorCompareChar | 比較 \- 變更的字元 |
| eeColorCompareAdded | 比較 \- 新增 |
| eeColorCompareDeleted | 比較 \- 刪除 |
| eeColorCompareBlank | 比較 \- 空白 |
| eeColorSpell | 錯誤拼字 |
| eeColorUnicode | Unicode 字元 |
| eeColorVerticalSel | 垂直選擇方塊架 |
| eeColorHexSel | 十六進位檢視選取框架 |
| eeColorIndentGuides | 縮排參考線 |
| eeColorHorzGrid | 水平網格 |
| eeColorOutline | 大綱 |
| eeColorLineNumberLines | 行號 (線) |
| eeColorRulerLines | 尺規/欄標題 (線) |
| eeColorVerticalSeparator | 垂直分隔符 |
| eeColorHtmlCharRef | HTML 字元引用 |
| eeColorUcn | 通用字元名稱/百分號編碼 |
| eeColorAutoMarker | 自動標記 |
| eeColorMarker1 | 標記 (1) |
| eeColorMarker2 | 標記 (2) |
| eeColorMarker3 | 標記 (3) |
| eeColorMarker4 | 標記 (4) |
| eeColorMarker5 | 標記 (5) |
| eeColorMarker6 | 標記 (6) |
| eeColorMarker7 | 標記 (7) |
| eeColorMarker8 | 標記 (8) |
| eeColorMarker9 | 標記 (9) |
| eeColorMarker10 | 標記 (10) |
| eeColorMatchingTag | 符合的標記 |
| eeColorBookmark | 書籤標示行 |
| eeColorUserDefinedGuides | 使用者定義的輔助線 |
| eeColorIndicatorModified | 垂直標記 \- 變更過的行 |
| eeColorIndicatorSaved | 垂直標記 \- 變更已儲存的行 |
| eeColorIndicatorBookmark | 垂直標記 \- 書籤 |
| eeColorMarkerModified | 捲軸標記 \- 變更過的行 |
| eeColorMarkerSaved | 捲軸標記 \- 變更已儲存的行 |
| eeColorMarkerBookmark | 捲軸標記 \- 書籤 |
| eeColorMarkerFound | 捲軸標記 \- 找到 |
| eeColorMarkerCursor | 捲軸標記 \- 游標位置 |
| eeColorMarkerCompareChange | 捲軸標記 \- 比較變更項 |
| eeColorMarkerCompareAdded | 捲軸標記 \- 比較新增項 |
| eeColorMarkerCompareDeleted | 捲軸標記 \- 比較刪除項 |
| eeColorHeadings | 標題 |
| eeColorSearchSel | 搜索範圍 |
| eeColorFilter | 篩選 |
| eeColorLinkUrlVisited | URL (瀏覽過的) |
| eeColorLinkIdVisited | 郵件地址 (瀏覽過的) |
| eeColorLinkTagVisited | 「多檔尋找」結果的超連結 (瀏覽過的) |
| eeColorCellText | CSV 儲存格選取文字 |
| eeColorCellBorder | CSV 儲存格選擇框架 |
| eeColorFilterSeparator | 篩選分隔符號 |
| eeColorMinimapBackground | 迷你地圖背景 |
| eeColorMinimapView | 迷你地圖視圖 |
| eeColorLinkIpv4 | IPv4 地址 |
| eeColorLinkIpv4Visited | IPv4 地址 (已訪問) |
| eeColorLinkIpv6 | IPv6 地址 |
| eeColorLinkIpv6Visited | IPv6 地址 (已訪問) |
| eeColorHexColor | 十六進位顏色 \- #ff0080 |
| eeColorRgbColor | RGB 顏色 - rgb(255,0,128) |
| eeColorLineNumberHovered | 行號 (懸停) |
| eeColorRulerHovered | 尺規/欄標題 (懸停) |
| eeColorLineNumberSel | 行號 (選取的行) |
| eeColorRulerSel | 尺規/欄標題 (選取的欄) |
| eeColorLineNumberCurr | 行號 (選區) |
| eeColorRulerCurr | 尺規/欄標題 (選區) |
| eeColorOpenFilter | 開啟篩選 |
| eeColorMultiSelection | 有多選區的行 |
| eeColorValidatorError | 語法檢查錯誤 |
| eeColorValidatorWarning | 語法檢查警告 |
| eeColorValidatorMessage | 語法檢查訊息 |
| eeColorEvenLines | 偶數行 |
| eeColorInvalidCharacters | 警告字元 |

如果對象是一個搜索清單，項目指定進行搜索的次數。

## 版本

支持 EmEditor 7.00 或之後的版本。
