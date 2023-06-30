# \#language 指令 (�ű�ָ��)

指定要使用的脚本语言。通过指定这个，你就可以使用 JavaScript 和 VBScript 之外的 ActiveScript 语言。这个指令必须在脚本的第一行，即主代码上面指定。

#language = "ScriptName"

## 参数

_ScriptName_

> 通过 ProgID 指定脚本语言。这个脚本引擎必须在脚本被使用前安装。

## 示例

用不同的脚本语言，插入 "Hello!" 到光标位置处。

#### \[JavaScript (JScript)\]

#language = "JScript"

document.write( "Hello!" );

#### \[JavaScript (V8)\]

#language = "V8"

document.write( "Hello!" );

#### \[PerlScript\]

#language = "PerlScript"

$Window->document->write( 'Hello!' );

#### \[PHPScript\]

#language = "PHPScript"

$Window->document->write( "Hello!" );

#### \[Python\]

#language = "Python"

Window.document.write( 'Hello' );

#### \[RubyScript\]

#language = "RubyScript"

Window.document.write( "Hello!" );

#### \[VBScript\]

#language = "VBScript"

document.write "Hello!";

如果你想要用上述语言之外的另一种语言，请运行注册表编辑器 (regedit.exe) 并搜索键值 {F0B7A1A2-9847-11CF-8F20-00805F2CD064}。如果被搜索的键在你想要的脚本语言下，你就能找到那个语言的 ProgID。

## 备注

如果 JavaScript 和 VBScript 之外的脚本语言被使用，宏的常数则（以 "ee" 开始）不会被定义。要使用这些常数，你必须把这些常数指定为整数值。你能检查这些值，例如，用 JavaScript 运行下面的一行:

alert( eeEncodingSystemDefault );

这些常数值可能以后会被更改。

如果用 JavaScript 和 VBScript 之外的脚本语言的话，宏就不能被自动录制。我们也无法提供有关如何编写 JavaScript 和 VBScript 之外的脚本语言的方法。

## 版本

支持 EmEditor 6.00 或之后的版本。