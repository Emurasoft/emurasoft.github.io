# Editor\_SetMultiSel

複数選択が利用可能な場合、指定する選択の情報を設定します。このインライン関数を使うか、または [EE\_SET\_MULTI\_SEL](../message/ee_set_multi_sel) メッセージを直接送ることができます。

Editor\_SetMultiSel( HWND hwnd, UINT\_PTR iSel, const SEL\_INFO\* pSelInfo );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iSel_

> 情報を設定する選択のインデックスを指定します。

_pSelInfo_

> [SEL\_INFO 構造体](../structure/sel_info) へのポインタを指定します。

## 戻り値

> 指定した選択に関する情報を設定したら TRUE を返します。選択が複数選択モードでない場合、またはエラーが発生すると、FALSE を返します。
