# 將 EmEditor 用作 Claude Code 的編輯器

在 Claude Code 的[互動模式](https://code.claude.com/docs/en/interactive-mode)中按 Ctrl+G 時，會開啟記事本，讓您編輯提示文字。依照下列步驟，可以將按 Ctrl+G 時開啟的編輯器變更為 EmEditor。

1. 結束 Claude Code。
2. 確認 EmEditor 位於 `PATH` 中。如果使用桌面版安裝程式安裝，通常已經設定好了。如果使用可攜版，請依下列方式設定 `PATH`：
   1. 開啟 Windows「開始」功能表，搜尋 **環境變數**，然後選取 **編輯您帳戶的環境變數**。
   2. 在 **系統內容** 中，按一下 **環境變數** 按鈕。
   3. 在 **使用者變數** 區段中，選取 **Path** 項目，然後按一下 **編輯**。
   4. 按一下 **新增**，然後貼上 EmEditor 安裝資料夾的路徑。
   5. 在每個開啟的視窗中按一下 **確定** 以儲存。
   6. 關閉並重新開啟終端機，讓新的 `PATH` 生效。
3. 在 EmEditor 中開啟檔案 `%USERPROFILE%\.claude\settings.json`。
4. 在 `env` 區段中新增 `VISUAL` 變數：

```json
{
  "env": {
    "VISUAL": "emeditor /sp"
  }
}
```

   - 如果已有 `"env"` 區段，請在其中新增 `"VISUAL": "emeditor /sp"` 這一行，並確認前一行以逗號結尾。
   - 如果沒有 `"env"` 區段，請新增上面顯示的整個區塊。如果檔案中已有其他設定，請將 `"env"` 與它們並列新增，並以逗號分隔。
   - 儲存檔案。
5. 執行 Claude Code。按 Ctrl+G 時，應該會開啟 EmEditor。在開啟的文件中輸入文字，然後關閉 EmEditor。輸入的文字會顯示在 Claude Code 的輸入方塊中。

## 疑難排解

- **在 Claude Code 中按 Ctrl+G 時，EmEditor 沒有開啟。** 開啟終端機並執行 `emeditor`。如果 EmEditor 啟動，表示 `PATH` 設定正確。如果 EmEditor 沒有啟動，請參閱步驟 2。
- **`PATH` 正確，但按 Ctrl+G 時 EmEditor 沒有開啟。** 將 `VISUAL` 的值變更為 `emeditor.exe` 的完整路徑。在 JSON 中，反斜線必須寫成兩個以進行逸出。例如：

```json
{
  "env": {
    "VISUAL": "C:\\path_to\\EmEditor\\EmEditor.exe /sp"
  }
}
```
