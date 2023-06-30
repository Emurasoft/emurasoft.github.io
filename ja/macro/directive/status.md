# \#status 指示子 ()

現在のマクロの状態 (マクロが有効かどうか、チェックされた状態かどうか) が ID によって指定されたコマンドの真似をすることを指定します。この指示子は、スクリプトのメイン コードの上の最初の行に指定する必要があります。

#status = _id_

## パラメータ

_id_

> 状態を調べるのに使用するコマンド ID の整数値を指定します。この値は、 [QueryStatusByID メソッド](../editor/editor_querystatusbyid) の _nID_ パラメータと同等です。

## 例

このマクロは \[自動コピー\] コマンド (ID = 3979) の真似をします。自動コピー機能がオンの時、マクロ メニューとツール バーのボタンがチェックされます。自動コピー機能がオフの時、マクロ メニューとツール バーのボタンがチェックされません。

#### \[JavaScript\]

#status = 3979

editor.ExecuteCommandByID(3979);   // 3979 = EEID\_AUTO\_COPY

#### \[VBScript\]

#status = 3979

editor.ExecuteCommandByID 3979   ' 3979 = EEID\_AUTO\_COPY

## バージョン

EmEditor Professional Version 16.4 以上で利用できます。