# Q. 我能把任務欄上的系統匣圖示用我最喜歡的圖示來顯示嗎？

可以。到注冊表編輯器 (RegEdit.exe) 中，找到: HKEY\_CURRENT\_USERSoftwareEmSoftEmEditor v3Common。設置一個 TrayIconFile 值作為 REG\_SZ, 然后設置圖示檔案路徑，再把 TrayIconIndex 值作為 REG\_DWORD 然後設置圖示索引。
