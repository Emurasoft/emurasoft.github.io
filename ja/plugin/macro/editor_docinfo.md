# Editor\_DocInfo

実行中の EmEditor または指定するドキュメントに関する情報を取得または設定を行います。このインライン関数を使うか、または
[EE\_INFO メッセージ](../message/ee_info) を直接送ることができます。

Editor\_DocInfo( HWND hwnd, int iDoc, int nCmd, LPARAM lParam );

## パラメータ

_nCmd_

> 取得または設定する情報の種類を指定します。指定できるコマンドの一覧は、 [EE\_INFO メッセージ](../message/ee_info) を参照してください。

_iDoc_

> 操作対象のドキュメントの 0 を基底とするインデックスを指定します。-1 を指定すると、現在アクティブなドキュメントが操作対象になります。

_lParam_

> nCmd によって意味が異なります。

## 戻り値

> nCmd によって意味が異なります。

## バージョン

> Version 5.00 以上で利用できます。