# Q. 怎么能不用顯示對話方塊就安裝EmEditor？

在正常安裝的情況下，您會看到屏幕顯示對話方塊指示您完成一系列的安裝步驟。但是，如果您想把 EmEditor 安裝到公司，團體或個人使用的多臺電腦中時，您可以用一個批次檔案或指令碼檔案讓電腦自動完成安裝並簡化安裝步驟。EmEditor 使用 Windows 安裝程式來進行安裝，所以如果您不想看到對話方塊的話就可以把它們都屏蔽掉。

假設 EmEditor 的安裝檔案是 emed64\_20.9.0.msi，請運行以下命令：

msiexec /i "(...path...)emed64\_20.9.0.msi" /passive MSIINSTALLPERUSER=1

這樣，EmEditor 在安裝時就不會出現任何對話方塊。如果您想變更預設設定的話，您也可以使用以下的這些選項：

|     |     |
| --- | --- |
| MSIINSTALLPERUSER=1 | 為目前的使用者指定按使用者（即「只為我」）安裝（v20.9 或更高版本的預設值）。 |
| MSIINSTALLPERUSER="" | 指定按每臺電腦（即「所有使用者」）安裝（v20.8 或之前版本的預設設定）。 |
| NOCHECKUPDATES=1 | 停用到 Internet 上檢視最新版本 EmEditor 的功能。 |
| NOCONTEXTMENU=1 | 停用添加一個快速鍵到檔案總管上的內容功能表中。 |
| DESKTOP=1 | 啓用添加一個快速鍵到桌面。 |
| NOIEEDITOR=1 | 停用把 EmEditor 添加至 IE 瀏覽器 HTML 編輯清單中. |
| NOIEVIEW=1 | 停用在 IE 瀏覽器中用 EmEditor 檢視源程式碼的功能。 |
| NOPATH=1 | 禁止把到 EmEditor 的路徑添加到 PATH 環境變數中。 |
| NOSHORTCUT=1 | 禁止添加一個快速鍵到程式功能表中。 |
| NOTRAYICON=1 | 停用系統匣圖示。 |
| NOTXT=1 | 停用文字檔案關聯。 |
| REGNAME=name | 授權使用者姓名。 |
| REGKEY=xxxxxx | 輸入註冊金鑰。 |

如果您只想用註冊金鑰和授權者名字為目前的使用者安裝 EmEditor，請執行下列命令：

msiexec /i "emed64\_20.9.0.msi" /q MSIINSTALLPERUSER=1 REGKEY=xxxxx REGNAME="John Doe"

如果您想用註冊金鑰和授權者名字為所有使用者安裝 EmEditor，請使用系統管理員權限執行命令：

msiexec /i "emed64\_20.9.0.msi" /q REGKEY=xxxxx REGNAME="John Doe"

Windows 安裝程式還有許多別的選項。具體信息，請執行：

msiexec /?

來顯示一系列可以操作的命令。

## 備註:

在 Windows Vista 或更新的系統上操作時，安裝程式一定要在管理員特權上運行，來避免「使用者帳戶控制」提示。例如，如果您要在命令提示符上運行安裝程式，您需要在按 SHIFT 鍵的同時右擊命令提示符圖示來打開命令提示符視窗，然後選擇 **作為管理員運行** 程式。此外，您必須指定 **MSIINSTALLPERUSER=""** 才能為所有使用者安裝 EmEditor v20.9 或更高版本。要僅為目前的使用者安裝 EmEditor v20.8 或更早版本，您必須指定 **MSIINSTALLPERUSER=1**。
