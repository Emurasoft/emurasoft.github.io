# 運行巨集 (�е{)

當儲存一個巨集檔案，巨集變為預設巨集檔案，并且，會在下次您選擇 [運行巨集 命令](../../cmd/macros/quick_macro_run) 時被加載。如果您打開巨集 的下拉功能表，您會看到運行 命令的右邊出現了"tutorial.jsee" 或 "tutorial.vbee"。另外，如果您把游標指針放在「運行巨集」 按鈕上，您會看到"運行巨集 tutorial.jsee" 或 "運行巨集 tutorial.vbee"的提示。總之，當要選擇巨集執行命令時所出現的巨集檔案名是預設的巨集。EmEditor 儲存預設巨集直到它記錄一個新的巨集，或選擇或儲存另一個巨集。當您退出 EmEditor 后，再重新打開它，預設的巨集保持不變。

現在選擇 [新增文字 命令](../../cmd/file/file_new) 來顯示一個新的 EmEditor 視窗。然后選擇 [運行巨集 命令](../../cmd/macros/quick_macro_run)。之前錄制的巨集會被顯示:

"EmEditor supports macros _."_

您想運行該巨集幾次都可以。

記住，當您錄制或選擇另一個巨集時，您便取代了預設巨集，這樣您就不能執行上面所顯示的之前儲存的巨集。在這種情況下，您可以用下面的任一方法來運行之前被錄制的巨集:

1. 點擊 [選擇巨集 命令](../../cmd/macros/macro_select)。在快顯的
In the resulting打開檔案 對話方塊中，選擇一個您想要運行的巨集檔案 (在這個教程中，我們選擇 tutorial.jsee 或 tutorial.vbee) 。然后，通過之前所描述的步驟運行該巨集。
2. 點擊功能表上的巨集。巨集 的下拉功能表中包括了已被儲存的巨集的清單。讓我們把該清單稱為"我的巨集"。您能通過從清單中選擇一個來運行指定的巨集 (在這個教程中，我們選擇 tutorial.jsee 或 tutorial.vbee) 。

預設情況下，EmEditor 會自動添加已經被錄制或選取的巨集到我的巨集 中。如果您不想要您的巨集被自動添加到我的巨集 中，請選擇 [自訂巨集 命令](../../cmd/macros/customize_macro)。
在 [自訂巨集 對話方塊](../../dlg/macro_customize/index) 的 [選項 頁面](../../dlg/macro_customize/options/index) 上，點擊清除對 [自訂巨集 對話方塊](../../dlg/macro_customize/index) 上的當儲存或選擇新的巨集時將該巨集添加至「我的巨集」。 核取方塊的勾選。這個動作會關閉該功能，這樣巨集就不會自動被添加到我的巨集 中當您儲存或選取一個巨集時。

同樣，如果您想要刪除一個巨集檔案，從 [自訂巨集 對話方塊](../../dlg/macro_customize/index) 中 [我的巨集 頁面](../../dlg/macro_customize/my_macros/index) 上選擇您想要刪除的巨集檔案的名稱。然后點擊「刪除」 按鈕。另外，該頁面還能讓您變更巨集檔案在巨集 下拉功能表中顯示的順序。

如果您想要用鍵盤上的一個快速鍵運行巨集，您可以通過 [所有組態屬性 命令](../../cmd/tools/all_prop) 或 [當前組態屬性 命令](../../cmd/tools/customize) 中的 [鍵盤 頁面](../../dlg/properties/keyboard/index) 給巨集分配一個快速鍵。

## 下一主題:
