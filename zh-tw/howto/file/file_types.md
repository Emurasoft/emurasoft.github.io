# 支持的檔案類型

EmEditor 能打開并編輯文字檔案，用 Unicode，Unicode big endian，UTF-8，UTF-7，波羅的海文，中歐，簡體中文，繁體中文，西里爾文，希臘文，日文 (Shift-JIS)，日文 (EUC)，韓文，泰文，土耳其文，越南文，西歐文，或任何其他在 Windows 上可用的編碼。

如果您使用的是 Windows 2000/XP/2003/Vista 系統，請到控制面板上的 **「區域和語言選項」** 中，選擇「語言」頁面，在 **附加語言支持** 下勾選額外的語言。您還可以到 **「進階」** 頁面上的 **代碼頁轉換表** 下勾選您想要使用的編碼。。

您想要使用的編碼可以在**自訂**對話方塊的[**檔案編碼**頁面](../../dlg/customize/encodings/index)中新增。

換行標記可以是僅僅歸位符 (CR)，換行符 (LF)，或歸位和換行符 (CR+LF)。

## 備注

- 您能編輯 Unicode 文字檔案，但是對于書寫方式是從右到左的語言，例如阿拉伯語以及希伯來語，被編輯時可能出現失誤。不是所有的 Uniocode 控制字元都支持。
- 您能編輯 Unicode 文字檔案，但這取決于字型。一些顯示字元沒有被支持。您需要選擇適合您要使用的語言的字型。
- 當一個檔案包含 [空字元](../../glossary/nullcharacter) 時， [空字元](../../glossary/nullcharacter) 會被轉換成空白。
