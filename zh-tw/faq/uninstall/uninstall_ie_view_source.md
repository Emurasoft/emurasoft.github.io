# Q. 在我卸載 EmEditor 之後，當我在 IE 瀏覽器上的內容功能表中選擇「檢視源」后，為什么源代碼不顯示在記事本中？

一些比較早版本的 EmEditor 不能夠完全卸載注冊信息。您需要右擊 **「開始」** 功能表選擇 **「運行」**，然后輸入「RegEdit.exe」，在點擊「確定」鍵來啟用注冊表編輯器。請在注冊表編輯器中搜尋 HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\View Source Editor，然后刪除該項。
