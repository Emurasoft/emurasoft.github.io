# Q. ダイアログ ボックスを表示せずに EmEditor のインストールを行うには?

通常のインストールでは、ダイアログ ボックスが表示され、ユーザーが \[次へ\] ボタンをクリックしたり、オプションを設定する必要があります。しかし、企業や団体などで複数のコンピュータにインストールする場合、インストールの作業をバッチ ファイルやスクリプトで行い、ダイアログ ボックスを表示したくない場合があります。EmEditor は、インストーラに Windows Installer を使用しているため、次のようにして、無人インストールを行うことができます。

たとえば、EmEditor のセットアップ用のファイルが emed64\_20.9.0.msi の場合、

msiexec /i "(...パス...)emed64\_20.9.0.msi" /passive MSIINSTALLPERUSER=1

を実行すると、一切のダイアログ ボックスが表示されず、既定の設定でインストールを行うことができます。既定の設定を変更したい場合、次のオプションを使用することができます。

|     |     |
| --- | --- |
| MSIINSTALLPERUSER=1 | 現在のユーザーだけのユーザー毎インストールを指定します (v20.9 以降で既定)。 |
| MSIINSTALLPERUSER="" | コンピューター毎インストール (全ユーザー インストール) を指定します (v20.8 以前で既定)。 |
| NOCHECKUPDATES=1 | EmEditor の新しいバージョンをインターネットで定期的にチェックすることを無効にします。 |
| NOCONTEXTMENU=1 | エクスプローラのコンテキスト メニューにショートカットを追加することを無効にします。 |
| DESKTOP=1 | デスクトップにショートカットを追加することを有効にします。 |
| NOIEEDITOR=1 | Internet Explorer の HTML エディタ一覧に EmEditor を追加することを無効にします。 |
| NOIEVIEW=1 | Internet Explorer からソース表示で EmEditor を起動することを無効にします。 |
| NOPATH=1 | EmEditor へのパスを PATH 環境変数に追加することを無効にします。 |
| NOSHORTCUT=1 | プログラム メニューにショートカットを追加することを無効にします。 |
| NOSKIP=1 | 更新時でも、カスタム インストールができるように、インストーラーの画面をスキップしません。 |
| NOTRAYICON=1 | タスクバーにトレイ アイコンを追加することを無効にします。 |
| NOTXT=1 | テキスト ファイルの関連付けを無効にします。 |
| REGNAME="name" | 登録ユーザーの名前を入力します。 |
| REGKEY=xxxxxx | 登録キーを入力します。 |

たとえば、登録キーを設定して、現在のユーザーだけが使用できるようにセットアップを実行したい場合は、

msiexec /i emed64\_20.9.0.msi /passive MSIINSTALLPERUSER=1 REGKEY=xxxxx REGNAME="John Doe"

と実行します。また、登録キーを設定して、全ユーザー インストールを行いたい場合には、次のコマンドを実行します。

msiexec /i emed64\_20.9.0.msi /passive MSIINSTALLPERUSER="" REGKEY=xxxxx REGNAME="John Doe"

他にも、Windows Installer にはさまざまなオプションが存在します。詳しくは、コマンド プロンプトで、

msiexec /?

を実行すると、コマンドの一覧が表示されます。

### 注意

EmEditor v20.9 以降を全ユーザーにインストールしたい場合は、MSIINSTALLPERUSER="" を指定する必要があります。EmEditor v20.8 以前を現在のユーザーのみにインストールしたい場合は、MSIINSTALLPERUSER=1 を指定する必要があります。