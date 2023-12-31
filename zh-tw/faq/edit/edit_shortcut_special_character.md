# Q. 怎么給特殊字元設置快速鍵？

許多特殊字元已經有預設的快速鍵方式了。請點擊下面的連結檢視已設置的一些特殊字元的快速鍵:

[插入特殊字元](../../howto/edit/edit_special_char)

除此之外，您可以用巨集給任何您常用到的字元設置快速鍵。例如，如果想要用一個快速鍵插入ä，您可以編寫一個巨集(這個例子中，我們用 JavaScript 編寫):

document.selection.Text="ä";

然后把這個檔案儲存為 **InsertA.jsee**。在 **「巨集」** 下拉單中點擊 **「選擇...」**，并打開 InsertA.jsee。當運行這個巨集時，EmEditor 便會自動插入這個字元。您只需要打開「工具」下的「組態屬性」，到「鍵盤」頁面上，在「類別」下拉清單中選擇「我的巨集」，并自訂一個快速鍵給這個巨集，設定完成后，您就能用您自訂的快速鍵來插入這個特殊字元了。
