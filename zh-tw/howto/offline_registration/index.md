# 離線註冊

使用[產品註冊對話方塊](../../dlg/regist/index)進行註冊需要互聯網串連。

如果您在線上註冊過程中遇到錯誤信息「請求錯誤：發送請求的 URL… 找不到這樣的主機。」，請確保您的防火墻允許 `EmEditor.exe` 通過端口 80 和 443 訪問 `support.emeditor.com`。

如果您想在沒有互聯網串連的情況下註冊 EmEditor，可以使用離線註冊功能。離線註冊要求 EmEditor 版本 24.3.0 或更高。

離線註冊在註冊過程中使用授權檔案。授權檔案通過電子郵件發送給客戶。請按照以下步驟，使用離線授權註冊 EmEditor。

1. 使用[聯繫表單](https://zh-tw.emeditor.com/support/#contact)請求授權檔案。在表單中，請使用您在 [Emurasoft 使用者中心](https://support.emeditor.com/)使用的電子郵件地址。包括您的註冊金鑰或 [Stripe 訂閱 ID](https://support.emeditor.com/en/account/subscriptions)。
2. 我們將通過電子郵件回復您的請求，郵件中附有授權檔案。將授權檔案下載到本地磁盤中一個不需要管理員權限訪問的資料夾中。
3. 如果您已經註冊了 EmEditor，請使用[註冊信息](../../dlg/registration_info/index)取消註冊。
4. 關閉 EmEditor。使用[命令列選項](https://www.emeditor.org/zh-tw/howto/file/file_commandline.html#options) `/ol "licenseFilePath"` 進行操作，其中 `licenseFilePath` 是授權檔案的路徑。以下是命令範例。

```
EmEditor.exe /ol "C:\Users\Example\emeditorLicenseFile-a7PT7Au3TOelfK1w.txt"
```

5. 打開 EmEditor 並檢視[註冊信息](../../dlg/registration_info/index)，確認離線註冊是否成功。授權檔案現在可以刪除，因為不再需要用它啟動 EmEditor。

## 技術信息

關於離線註冊的內部細節可以[在這裡](https://www.emeditor.com/general/new-validation-system-explained/)檢視。
