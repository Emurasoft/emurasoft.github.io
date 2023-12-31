# Q. インストール先フォルダを変更するには?

既定では、インストール先フォルダは、以前のバージョンが既にインストールされている場合はそのフォルダになり、新しいインストールの場合は、ユーザー毎インストールの場合 %LocalAppData%\\Programs\\EmEditor になり、コンピューター全体インストールの場合 \\Program Files\\EmEditor になります。管理者権限でコマンドプロンプトを開いて、インストーラを NOSKIP オプションを付けて実行することにより、インストール先フォルダを変更することが可能です。

たとえば、EmEditor のセットアップ用のファイルが emed64\_18.9.3.msi で、異なるフォルダにインストールしたい場合、

msiexec /i emed64\_18.9.3.msi NOSKIP=1

を実行します。すると、インストールの途中で、「カスタム」を選択する画面が現れます。そこで「カスタム」を選択すると、インストール先フォルダを変更することができます。

注意: EmEditor がユーザー毎にインストールされている場合は、インストール先フォルダを変更することができません。インストール先フォルダを変更するには、すべてのユーザーにインストールする必要があります。

異なるバージョンの EmEditor を同時にインストールすることはできません。以前のバージョンの EmEditor が既にインストールされている場合は、以前のバージョンをアンインストールしてから新しいバージョンをインストールするか、以前のバージョンがインストールされているフォルダ上に上書きインストールしてください。
