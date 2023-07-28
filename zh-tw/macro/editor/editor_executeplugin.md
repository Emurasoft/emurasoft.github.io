# ExecutePlugin 方法 (Editor 對象)

執行一個指定的外掛程式。

## 

### \[JavaScript\]

```
nResult = editor.ExecutePlugin( strPluginFileName, nFlags, nParam, strParam );
```

### \[VBScript\]

```
nResult = editor.ExecutePlugin( strPluginFileName, nFlags, nParam, strParam )
```

## 參數

_strPluginFileName_

指定外掛程式檔案名。

_nFlags_

指定下列值的組合。不能同時指定 eePluginExecuteCommand，eePluginUserMessage，和 eePluginQueryStatus。

|     |     |
| --- | --- |
| eePluginExecuteCommand | 像使用者選擇外掛程式命令一樣運行外掛程式。指定此參數時，將忽略 nParam 和 strParam 參數。 |
| eePluginUserMessage | 使用 nParam 和 strParam 參數向外掛程式發送消息。 |
| eePluginQueryStatus | 檢索外掛程式狀態。指定此參數時，將忽略 nParam 和 strParam 參數。 |
| eePluginAbsolutePath | strPluginFileName 包含檔案的完整路徑。如果未指定此標志，則外掛程式必須存在于預設外掛程式資料夾中，即 EmEditor 安裝資料夾中的 PlugIns 子資料夾。 |

_nParam_

指定要發送到外掛程式的整數參數。參數的含義取決于每個外掛程式。如果省略，則 0 會被指定。

_strParam_

指定要發送到外掛程式的字串參數。參數的含義取決于每個外掛程式。如果省略，則空字串會被指定。

## 返回值

返回值為負值如果發生錯誤的話。否則，如果指定了 eePluginExecuteCommand，則返回值為0。如果指定了 eePluginUserMessage，則返回值的含義取決于每個外掛程式。如果指定了eePluginQueryStatus，則該方法會返回以下值的組合。

|     |     |
| --- | --- |
| eeStatusEnabled | 外掛程式已啟用。 |
| eeStatusLatched | 外掛程式已檢查。 |

## 範例

### \[JavaScript\]

```
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0" );
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 1, "General\\\Date");
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 2, "/General/Date" );
```

### \[VBScript\]

```
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0"
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 1, "General" & Chr(92) & "Date"
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 2, "/General/Date"
```

## 版本

支持 EmEditor 15.5 或之後的版本。
