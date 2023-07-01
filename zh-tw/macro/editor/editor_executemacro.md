# ExecuteMacro 方法 (Editor ��H)

執行一個指定的巨集。

#### \[JavaScript\]

_nResult_ = editor. **ExecuteMacro**( _strMacroFileName_, _nFlags_ );

#### \[VBScript\]

_nResult_ = editor. **ExecuteMacro**( _strMacroFileName_, _nFlags_ )

## 參數

_strMacroFileName_

指定巨集檔案名。

_nFlags_

指定下列值的組合。

|     |     |
| --- | --- |
| eeRunFile | _strMacroFileName_ 參數指定巨集檔案的路徑以及檔案名。 |
| eeRunText | _strMacroFileName_ 參數指定記憶體上的巨集文字。 |
| eeMacroLangJScript | 巨集程式碼是 JScript。 |
| eeMacroLangV8 | 巨集是 V8。 |
| eeMacroLangVBScript | 巨集程式碼是 VBScript。 |
| eeMacroSyncOnly | 同步執行巨集。 |

## 返回值

不使用返回值。

## 版本

支持 EmEditor 17.0 或之後的版本。
