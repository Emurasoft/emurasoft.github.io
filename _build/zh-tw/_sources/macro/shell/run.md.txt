# Run 方法

在新進程中運行程式。

#### \[JavaScript\]

nReturnCode = shell. **Run**( _strCommand_, _nWindowStyle_, _bWaitOnReturn_, _strParameter_, _strFolder_ );

#### \[VBScript\]

nReturnCode = shell. **Run**( _strCommand_, _nWindowStyle_, _bWaitOnReturn_, _strParameter_, _strFolder_ )

## 參數

_strCommand_

指定命令。通常，這是程式檔案的完整路徑和名稱。

_nWindowStyle_

指定一個整數值，指示程式視窗的外觀。該參數可以省略。此參數可以是以下值之一。

|     |     |
| --- | --- |
| 值 | 描述 |
| 1 | 激活並顯示一個視窗。如果視窗被最小化或最大化，系統會將其恢復到原來的大小和位置。 |
| 2 | 激活視窗並將其顯示為最小化視窗。 |
| 3 | 激活視窗並將其顯示為最大化視窗。 |
| 4 | 以最近的大小和位置顯示視窗。活動視窗保持活動狀態。 |

_bWaitOnReturn_

指定一個布林值（'true' 或 'false'），指示腳本是否應等待程式完成執行後再繼續執行腳本中的下一條語句。該參數可以省略。

_strParameter_

指定要作為命令列的參數。該參數可以省略。

_strFolder_

指定初始目錄。該參數可以省略。

## 範例

#### \[JavaScript\]

nAttr = shell.Run( "C:\\\Windows\\\calc.exe", 1 );

#### \[VBScript\]

nAttr = shell.Run( "C:\\Test\\file.txt" )

## 返回值

如果 _bWaitOnReturn_ 為 true，則返回程式的傳回代碼。如果 _bWaitOnReturn_ 為 false，則不使用返回值。

## 版本

支持 EmEditor Professional 22.1 或之後的版本。