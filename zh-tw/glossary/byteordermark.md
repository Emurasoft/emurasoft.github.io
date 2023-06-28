# 位元順序標記 (BOM)

一個位元順序標記 (BOM) 是在碼位 FEFF 處的字元。它被用來代表在怎樣編碼一個 Unicode，Unicode big endian，或 UTF-8 檔案中的數據。在 Unicode (little endian)，檔案的第一個位元是 FF，第二個位元是 FE。在 Unicode big endian 中，檔案的第一個位元是 FE，第二個位元是 FF。在 UTF-8 中，檔案的第一個位元是 EF，第二個位元是 BB，第三個位元是 BF。