# EmEditor 中巨集的模塊化設計 (�\��)

EmEditor 中的巨集是獨立于 EmEditor 之外的模塊，它是作為動態鏈結庫 (DLL) 檔案被執行的。為了維護系統資源，DLL 僅僅在巨集執行期間被加載。
