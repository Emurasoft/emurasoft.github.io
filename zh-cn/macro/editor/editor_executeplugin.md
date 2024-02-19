# ExecutePlugin 方法 (Editor 对象)

执行一个指定的插件。

## 

### \[JavaScript\]

```
nResult = editor.ExecutePlugin( strPluginFileName, nFlags, nParam, strParam );
```

### \[VBScript\]

```
nResult = editor.ExecutePlugin( strPluginFileName, nFlags, nParam, strParam )
```

## 参数

_strPluginFileName_

指定插件文件名。

_nFlags_

指定下列值的组合。不能同时指定 eePluginExecuteCommand，eePluginUserMessage，和 eePluginQueryStatus。

|     |     |
| --- | --- |
| eePluginExecuteCommand | 像用户选择插件命令一样运行插件。指定此参数时，将忽略 nParam 和 strParam 参数。 |
| eePluginUserMessage | 使用 nParam 和 strParam 参数向插件发送消息。 |
| eePluginQueryStatus | 检索插件状态。指定此参数时，将忽略 nParam 和 strParam 参数。 |
| eePluginAbsolutePath | strPluginFileName 包含文件的完整路径。如果未指定此标志，则插件必须存在于默认插件文件夹中，该文件夹是 EmEditor 安装文件夹中的 PlugIns 子文件夹。 |

_nParam_

指定要发送到插件的整数参数。参数的含义取决于每个插件。如果省略，则 0 会被指定。

_strParam_

指定要发送到插件的字符串参数。参数的含义取决于每个插件。如果省略，则空字符串会被指定。

## 返回值

返回值为负值如果发生错误的话。否则，如果指定了 eePluginExecuteCommand，则返回值为0。如果指定了 eePluginUserMessage，则返回值的含义取决于每个插件。如果指定了eePluginQueryStatus，则该方法会返回以下值的组合。

|     |     |
| --- | --- |
| eeStatusEnabled | 插件已启用。 |
| eeStatusLatched | 插件已检查。 |

## 示例

### \[JavaScript\]

```
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0" );
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 1, "General\\\\Date");
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 2, "/General/Date" );
```

### \[VBScript\]

```
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0"
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 1, "General" & Chr(92) & "Date"
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 2, "/General/Date"
```

## 版本

支持 EmEditor 15.5 或之后的版本。
