# EP\_GET\_INFO

プラグインに関するさまざまな情報を取得します。

EP\_GET\_INFO

hwnd = hwndParent;

wParam = flag;

lParam = 0;

## パラメータ

_hwndParent_

> EmEditor のフレームのウィンドウ ハンドルが格納されています。

_flag_

> 取得する情報の種類が指定されます。次の値のいずれかになります。EPGI\_ALLOW\_OPEN\_SAME\_GROUP と EPGI\_ALLOW\_MULTIPLE\_INSTANCES 以外の戻り値は、EmEditor Version 5.00 では使用されませんが、将来のバージョンで使用される可能性があります。
>
> | 定数 | 説明 |
> | --- | --- |
> | EPGI\_ALLOW\_OPEN\_SAME\_GROUP | ファイルを同じグループ内で開くことを許す場合に TRUE を返します。 |
> | EPGI\_ALLOW\_MULTIPLE\_INSTANCES | プラグインが複数インスタンスをサポートする場合に TRUE を返します。プラグインが 2 個以上のフレームで同時に動作することが許される場合には、このメッセージは TRUE を返す必要があります。複数インスタンスが実行している間、グローバル変数は共有されることに注意してください。 |
> | EPGI\_MAX\_EE\_VERSION | 対応するもっとも新しい EmEditor のバージョン番号 \* 1000 を返します。 |
> | EPGI\_MIN\_EE\_VERSION | 対応するもっとも古い EmEditor のバージョン番号 \* 1000 を返します。 |
> | EPGI\_SUPPORT\_EE\_PRO | EmEditor Professional をサポートする場合に TRUE を返します。 |
> | EPGI\_SUPPORT\_EE\_STD | EmEditor Standard をサポートする場合に TRUE を返します。 |

## 戻り値

> Tlag によって返す値が異なります。

## バージョン

> Version 5.00 以上で利用できます。
