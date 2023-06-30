# ExecuteMacro メソッド ()

指定するマクロを実行します。

#### \[JavaScript\]

editor. **ExecuteMacro**( _strMacroFileName_ \[, _nFlags_ \] );

#### \[VBScript\]

editor. **ExecuteMacro** _strMacroFileName_ \[, _nFlags_ \]

## パラメータ

_strMacroFileName_

起動したいマクロ ファイルのパスとファイル名、またはメモリのマクロ テキストを指定します。

_nFlags_

次の値の組み合わせを指定します。省略すると、 _strMacroFileName_ パラメータは、マクロ ファイルのパスとファイル名を指定し、マクロの種類はファイルの拡張子より検出されます。

|     |     |
| --- | --- |
| eeRunFile | _strMacroFileName_ パラメータは、マクロ ファイルのパスとファイル名を指定します。 |
| eeRunText | _strMacroFileName_ パラメータは、メモリのマクロ テキストを指定します。 |
| eeMacroLangJScript | マクロは JScript です。 |
| eeMacroLangV8 | マクロは V8 です。 |
| eeMacroLangVBScript | マクロは VBScript です。 |
| eeMacroSyncOnly | マクロを同期実行します。 |

## 戻り値

戻り値は使用されません。

## 例

#### \[JavaScript\]

editor.ExecuteMacro( "E:\\\Macros\\\Macro.jsee", eeRunFile \| eeMacroLangJScript );

editor.ExecuteMacro( "alert('Hello')", eeRunText \| eeMacroLangJScript );

#### \[VBScript\]

editor.ExecuteMacro "E:\\Macros\\Macro.jsee", eeRunFile Or eeMacroLangJScript

editor.ExecuteMacro "alert('Hello')", eeRunText Or eeMacroLangJScript

## バージョン

EmEditor Professional Version 17.0 以上で利用できます。