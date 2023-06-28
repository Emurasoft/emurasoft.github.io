# \#status 指示詞

指定目前的巨集的狀態（是否啟用巨集以及是否勾選）應該模擬由 ID 指定的命令。 巨集功能表以及巨集工具列根據這個指定的命令狀態更新巨集狀態。 此指示詞必須在腳本的第一行，即主程式碼上面指定。

#status = _id_

## 參數

_id_

> 指定用於查詢狀態的命令 ID 的整數值。 此值等同于 QueryStatusByID 方法的 _nID_ 參數。

## 示例

該巨集模擬自動復制命令 (ID = 3979)。當啟用自動復制功能時，會選中巨集功能表和工具列上的按鈕。當關閉自動復制功能時，不會選中巨集功能表和工具列上的按鈕。

#### \[JavaScript\]

#status = 3979

editor.ExecuteCommandByID(3979);   // 3979 = EEID\_AUTO\_COPY

#### \[VBScript\]

#status = 3979

editor.ExecuteCommandByID 3979   ' 3979 = EEID\_AUTO\_COPY

## 版本

支持 EmEditor Professional Version 16.4 或之後的版本。