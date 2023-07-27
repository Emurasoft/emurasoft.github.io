# Q. 外部工具組態的例子有哪些？

- 打開IE瀏覽器

命令: C:\\Program Files\\Internet Explorer\\iexplore.exe

參數: $(Path)

初始目錄: $(Dir)

圖示路徑: C:\\Program Files\\Internet Explorer\\iexplore.exe

CheckSave File

- 打開檔案總管

命令: %WinDir%\\explorer.exe

參數: $(Dir)

初始目錄: $(Dir)

圖示路徑: %WinDir%\\explorer.exe

- 打開命令提示符

命令: %WinDir%\\system32\\cmd.exe

參數: $(Dir)

初始目錄: $(Dir)

圖示路徑: %WinDir%\\system32\\cmd.exe

- 通過Visual C++ 編譯

命令: %WinDir%\\system32\\cmd.exe

參數: /k "C:\\Program Files\\Visual Studio\\Vc7\\bin\\vcvars32.bat"&&cl $(Path)

初始目錄: $(Dir)

圖示路徑: C:\\Program Files\\Visual Studio\\Common7\\IDE\\devenv.exe

檢查儲存檔案

- 運行相關程式

命令: $(Path)

參數:

初始目錄: $(Dir)

圖示路徑:

檢查儲存檔案

- 用Google 搜尋在游標處的單字或一段選取的文字。

命令: http://google.com/search?q=$(CurText)

參數:

初始目錄:

圖示路徑:

- 從Microsoft Visual SourceSafe 簽出

命令: %WinDir%\\system32\\cmd.exe

參數: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkout
$/(path)/$(Filename).$(Ext) -y(user name)

初始目錄: $(Dir)

圖示路徑: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

- 簽入到Microsoft Visual SourceSafe 中

命令: %WinDir%\\system32\\cmd.exe

參數: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkin
$/(path)/$(Filename).$(Ext) -y(user name)

初始目錄: $(Dir)

圖示路徑: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

檢查儲存檔案

您能在命令，參數，初始目錄，and圖示路徑 中使用下面預先定義的參數。

$(Path) 檔案的完整路徑名稱。

$(Dir) 檔案的目錄名稱。

$(Filename) 副檔名之外的檔案名。

$(Ext) 檔案名的延伸。

$(CurLine) 游標處的邏輯行行號。

$(CurText) 選取的文字或在游標處的單字(如果沒有選取的文字)。

您還能指定環境變量，例如 %WinDir% 。
