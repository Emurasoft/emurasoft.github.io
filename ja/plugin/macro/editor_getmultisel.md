# Editor\_GetMultiSel

複数選択が利用可能な場合、指定する選択の情報を取得します。このインライン関数を使うか、または [EE\_GET\_MULTI\_SEL](../message/ee_get_multi_sel) メッセージを直接送ることができます。

Editor\_GetMultiSel( HWND hwnd, UINT\_PTR iSel, SEL\_INFO\* pSelInfo );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iSel_

情報を取得する選択のインデックスを指定します。-1 を指定すると、選択の個数を返します。

_pSelInfo_

[SEL\_INFO 構造体](../structure/sel_info) へのポインタを指定します。

## 戻り値

iSel に -1 を指定した場合、選択の個数を返します。そうでなければ、指定した選択に関する情報を返したら TRUE を返します。選択が複数選択モードでない場合、またはエラーが発生すると、FALSE を返します。
