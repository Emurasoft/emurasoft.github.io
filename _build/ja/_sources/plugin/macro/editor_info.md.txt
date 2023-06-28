# Editor\_Info

実行中の EmEditor または現在アクティブなドキュメントに関する情報を取得または設定を行います。このインライン関数を使うか、または
[EE\_INFO メッセージ](../message/ee_info) を直接送ることができます。

Editor\_Info( HWND hwnd, int nCmd, LPARAM lParam );

## パラメータ

_nCmd_

> 取得または設定する情報の種類を指定します。指定できるコマンドの一覧は、 [EE\_INFO メッセージ](../message/ee_info) を参照してください。

_lParam_

> nCmd によって意味が異なります。

## 戻り値

> nCmd によって意味が異なります。

## バージョン

> Version 3.00 以上で利用できます。