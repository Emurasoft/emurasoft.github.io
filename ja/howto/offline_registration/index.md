# オフライン登録

[\[製品登録\] ダイアログ ボックス](../../dlg/regist/index) での製品登録には、インターネット接続が必要です。

オンライン登録中に「Request error: sending request for url…No such host is known.」というエラーメッセージが表示された場合、システムがインターネットアクセスに特定のプロキシ設定を必要とする場合があります。[プロキシのカスタマイズ](../../dlg/customize/proxy/index)でそれらを設定できます。

インターネット接続なしで EmEditor に登録したい場合は、オフライン登録機能を使用できます。オフライン登録には、EmEditor v24.4.2 以降が必要です。

オフライン登録では、登録時にライセンス ファイルを使用します。ライセンス ファイルはメールでお客様に送付されます。オフラインライセンスを使用して EmEditor を登録する手順は以下の通りです。

1. [お問い合わせフォーム](https://jp.emeditor.com/support/#contact) を使用してライセンス ファイルをリクエストしてください。フォームには、[エムソフト カスタマー センター](https://support.emeditor.com/)で使用されているメール アドレスを指定してください。登録キーまたは [Stripe サブスクリプションID](https://support.emeditor.com/ja/account/subscriptions) を含めてください。
2. リクエストに対する返信メールにライセンス ファイルが添付されます。ライセンス ファイルを管理者権限が不要なローカル ディスクのフォルダーにダウンロードしてください。
3. EmEditorをまだインストールしていない場合は、EmEditorをインストールしてください。インストール時に[`REGKEY`](https://jp.emeditor.com/faq/%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab-faq/%e3%83%80%e3%82%a4%e3%82%a2%e3%83%ad%e3%82%b0-%e3%83%9c%e3%83%83%e3%82%af%e3%82%b9%e3%82%92%e8%a1%a8%e7%a4%ba%e3%81%9b%e3%81%9a%e3%81%ab-emeditor-%e3%81%ae%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc/)オプションを追加する必要はありません。
4. すでに EmEditor を登録している場合は、[登録情報](../../dlg/registration_info/index) を使用して登録を解除してください。
5. EmEditor を閉じます。[コマンド ライン オプション](https://www.emeditor.org/en/howto/file/file_commandline.html#options) `/ol "licenseFilePath"` を使用します。`licenseFilePath` はライセンス ファイルの完全パスです。以下はコマンドの例です。

```
EmEditor.exe /ol "C:\Users\Example\emeditorLicenseFile-a7PT7Au3TOelfK1w.txt"
```

- EmEditorをコンピュータごとに登録するには、`/ol`の代わりに`/ola`を使用できます (管理者権限が必要です)。

6. EmEditor を起動し、[登録情報](../../dlg/registration_info/index)を表示してオフライン登録が成功したことを確認します。ライセンス ファイルはもう必要ないので削除して構いません。

- サブスクリプションを更新した後、オフラインライセンスで再登録する必要はありません。

## 技術情報

オフライン登録の内部詳細については、[こちら](https://www.emeditor.com/general/new-validation-syst)を参照してください。
