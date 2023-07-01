# Q. 怎么用命令列轉換檔案編碼？

您可以參考使用下列的命令列選項:

/cp Encoding --- 設定一個編碼來打開檔案。sets an encoding to open as.

/cps Encoding --- 設定一個編碼來儲存檔案。

/sa "DestFile" --- 指定一個檔案名來另存新檔在轉換編碼後。

/ss+ --- 用 Unicode 簽名 (BOM) 來儲存檔案在轉換編碼後。

/ss- --- 不用 Unicode 簽名 (BOM) 來儲存檔案在轉換編碼後。

例如，如果您想要把一個檔案編碼從 Western European (iso-8859-1) 轉換為UTF-8，可以使用下面的語法:

emeditor.exe "windows1252.txt" /cp 1252 /cps 65001 /ss- /sa "utf8.txt"

又或者，如果您想要把一個檔案，Chinese.txt，從繁體中文( Big5) 轉換成UTF-8，並且想把檔案重新命名為utf8Chinese，您可以使用如下所示的語法:

emeditor.exe 「Chinese.txt」 /cp 950 /cps 65001 /ss- /sa 「utf8Chinese.txt」

請參考 [編碼常數](../../macro/const/const_encoding) 尋找編碼。

請參考 [使用命令列選項](../../howto/file/file_commandline) 獲取更多信息。
