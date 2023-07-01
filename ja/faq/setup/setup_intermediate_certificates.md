# Q. プログラム ファイルのデジタル署名が確認できません (インターネット接続が利用できない場合)。

インターネット接続が利用できない PC で EmEditor を実行すると、次のような問題が発生することがあります。

- EmEditor を実行しようとすると、「プログラム ファイルのデジタル署名が確認できません。」という警告メッセージが表示される。
- emeditor.exe や .msi インストーラーなどの EmEditor ファイルのデジタル署名が確認できない。
- EmEditor の起動が遅い。

このような場合、EmEditor を実行するか、プログラム ファイルのデジタル署名を確認する間、インターネットに接続してください。一度インターネットに接続すれば、その後は切断していても問題は発生しません。

もし、インターネットに接続することができない場合、次のステップにしたがって Sectigo コード署名中間証明機関の証明書をインストールしてください。

1. インターネットに接続された PC より、 ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false) に接続します。
2. "Code Signing" セクションの "Standard Sectigo RSA Cod Signing CA" をダウンロードします。
3. ダウンロードしたファイルを EmEditor ファイルの存在するコピー先の PC にコピーします。
4. コピー先の PCで、このファイルを右クリックし、\[証明書のインストール\] を選択すると、\[証明書のインポート ウィザード\] が表示されます。
5. ウィザードの指示に従い、\[証明書をすべて次のストアに配置する\] を選択し、\[参照\] ボタンをクリックし、\[中間証明機関\] を選択します。\[次へ\] をクリックして、証明書をインポートします。

emeditor.exe などの EmEditor ファイルのデジタル署名に問題がないことを確認します。もし、ルート証明書が確認できないために問題がある場合には、次のステップにしたがって Sectigo ルート証明機関の証明書をインストールしてください。

1. インターネットに接続された PC より、 ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false) に接続します。
2. "Root Certificates" セクションの "SHA-2 Root: USERTrust RSA Certification Authority" をダウンロードします。
3. ダウンロードしたファイルを EmEditor ファイルの存在するコピー先の PC にコピーします。
4. コピー先の PCで、このファイルを右クリックし、\[証明書のインストール\] を選択すると、\[証明書のインポート ウィザード\] が表示されます。
5. ウィザードの指示に従い、\[証明書をすべて次のストアに配置する\] を選択し、\[参照\] ボタンをクリックし、\[信頼されたルート証明機関\] を選択します。\[次へ\] をクリックして、証明書をインポートします。

また、Windows のグループ ポリシーの編集で、 [ルート証明書の自動更新をオフ](https://admx.help/?Category=Windows_7_2008R2&Policy=Microsoft.Policies.InternetCommunicationManagement::CertMgr_DisableAutoRootUpdates&Language=ja-jp) にするにより、この問題を解決したという報告がありました。
