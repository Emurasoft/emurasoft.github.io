# Run メソッド ()

新規プロセスでプログラムを実行します。

#### \[JavaScript\]

nReturnCode = shell. **Run**( _strCommand_, _nWindowStyle_, _bWaitOnReturn_, _strParameter_, _strFolder_ );

#### \[VBScript\]

nReturnCode = shell. **Run**( _strCommand_, _nWindowStyle_, _bWaitOnReturn_, _strParameter_, _strFolder_ )

## パラメータ

_strCommand_

コマンドを指定します。通常、プログラム ファイルの完全パスと名前になります。

_nWindowStyle_

プログラム ウィンドウの表示方法を指示する整数値を指定します。このパラメータは省略できます。このパラメータは次の値のいずれかになります。

|     |     |
| --- | --- |
| 値 | 説明 |
| 1 | ウィンドウをアクティブにして表示します。ウィンドウが最小化または最大化されている場合、システムは元のサイズと位置に復元します。 |
| 2 | ウィンドウをアクティブにして最小化ウィンドウで表示します。 |
| 3 | ウィンドウをアクティブにして最大化ウィンドウで表示します。 |
| 4 | ウィンドウを最近のサイズと位置で表示します。アクティブなウィンドウはアクティブなまま残ります。 |

_bWaitOnReturn_

スクリプトが、プログラムの終了するの待ってから次のステートメントを実行するかどうかを指定するブーリアン型を指定します。このパラメータは省略できます。

_strParameter_

コマンド ラインとして渡したいパラメータを指定します。このパラメータは省略できます。

_strFolder_

初期のディレクトリを指定します。このパラメータは省略できます。

## 例

#### \[JavaScript\]

nAttr = shell.Run( "C:\\\Windows\\\calc.exe", 1 );

#### \[VBScript\]

nAttr = shell.Run( "C:\\Test\\file.txt" )

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。