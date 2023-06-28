# Q. EmEditor 被指定為另一個應用程式的外部文字編輯器。為什么在 EmEditor 中做的改變沒有在這個應用程式中顯現出來？

如果 EmEditor 被設定為另一個應用程式(例如郵件客戶端)的外部文字編輯器，并且這個應用程式監控著 EmEditor 的操作，這個程式很有可能不會反映用 EmEditor 儲存并修改的內容。要解決這個問題，請用 [/sp (分離)選項](../../howto/file/file_commandline)
在單獨的進程中啟動 EmEditor (具體操作方式是: 右擊 Windows「開始」功能表－>點擊「運行」－>輸入「emeditor /sp」)。要注意的是在這種情況下，每一個 EmEditor 視窗都會作為單獨的群組顯示。