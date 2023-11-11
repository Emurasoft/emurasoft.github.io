# 多檔尋找 (教程)

要多檔尋找，添加第八行到我們所示范的巨集中:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
document.selection.ChangeCase( eeCaseUpperCase );
if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!"
);
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseLowerCase
If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"
```
儲存該巨集并在一個新的 EmEditor 視窗中運行它。現在 "Em" 被搜尋并且出現顯示有 "Found!" 的消息方塊。
[Find 方法](../selection/selection_find) 的第一個參數指定一個要搜尋的字串；第二個參數指定要告知它如何搜尋的標志。在這個例子中，第二個參數是 eeFindPrevious，即從目前的游標位置向前搜尋到該檔案的頂部。
[Find 方法](../selection/selection_find) 返回 1 如果搜尋字串被找到。不然，則返回 0。在這個例子中，搜尋字串被找到，返回 1，因此執行 Then 子句，即 [alert 方法](../window/window_alert)。
[alert 方法](../window/window_alert) 顯示一個簡單的帶有「OK」按鈕的消息方塊以及該參數的字串。在我們的示例中，它會顯示文字 "Found!"。
[Find 方法](../selection/selection_find) 的第二個參數讓您能指定一系列的標志。更多說明請詳見 [Find 方法](../selection/selection_find)。
通常不會終止執行一個巨集當沒有找到搜尋字串。但是，有一個例外。如果您用巨集 功能表下的使用臨時選項運行 命令，并在快顯的對話方塊中勾選了搜尋失敗即停止 核取方塊，那么就會終止執行巨集當沒有找到搜尋字串時。
使用臨時選項運行 讓您能用更靈活的方式進行搜尋。例如，如果您想要重複一個操作，比如搜尋和取代，并且您不知道操作會發生幾次，您可以不用修改巨集，勾選搜尋失敗即停止 核取方塊，并輸入一個比您認為您所需要的重複操作次數多的數字。
如果您想不用使用臨時選項運行 命令就終止巨集當搜尋失敗時，那么您需要修改該巨集。即，當 [Find 方法](../selection/selection_find) 返回 0，您會終止該巨集。下列的代碼可以做到:

### \[JavaScript\]

```
if( !document.selection.Find( "xx", eeFindPrevious ) )  throw new
Error("Cannot find xx");
```

### \[VBScript\]

```
If Not document.selection.Find( "xx", eeFindPrevious )  Then Err.Raise
vbObjectError + 1, "Find Error", "Cannot find xx"
另外，如果您用 [FindRepeat 方法](../selection/selection_findrepeat)，
您能再次搜尋您之前搜尋過的字串，并且您能搜尋游標所在位置的單字。
如果您如下指定了 [FindRepeat 方法](../selection/selection_findrepeat) 的標志，它會執行搜尋，并有相對應的鍵盤快速鍵。
```
|     |     |
| --- | --- |
| eeFindRepeatNext | 從游標位置向下再次搜尋您之前搜尋過的字串。等同于 F3。 |
| eeFindRepeatPrevious | 從游標位置向上再次搜尋您之前搜尋過的字串。等同于 Shift + F3。 |
| eeFindRepeatNext + eeFindRepeatWord | 從游標位置向下搜尋被選取的字串或游標處的單字。等同于 CTRL + F3。 |
| eeFindRepeatPrevious + eeFindRepeatWord | 從游標位置向上搜尋被選取的字串或游標處的單字。等同于 CTRL + SHIFT + F3。 |
