# 取代一個字串 (�е{)

要取代一個字串，添加第九行到我們所示范的巨集中:

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

document.selection.CharLeft( false, 12 );

document.selection.DeleteLeft( 15 );

document.selection.CharRight( true, 9 );

document.selection.ChangeCase( eeCaseUpperCase );

if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!"
);

n = document.selection.Replace( "editor", "######", eeReplaceAll );

alert( n + " strings found!" );

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

document.selection.CharLeft False, 12

document.selection.DeleteLeft 15

document.selection.CharRight True, 9

document.selection.ChangeCase eeCaseLowerCase

If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"

n = document.selection.Replace( "editor", "######", eeReplaceAll )

alert n & " strings found!"

儲存該巨集并在一個新的 EmEditor 視窗中運行它。注意兩個"editor" 字串已經被不區分大小寫地搜尋了，并且被 "######" 所取代，還有一個消息方塊會顯示 " Two strings found!" 。

[Replace 方法](../selection/selection_replace) 的第一個參數指定要搜尋的字串，第二個參數指定要取代為的字串，第三個參數指定標志的組合。該方法返回字串被取代的次數。如果您指定 eeReplaceAll 在第三個參數中，該方法會立即取代字串并且可能會返回大于 1 的一個數字。有關第三個參數的標志，詳見 [Replace 方法](../selection/selection_replace) 的參數說明。

通常在 [Replace 方法](../selection/selection_replace)，與 [Find 方法](../selection/selection_find) 相同，不會終止執行一個巨集當沒有找到搜尋字串。但是，有一個例外。如果您用 **巨集** 功能表下的 [**使用臨時選項運行** 命令](../../cmd/macros/macro_run_options)，并在快顯的 [**巨集臨時選項** 對話方塊](../../dlg/macro_temp_options/index) 中勾選了 **搜尋失敗即停止** 核取方塊，那么巨集就會被終止當沒有找到搜尋字串時。詳見教程中的 [尋找一個字串](tutorial_find)。
