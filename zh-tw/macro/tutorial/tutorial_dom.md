# 巨集的規格 (文檔對象模型) (教程)

在 EmEditor 巨集文檔對象模型 (DOM) 的規格中，In the specifications of the EmEditor macro Document 對象 Model (DOM), **[Window 對象](../window/index)** 是目前的的範圍。換句話說，沒有明確的範圍的屬性和方法指的都是目前的的 **[Window 對象](../window/index)**。
例如，第一個 _document_ 是 Window 對象的 **[document 屬性](../window/window_document)**，適用於網頁瀏覽器的指令碼。對于熟悉網頁瀏覽器指令碼的使用者，下面的代碼可能會比較眼熟:

## 

### \[JavaScript\]

```
document.write("EmEditor supports macros.");
```

### \[VBScript\]

```
document.write "EmEditor supports macros."
上面任一指令碼都會產生同樣的結果；[Text 屬性](../selection/selectiontext) 以及[write 方法](../document/documentwrite) 的行為是一致的。
在 EmEditor 巨集中，您能用多個對象。我們這樣設計巨集是為了達到面向對象的編程 (OOP) 以及允許程式的延伸性并能適應增強的巨集，例如在一個巨集中操縱多個視窗和文檔。
您能在 EmEditor 巨集中用下列的對象:
-[Window 對象](../window/index) \-
變為預設範圍，這樣，不需要指定對象名稱。它會提供 Windows 使用者界面的方法與屬性。比如， [document\
屬性](../window/windowdocument) 讓您能把[Document 對象](../document/index) 的屬性與方法用於目前的文檔。同樣，[editor \
屬性](../window/windoweditor) 讓您能訪問[Editor 對象](../editor/index)。
-[Document 對象](../document/index) \-
為打開的文檔提供方法和屬性，應用於整個文檔中的所有元素，包括檔案中的細節部分，例如文檔的檔案名，安裝名，還有唯讀狀態。而且，[selection \
屬性](../document/documentselection) 讓您能把[Selection \
對象](../selection/index) 用於目前的選區範圍 (Selection Range) 以及游標位置。
-[Selection 對象](../selection/index) \-
為目前的選區範圍 (Selection Range) 以及游標位置提供方法和屬性。它提供許多方法和屬性。例如在選區範圍內的選取變更 (Selection Change)，字元轉換，游標移動，搜尋以及取代。
-[Editor 對象](../editor/index) \- EmEditor
EmEditor 為整個應用程式所提供的方法和屬性。例如，它提供 EmEditor 可執行的檔案的路徑和版本，以及用於打開新或指定檔案的方法和屬性。
```

## 下一主題:
