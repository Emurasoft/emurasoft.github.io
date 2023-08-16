# INFO\_EX\_DATA

[EE\_INFO\_EX メッセージ](../message/ee_info_ex) で使用します。

typedef struct \_INFO\_EX\_DATA {

UINT cbSize;

UINT nCmd;

HEEDOC hDoc;

LPARAM lParam;

} INFO\_EX\_DATA;

## フィールド

_cbSize_

sizeof( INFO\_EX\_DATA ) を指定します。

_nCmd_

取得または設定する情報の種類を指定します。指定できるコマンドの一覧は、 [EE\_INFO メッセージ](../message/ee_info) を参照してください。

_hDoc_

操作対象のドキュメントへのハンドルを指定します。NULL を指定すると、現在アクティブなドキュメントが操作対象になります。 _nCmd_ によっては、このフィールドは使用されないこともあります。

_lParam_

_nCmd_ によって意味が異なります。
