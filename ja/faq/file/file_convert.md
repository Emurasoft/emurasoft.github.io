# Q. コマンド ラインでエンコードを変換するには?

次のコマンド ライン オプションを使用します。

/cp Encoding --- 開く時のエンコードを指定します。

/cps Encoding --- 保存時のエンコードを指定します。

/sa "DestFile" --- エンコード変換後のファイル名を指定します。

/ss+ --- エンコード変換後 Unicode サイン (BOM) を付けて保存します。

/ss- --- エンコード変換後 Unicode サイン (BOM) を付けないで保存します。

例えば、日本語 Shift-JIS のファイルを UTF-8 に変換するには、次の構文を使用します。

emeditor.exe "shift-jis.txt" /cp 932 /cps 65001 /ss- /sa "utf8.txt"

## 参照

[エンコード一覧](../../macro/const/const_encoding)

[コマンドライン オプション](../../howto/file/file_commandline)
