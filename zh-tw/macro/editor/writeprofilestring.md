# WriteProfileString 方法 (Editor 對象)

按 EmEditor 設定，設置一個字串值到注冊表或一個 INI 檔案中。

## 

### \[JavaScript\]

```
editor.WriteProfileString( nKey, strConfig, strEntry, strData [ , nType ] );
```

### \[VBScript\]

```
editor.WriteProfileString nKey, strConfig, strEntry, strData [ , nType ]
```

## 參數

_nKey_

用下列值之一來指定一個機碼。eeRegConfig 和 eeRegEmEditorPlugin 需要 _pszConfig_ 參數來指定機碼。

|     |     |
| --- | --- |
| eeRegCommon | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common or eeCommon.ini\\\[Common\] |
| eeRegRegist | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist or eeCommon.ini\\\[Regist\] |
| eeRegLMCommon | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common or eeLM.ini\\\[Common\] |
| eeRegLMRegist | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist or eeLM.ini\\\[Regist\] |
| eeRegConfig | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) or eeConfig.ini\\\[(pszConfig)\] |
| eeRegEmEditorPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) or eePlugins.ini\\\[(pszConfig)\] |
| eeRegEmEditorUsers | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) or eeUsers.ini\\\[(pszConfig)\] |

_strConfig_

用額外的字串來指定機碼當 eeRegConfig，eeRegEmEditorPlugin，或 eeRegEmEditorUsers 被選取時。

_strEntry_

指定要檢索的值的名稱。

_strData_

指定要存儲的數據。

## 版本

支持 EmEditor 8.00 或之後的版本。
