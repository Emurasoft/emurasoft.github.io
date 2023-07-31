# Shell オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [ForegroundWindow](foreground_window) | 現在のフォアグラウンド ウィンドウを取得します。 |
| [windows](windows) | トップ レベルの Windows コレクションを返します。 |

## メソッド

|     |     |
| --- | --- |
| [CreateFolder](create_folder) | フォルダを作成します。 |
| [DeleteFile](delete_file) | 指定するファイルを削除します。 |
| [DeleteFolder](delete_folder) | 指定するフォルダとその中身を削除します。指定したフォルダが空でなくも削除されます。 |
| [FileExists](file_exists) | 指定するファイルが存在すれば true を、存在しなければ false を返します。 |
| [FindWindow](find_window) | クラス名またはウィンドウ タイトルでトップ レベルの Window オブジェクトを検索します。 |
| [FolderExists](folder_exists) | 指定するフォルダが存在すれば true を、存在しなければ false を返します。 |
| [GetFileAttributes](get_file_attributes) | 指定するファイルまたはフォルダの属性を返します。 |
| [Run](run) | 新規プロセスでプログラムを実行します。 |
| [SendKeys](send_keys) | アクティブなウィンドウにキー ストローク (またはマウス アクティビティ) を送ります。 |
| [SetFileAttributes](set_file_attributes) | 指定するファイルまたはフォルダの属性を設定します。 |

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。


```{toctree}
:hidden:
:maxdepth: 1
create_folder
delete_file
delete_folder
file_exists
find_window
folder_exists
foreground_window
get_file_attributes
run
send_keys
set_file_attributes
windows
```
