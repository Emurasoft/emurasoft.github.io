# ExecuteMacro Method (Editor Object)

Executes a specified macro.

## 

### \[JavaScript\]

```
nResult = editor.ExecuteMacro( strMacroFileName, nFlags );
```

### \[VBScript\]

```
nResult = editor.ExecuteMacro( strMacroFileName, nFlags )
```

## Parameters

_strMacroFileName_

Specifies the path and file name of the macro file you want to run, or a macro text on memory that you want to run.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeRunFile | The _strMacroFileName_ parameter specifies the path and file name of the macro file. |
| eeRunText | The _strMacroFileName_ parameter specifies a macro text on memory. |
| eeMacroLangJScript | The macro is JScript. |
| eeMacroLangV8 | The macro is V8. |
| eeMacroLangVBScript | The macro is VBScript. |
| eeMacroSyncOnly | Executes the macro synchronously. |

## Return Values

The return value is not used.

## Examples

### \[JavaScript\]

```
editor.ExecuteMacro( "E:\\\Macros\\\Macro.jsee", eeRunFile \| eeMacroLangJScript );
editor.ExecuteMacro( "alert('Hello')", eeRunText \| eeMacroLangJScript );
```

### \[VBScript\]

```
editor.ExecuteMacro "E:\\Macros\\Macro.jsee", eeRunFile Or eeMacroLangJScript
editor.ExecuteMacro "alert('Hello')", eeRunText Or eeMacroLangJScript
```

## Version

Supported on EmEditor Professional Version 17.0 or later.
