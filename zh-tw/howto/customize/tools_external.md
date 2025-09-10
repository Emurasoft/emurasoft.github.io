# 外部工具範例

- 打開 **Internet Explorer**

**命令**: C:\\Program Files\\Internet Explorer\\iexplore.exe

**參數**: $(Path)

**初始目錄**: $(Dir)

**圖示路徑**: C:\\Program Files\\Internet Explorer\\iexplore.exe

勾選 **儲存檔案**

- 打開 **檔案總管**

**命令**: %WinDir%\\explorer.exe

**參數**: $(Dir)

**初始目錄**: $(Dir)

**圖示路徑**: %WinDir%\\explorer.exe

- 打開 **命令提示符**

**命令**: %WinDir%\\system32\\cmd.exe

**參數**: $(Dir)

**初始目錄**: $(Dir)

**圖示路徑**: %WinDir%\\system32\\cmd.exe

- 使用 **Visual C++** 編譯

**命令**: %WinDir%\\system32\\cmd.exe

**參數**: /k "C:\\Program Files\\Visual Studio\\Vc7\\bin\\vcvars32.bat"&&cl $(Path)

**初始目錄**: $(Dir)

**圖示路徑**: C:\\Program Files\\Visual Studio\\Common7\\IDE\\devenv.exe

勾選 **儲存檔案**

- 運行關聯的程式

**命令**: $(Path)

**參數**:

**初始目錄**: $(Dir)

**圖示路徑**:

勾選 **儲存檔案**

- 使用 **Google** 搜索游標處的單字或所選文字

**命令**: http://google.com/search?q=$(CurText)

**參數**:

**初始目錄**:

**圖示路徑**:

- 從 **Microsoft Visual SourceSafe** 簽出

**命令**: %WinDir%\\system32\\cmd.exe

**參數**: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkout
$/(path)/$(Filename).$(Ext) -y(user name)

**初始目錄**: $(Dir)

**圖示路徑**: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

- 簽入到 **Microsoft Visual SourceSafe**

**命令**: %WinDir%\\system32\\cmd.exe

**參數**: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkin
$/(path)/$(Filename).$(Ext) -y(user name)

**初始目錄**: $(Dir)

**圖示路徑**: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

勾選 **儲存檔案**

你可以在**命令**、**參數**、**初始目錄**和**圖示路徑**中使用以下預定義參數。

$(Path) 檔案的完整路徑名。

$(Dir) 檔案所在的目錄名。

$(Filename) 不帶副檔名的檔案名。

$(Ext) 檔案副檔名。

$(CurLine) 游標所在的邏輯行號。

$(CurText) 如果已選擇則為所選文字，否則為游標處的單字。

你也可以指定環境變數，例如 %WinDir%。