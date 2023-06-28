# Editor\_DocInfoEx

実行中の EmEditor または指定するドキュメントに関する情報を取得または設定を行います。このインライン関数を使うか、または
[EE\_INFO\_EX メッセージ](../message/ee_info_ex) を直接送ることができます。

Editor\_DocInfoEx( HWND hwnd, HEEDOC hDoc, UINT nCmd, LPARAM lParam );

## パラメータ

_nCmd_

> 取得または設定する情報の種類を指定します。指定できるコマンドの一覧は、 [EE\_INFO メッセージ](../message/ee_info) を参照してください。

_hDoc_

> 操作対象のドキュメントへのハンドルを指定します。NULL を指定すると、現在アクティブなドキュメントが操作対象になります。 _nCmd_ によっては、このフィールドは使用されないこともあります。

_lParam_

> _nCmd_ によって意味が異なります。

## 戻り値

> _nCmd_ によって意味が異なります。

## バージョン

> Version 21.8 以上で利用できます。