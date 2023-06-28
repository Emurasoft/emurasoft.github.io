# Q. タスクバー上のトレイ アイコンを自分の好きなアイコンに変更できますか?

はい、できます。レジストリ
エディタ(RegEdit.exe)を実行し、HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common
を検索してください。TrayIconFile という値を REG\_SZ で作成し、アイコンファイルのパスを指定し、TrayIconIndex という値を REG\_DWORD で作成し、アイコンのインデックスを指定してください。