# EE\_SET\_MODIFIED

文書が更新されているかどうかのフラグを設定します。このメッセージを直接送るか、または
[Editor\_SetModified インライン関数](../macro/editor_setmodified) を使うことができます。

EE\_SET\_MODIFIED

wParam = (WPARAM) (BOOL) bModified;

lParam = 0;

## パラメータ

_bModified_

更新されている状態にするには TRUE を、更新されていない状態にするには FALSE を指定します。

## 戻り値

戻り値は利用されません。
