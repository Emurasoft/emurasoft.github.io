# 「代理伺服器」頁面

**代理伺服器**頁面允許您自訂與代理連線相關的設定。EmEditor 將使用此頁面上的代理伺服器設定通過 HTTP 和 HTTPS 連線到 `support.emeditor.org`，如果使用 AI 功能，它將使用代理伺服器設定連線到 `api.openai.com`。

## 「無代理」選項按鈕

在不指定代理伺服器設定的情況下連線到互聯網。如果您不使用代理伺服器或已[在 Windows 中使用 Proxy 伺服器](https://support.microsoft.com/zh-tw/windows/use-a-proxy-server-in-windows-03096c53-0554-4ffe-b6ab-8b1deee8dae1#ID0EFD=Windows_11)，請使用此設定。

## 「手動代理配置」選項按鈕

選中以啟用以下自訂代理設定。

### 「協議」下拉清單方塊

選擇 HTTP 或 SOCKS5 協議以連線到您的代理伺服器。

### 主機名稱

指定您的代理伺服器的主機名稱或 IP 地址。

### 端口號碼

指定您的代理伺服器的端口號碼。

### 代理認證

如果您的代理伺服器需要使用者名稱和密碼才能連線，請啟用此選項。

### 使用者名稱

指定用於連線的使用者名稱。

### 密碼

指定用於連線的密碼。您可以點擊 o-o 顯示或隱藏密碼。使用者名稱和密碼將存儲在您的計算機上。

### 代理伺服器網址

此欄位顯示對上面指定的所有設定進行編碼的 URL。您可以點擊 o-o 顯示或隱藏 URL。EmEditor 將使用此 URL 連線到代理。

## 「檢查連線」按鈕

點擊此按鈕以使用上述指定的設定測試與 `support.emeditor.org` 的連線。如果連線成功，此按鈕左側將顯示「✓ 連線成功！」。

如果不成功，將出現錯誤消息以診斷問題。請仔細檢查代理伺服器的設定並確保代理可訪問。

## 「重設」按鈕

重設為預設設定。