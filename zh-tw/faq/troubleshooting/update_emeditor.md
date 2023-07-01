# Q. 更新 EmEditor 時發生錯誤，並且需要重新啟動。

更新 EmEditor 時，安裝程式顯示以下消息，並且可能需要重新啟動。

「安裝程式沒有足夠權限存取此目錄：C:\\Program Files\\EmEditor。安裝無法繼續。請以系統管理員身分登入，或請連絡您的系統管理員。」

可能有另一個應用程式將 EmEditor 安裝資料夾保持為打開狀態。建議您在更新 EmEditor 之前關閉所有應用程式，特別是 Brother 列印機隨附的 Brother Control Center（BrCtrlCntr.exe）可能會打開 EmEditor 資料夾。您可以在工作列通知區域中找到的 Control Center。

如果問題仍然存在，請使用 [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) 並搜索 EmEditor 安裝資料夾的所有開啟的控制代碼。

通常，系統僅要求系統重啟作為最後的選擇，並且這樣做基本上是為了使系統可以釋放需要更新的資源。尤其是當系統重新啟動時，請使用 Process Installer 並搜索 C:\\Program Files\\EmEditor 的所有控制代碼。
