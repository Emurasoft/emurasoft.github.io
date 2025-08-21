# 外部ツールの定義例

-  インターネット エクスプローラを開く

\[コマンド\] C:\\Program Files\\Internet Explorer\\iexplore.exe

\[引数\] $(Path)

\[初期ディレクトリ\] $(Dir)

\[アイコン パス\] C:\\Program Files\\Internet Explorer\\iexplore.exe

\[ファイルを保存\] をチェック

- エクスプローラを開く

\[コマンド\] %WinDir%\\explorer.exe

\[引数\] $(Dir)

\[初期ディレクトリ\] $(Dir)

\[アイコン パス\] %WinDir%\\explorer.exe

- コマンド プロンプトを開く

\[コマンド\] %WinDir%\\system32\\cmd.exe

\[引数\] $(Dir)

\[初期ディレクトリ\] $(Dir)

\[アイコン パス\] %WinDir%\\system32\\cmd.exe

- Visual C++ でコンパイル

\[コマンド\] %WinDir%\\system32\\cmd.exe

\[引数\] /k "C:\\Program Files\\Visual Studio\\Vc7\\bin\\vcvars32.bat"&&cl $(Path)

\[初期ディレクトリ\] $(Dir)

\[アイコン パス\] C:\\Program Files\\Visual Studio\\Common7\\IDE\\devenv.exe

\[ファイルを保存\] をチェック

- 関連付けられたファイルを実行

\[コマンド\] $(Path)

\[引数\]

\[初期ディレクトリ\] $(Dir)

\[アイコン パス\]

\[ファイルを保存\] をチェック

- Google でカーソル位置の単語 (または選択した文字列) を検索

\[コマンド\] http://google.com/search?ie=Shift\_JIS&q=$(CurText)

\[引数\]

\[初期ディレクトリ\]

\[アイコン パス\]

- Microsoft Visual SourceSafe からチェック アウトする

\[コマンド\] %WinDir%\\system32\\cmd.exe

\[引数\] /k C:\\(SourceSafe のパス)\\Common\\VSS\\win32\\SS.EXE checkout
$/(パス)/$(Filename).$(Ext) -y(ユーザー名)

\[初期ディレクトリ\] $(Dir)

\[アイコン パス\] C:\\(SourceSafe のパス)\\Common\\VSS\\win32\\SSEXP.EXE

- Microsoft Visual SourceSafe にチェック インする

\[コマンド\] %WinDir%\\system32\\cmd.exe

\[引数\] /k C:\\(SourceSafe のパス)\\Common\\VSS\\win32\\SS.EXE checkin
$/(パス)/$(Filename).$(Ext) -y(ユーザー名)

\[初期ディレクトリ\] $(Dir)

\[アイコン パス\] C:\\(SourceSafe のパス)\\Common\\VSS\\win32\\SSEXP.EXE

\[ファイルを保存\] をチェック

\[コマンド\]、\[引数\]、\[初期ディレクトリ\]、\[アイコン パス\] には、次のあらかじめ定義された引数を使うことができます。

$(Path) ファイルの完全パス名

$(Dir) ファイルのディレクトリ名

$(Filename) 拡張子を除くファイル名

$(Ext) ファイルの拡張子

$(CurLine) カーソル位置の論理行番号

$(CurText) テキストが選択されている場合は選択した文字列、選択されていない場合はカーソル位置の単語

その他、%WinDir% などの環境変数が利用できます。
