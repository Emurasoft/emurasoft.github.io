# 變更選取範圍 (�е{)

要更改選取範圍，添加第六行到我們所示范的巨集中:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
儲存該巨集并在一個新的 EmEditor 視窗中運行它。注意，"text edit" 部分會如下圖所示被亮顯顯示:
text editor.
我們把 true 傳遞到CharRight 方法 的第一個參數中，這樣就變更了游標位置并且改變了選取範圍；您也可以當按住 SHIFT 鍵的同時按右箭頭鍵來進行相同的操作。
同樣，許多游標移動方法接收參數來變更選取範圍 (詳見 [移動游標](tutorialmove)) 。
更多變更選取範圍的可用方法:
|     |     |
| --- | --- |
|[SelectAll](../selection/selectionselectall) | 選擇整個文字。等同于 CTRL + A 鍵。 |
|[SelectLine](../selection/selectionselectline) | 選擇游標所在處的行。 |
|[SelectWord](../selection/selectionselectword) | 選擇游標位置處的整個單字。 |
|[Collapse](../selection/selectioncollapse) | 關閉目前的選項。等同于 ESC 鍵。 |
您能用下列屬性安裝或檢查選取範圍的狀態:
|     |     |
| --- | --- |
|[IsActiveEndGreater](../selection/selectionisactiveendgreater) | 顯示活動點是否與選取範圍的結尾部分符合。 |
|[IsEmpty](../selection/selectionisempty) | 顯示是否選取範圍為空。 |
|[Mode](../selection/selectionmode) | 獲取或安裝選擇類型 (垂直選擇，行選擇等等) 。 |
```

## 下一主題:
