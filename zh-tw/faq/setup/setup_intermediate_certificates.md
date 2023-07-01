# Q. 無法驗證程式檔案的數位簽章（當網際網路連線不可用時）。

如果在沒有連接網際網路的 PC 上運行 EmEditor，可能會遇到以下問題：

- 當嘗試啟動 EmEditor 時出現一個警告對話方塊「無法驗證程式檔案的數位簽章」。
- 無法驗證 EmEditor 檔案（例如 emeditor.exe 和 .msi 安裝程式）的數位簽章。
- EmEditor 的啟動速度變慢。

在這種情況下，請在運行 EmEditor 或驗證程式檔案的數位簽章時連接網際網路。 建立網路連接後，無需連接網際網路就可以繼續使用 EmEditor。

如果無法連接到網路，請按照以下步驟安裝 Sectigo Code Signing Intermediate Certificate（Sectigo 程式碼簽名中繼憑證）：

1. 從連接互聯網的 PC 上，轉到 ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false)。
2. 到 "Code Signing" 部分下載 "Standard Sectigo RSA Cod Signing CA"。
3. 將下載的檔案複製到存在 EmEditor 檔案的目標離線 PC。
4. 在目標 PC 上，右鍵單擊該檔案，選擇 "Install Certificate" （安裝憑證）。會出現 "Certificate Import Wizard" （憑證匯入精靈）。
5. 按照精靈選擇 "Place all certificates in the following store" （將所有憑證放入以下存儲區）, 單擊 "Browse"（瀏覽），然後選擇 "Intermediate Certification Authorities"（中間憑證頒發機構）。單擊「下一步」匯入憑證。

檢視 EmEditor 檔案（例如 emeditor.exe）的數位簽章，然後確認數位簽章沒問題就可以了。如果由於無法驗證根憑證讓數位簽章不 OK，請按照以下步驟安裝 Sectigo 根憑證：

1. 從連接互聯網的 PC 轉到 ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false)。
2. 到 "Root Certificates" 部分中下載 "SHA-2 Root: USERTrust RSA Certification Authority"。
3. 將下載的檔案複製到目標 PC。
4. 在目標 PC 上，右鍵單擊該檔案，然後選擇 "Install Certificate" （安裝憑證）。會出現 "Certificate Import Wizard" （憑證匯入精靈）。
5. 按照精靈選擇 "Place all certificates in the following store" （將所有憑證放入以下存儲區）, 單擊 "Browse"（瀏覽），然後選擇 "Intermediate Certification Authorities"（中間憑證頒發機構）。單擊「下一步」匯入憑證。
