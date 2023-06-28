# ExecuteMacro 方法

执行一个指定的宏。

#### \[JavaScript\]

_nResult_ = editor. **ExecuteMacro**( _strMacroFileName_, _nFlags_ );

#### \[VBScript\]

_nResult_ = editor. **ExecuteMacro**( _strMacroFileName_, _nFlags_ )

## 参数

_strMacroFileName_

指定宏文件名。

_nFlags_

指定下列值的组合。

|     |     |
| --- | --- |
| eeRunFile | _strMacroFileName_ 参数指定宏文件的路径以及文件名。 |
| eeRunText | _strMacroFileName_ 参数指定内存上的宏文本。 |
| eeMacroLangJScript | 宏代码是 JScript。 |
| eeMacroLangV8 | 宏是 V8。 |
| eeMacroLangVBScript | 宏代码是 VBScript。 |
| eeMacroSyncOnly | 同步执行宏。 |

## 返回值

不使用返回值。

## 版本

支持 EmEditor 17.0 或之后的版本。