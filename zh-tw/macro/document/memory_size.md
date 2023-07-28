# MemorySize 屬性 (Document 對象)

檢索或設置文檔的每個大塊的最大記憶體大小。可以在自訂 對話方塊的 [進階 頁面](../../dlg/customize/advanced/index) 上的記憶體大小 文字方塊中指定預設值。 屬性獲取（n = document.MemorySize）總會成功，但設置（document.MemorySize = n）可能會拋出例外，如果文檔已經使用比指定大小更大的記憶體大小。

## 

### \[JavaScript\]

```
n = document.MemorySize;
document.MemorySize = n;
```

### \[VBScript\]

```
n = document.MemorySize
document.MemorySize = n
```

## 版本

支持 EmEditor v17.8 或之後的版本。
