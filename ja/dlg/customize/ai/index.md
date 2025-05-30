# \[AIオプション\] ページ

\[AIオプション\] ページでは、AIに関する設定を行います。

## \[AI を有効にする\] チェック ボックス

[OpenAI](https://openai.com/) を使用した執筆支援を有効にします。本オプションを有効にした後、さらに、各設定のプロパティの [\[AI支援\]](../../properties/ai_assist/index) ページの [AIによる支援執筆] チェック ボックスを設定する必要があります。本機能を使用するには、[OpenAI API キー](https://platform.openai.com/api-keys)が必要です。

## \['OPENAI_API_KEY' 環境変数を使用する\] チェック ボックス

これがチェックされていると、'OPENAI_API_KEY' 環境変数を使用して API キーを保存します。これは、OpenAI で推奨されている保存方法であり、他のアプリでも共有される方法です。これがチェックされていない場合は、EmEditor のみで使用できるように API キーを保存します。

## \[OpenAI API キー\] テキスト ボックス

OpenAI API キーを指定します。このテキスト ボックスの右側の [o-o] をクリックして、文字の表示/非表示を切り替えることができます。本テキスト ボックスを変更して、このダイアログ ボックスの [OK] ボタンをクリックすると、入力した API キーが使用できるかどうかを確認するため、OpenAI API への接続テストを行います。

## \[優先モデル\] ドロップ ダウン リスト ボックス

使用するモデルの名前を指定します。一覧から、既に定義されているモデル名を選択するか、または未定義のモデル名を直接入力することができます。使用するモデルにより、AI の回答が異なったり、OpenAI の利用料金が異なることがあります。未定義のモデル名を指定して、このダイアログ ボックスの [OK] ボタンをクリックすると、使用できるかどうかを確認するため、OpenAI API への接続テストを行います。

## \[AI を無効にする (コンピューター毎)\] ボタン

EmEditor の全ての AI 関連機能、[AI 支援執筆] 機能、AI マクロ、および fetch 関数を使用するその他のマクロを禁止します。このボタンを実行するには管理者権限が必要です。

## \[リセット\] ボタン

設定を既定にします。

## 注

このページは、ChatAI プラグインがインストールされ有効になっている場合だけ、利用可能です。
