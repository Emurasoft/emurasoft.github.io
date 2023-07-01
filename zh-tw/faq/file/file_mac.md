# Q. 當讀取 Macintosh 文字檔案時，一些字元無法正常顯示。怎樣才能正常地讀取 Macintosh 文字檔案呢？

Macintosh 與 Windows 系統使用的代碼頁稍有不同。在 Windows 2000/XP/2003/Vista 中，Macintosh 的代碼頁已經安裝了，您能輕松地把 Macintosh 文字檔案轉換成 Windows 文字檔案。首先，在 **工具** 功能表中選擇 [**定義編碼** 命令](../../cmd/tools/define_code_page) 在快顯的 [**定義編碼** 對話方塊](../../dlg/encodings/index) 中，點擊 **「新增」** 按鈕，然后選擇一個 Macintosh
編碼，例如「10001 (MAC – Japanese)」。再選擇一個適當的字型類別，例如，Japanese (日文)。點擊 **「確定」** 兩次關閉對話方塊。

接著，到 **檔案** 下拉單中，選擇 [**打開...** 命令](../../cmd/file/file_open)，
選擇您要定義的編碼，例如，從 **編碼** 組合方塊中選擇 「10001 (MAC -
Japanese)」，接著選擇一個您想要讀取的 Macintosh 檔案。

在 Windows 98/Me 中，沒有安裝 Macintosh 的代碼頁，所以您無法正常讀取有特殊字元的 Macintosh 檔案，因為 Windows 代碼頁無法讀取這些檔案。
