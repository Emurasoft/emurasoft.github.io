# EE\_GET\_LINES

テキスト全体の行数を取得します。このメッセージを直接送るか、または [Editor\_DocGetLines インライン関数](../macro/editor_docgetlines) または [Editor\_GetLines インライン関数](../macro/editor_getlines) を使うことができます。

EE\_QUERY\_STATUS

wParam = (WPARAM) MAKEWPARAM(nLogical, iDoc+1);

lParam = hDoc;

## パラメータ

_nLogical_

> 次のうちのいずれかを指定します。
>
> | 定数 | 説明 |
> | --- | --- |
> | POS\_VIEW | 表示座標 |
> | POS\_LOGICAL\_A | 論理座標 (2バイト文字を 2 と数えます) |
> | POS\_LOGICAL\_W | 論理座標 (2バイト文字を 1 と数えます) |

_iDoc_

> 操作対象のドキュメントのインデックスを指定します。wParamの上位ワードには、1 を基底とするインデックスを指定します。 wParam の上位ワードに 0 を指定すると、現在アクティブなドキュメントが操作対象になります。

_hDoc_

> 省略可能。対象となるドキュメントへのハンドルを指定します。このパラメータを指定する場合、iDoc は 0 である必要があります。

## 戻り値

> 文書全体の行数を返します。最終行が改行コードで終わる場合、最終行も含まれます。空の場合は 1 を返します。
