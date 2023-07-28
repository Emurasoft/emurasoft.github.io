# Unpivot 方法 (Document 對象)

通過壓平合併 CSV 數據將欄轉換為列。

## 

### \[JavaScript\]

```
document.Unpivot( strSelect, strAttrLabel, strValueLabel, nFooter );
```

### \[VBScript\]

```
document.Unpivot strSelect, strAttrLabel, strValueLabel, nFooter
```

## 參數

_strSelect_

指定用於選擇要取消樞紐的列的字串。例如，"2-5"，"3-"，"1,3,5"。如果該參數為空或省略，則會體現為 "2-"。

_strAttrLabel_

指定要建立的屬性欄的標題標籤。

_strValueLabel_

指定要建立的值欄的標題標籤。

_nFooter_

指定頁腳中的列數。頁腳列不會被轉換。

## 範例

取消樞紐除第一欄之外的所有欄。最後一列被忽略。

### \[JavaScript\]

```
document.Unpivot( "2-", "Attribute", "Value", 1 );
```

### \[VBScript\]

```
document.Unpivot( "2-", "Attribute", "Value", 1 )
```

## 版本

支持 EmEditor Professional v21.4 或之後的版本。
