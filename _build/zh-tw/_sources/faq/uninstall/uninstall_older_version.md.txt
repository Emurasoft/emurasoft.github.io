# Q. 我不能從控制面板上的「卸載或更改程式」中卸載舊版的EmEditor，我要怎么做？

如果您無法卸載一個舊的版本，請用「/L\*V log.txt」指令來運行舊版的安裝程式，這樣就會為卸載該程式創建一個 **日志檔案(log file)**。
例如，如果安裝程式名是「emed64\_14.3.1.exe」，請運行下面的指令:

emed64\_14.3.1.exe **/L\*V log.txt**

這個 log.txt 檔案可能含有非常有用的信息，比如為什么安裝程式停止工作。

注意: 舊版的安裝程式能在
**C:\\ProgramData\\Emurasoft\\EmEditor\\updates\\update...** 資料夾中找到。

如果您在卸載或安裝一個新的版本時，看到下面的對話方塊內容:

「您試圖使用的功能在一個不可用的CD-ROM或其它移動磁盤上。請插入『EmEditor Professional (…)』磁盤并點擊確認。」

首先，請先找到舊版的安裝程式。用 「/extract」 把該安裝程式提取出來。例如，如果安裝程式是 「emed64\_14.3.1.exe」，您可以運行下面的指令:

emed64\_14.3.1.exe **/extract**

這將創建一個子資料夾。在這個資料夾中，您將會看到一個有著「.msi」 副檔名的檔案，在我們舉的這個例子中，您會看到檔案名顯示為「emed64\_14.3.1 **.msi**"。

當您卸載時，看到了以上所述的對話方塊內容，請點擊「瀏覽」按鈕，并指定上面的 .msi 檔案。繼續這個過程，您應該可以卸載舊版的EmEditor。

如果您不確定您需要哪一個 .msi 檔案，您可以檢視 log.txt 檔案，應該會找到相關信息。

另外，如果當您從控制面板卸載時卸載程式停止運行，請試試看用 [GeekUninstaller (freeware)](http://www.geekuninstaller.com/) 或 [Revo Uninstaller (freeware)](http://www.revouninstaller.com/revo_uninstaller_free_download.html) 來進行卸載。

如果您還是需要說明的話，請把具體發生的情況寫下來，并和 log.txt 檔案一起發送到我們的技術支持部 [tech@emurasoft.com](mailto:tech@emurasoft.com)。我們會盡快答復您。