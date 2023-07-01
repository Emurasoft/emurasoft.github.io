# Q. Windows のコントロール パネルのプログラムの追加と削除から、EmEditor の古いバージョンをアンインストールすることができません。どうしたらどうしたらアンインストールできますか?

EmEditor の古いバージョンをアンインストールすることができない場合、古いバージョンのインストーラーを "/L\*V log.txt" オプションを付けて実行してください。すると、アンインストールのログ ファイルが作成されます。例えば、インストーラーが "emed64\_14.3.1.exe" なら、次を実行します。

emed64\_14.3.1.exe **/L\*V log.txt**

log.txt ファイルは、インストーラーが停止した理由について、役に立つ情報が含まれている可能性があります。

注意: 古いバージョンのインストーラーが見つからない場合には、C:\\ProgramData\\Emurasoft\\EmEditor\\updates\\update... フォルダに見つかる場合があります。

古いバージョンのアンインストール中に、次のいずれかのダイアログ ボックスが表示された場合:

「選択した機能は現在使用できないネットワークリソースにあります。」

または、

「The feature you are trying to use is on a CD-ROM or other removal disk that is not available. Insert the 'EmEditor Professional (...)' disk and click OK.」

まず、古いバージョンのインストーラーを見つけます。インストーラーのファイル名のファイル拡張子が .exe の場合、"/extract" オプションを付けて解凍します。例えば、インストーラーのファイル名が "emed64\_14.3.1.exe" の場合、以下を実行します。

emed64\_14.3.1.exe **/extract**

インストーラーを "/extract" オプションを付けて実行すると、ファイルの中身と共にサブ フォルダが作成されます。その中に、".msi" というファイル拡張子のファイルが含まれています。この場合、"emed64\_14.3.1 **.msi**" になります。

アンインストール時に、上のダイアログ ボックスが表示された場合、参照ボタンを押して、上の .msi ファイルを指定します。アンインストールを継続すると、古いバージョンをアンインストールすることができます。

どの .msi ファイルが必要かわからない場合、log.txt ファイルを表示すると、情報が見つかることがあります。

または、 [GeekUninstaller (フリーウェア)](http://www.geekuninstaller.com/)、または [Revo Uninstaller (フリーウェア)](http://www.revouninstaller.com/revo_uninstaller_free_download.html) をダウンロードして実行すると、不要なアプリケーションの項目が削除できます。

さらにサポートが必要な場合、詳細な情報を添えて、 [tech@emurasoft.com](mailto:tech@emurasoft.com) 宛のサポートまで log.txt をメールでお送りください。
