# Run 方法 (Shell ����)

在新进程中运行程序。

#### \[JavaScript\]

nReturnCode = shell. **Run**( _strCommand_, _nWindowStyle_, _bWaitOnReturn_, _strParameter_, _strFolder_ );

#### \[VBScript\]

nReturnCode = shell. **Run**( _strCommand_, _nWindowStyle_, _bWaitOnReturn_, _strParameter_, _strFolder_ )

## 参数

_strCommand_

指定命令。通常，这是程序文件的完整路径和名称。

_nWindowStyle_

指定一个整数值，指示程序窗口的外观。该参数可以省略。此参数可以是以下值之一。

|     |     |
| --- | --- |
| 值 | 描述 |
| 1 | 激活并显示一个窗口。如果窗口被最小化或最大化，系统会将其恢复到原来的大小和位置。 |
| 2 | 激活窗口并将其显示为最小化窗口。 |
| 3 | 激活窗口并将其显示为最大化窗口。 |
| 4 | 以最近的大小和位置显示窗口。活动窗口保持活动状态。 |

_bWaitOnReturn_

指定一个布尔值（'true' 或 'false'），指示脚本是否应等待程序完成执行后再继续执行脚本中的下一条语句。该参数可以省略。

_strParameter_

指定要作为命令行的参数。该参数可以省略。

_strFolder_

指定初始目录。该参数可以省略。

## 示例

#### \[JavaScript\]

nAttr = shell.Run( "C:\\\Windows\\\calc.exe", 1 );

#### \[VBScript\]

nAttr = shell.Run( "C:\\Test\\file.txt" )

## 返回值

如果 _bWaitOnReturn_ 为 true，则返回程序的返回代码。如果 _bWaitOnReturn_ 为 false，则不使用返回值。

## 版本

支持 EmEditor Professional 22.1 或之后的版本。