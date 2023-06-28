# RUN\_MACRO\_INFO

[EE\_RUN\_MACRO](../message/ee_run_macro) メッセージで使用します。

typedef struct \_RUN\_MACRO\_INFO {

size\_t cbSize;

LPCWSTR pszMacroFile;

LPCWSTR pszText;

UINT nFlags;

int nDefMacroLang;

POINT\_PTR ptOrgPos;

POINT\_PTR ptCodePos;

POINT\_PTR ptErrorPos;

HGLOBAL hstrResult;

} RUN\_MACRO\_INFO;

## フィールド

_cbSize_

> このデータ構造体のバイトのサイズ。 [EE\_RUN\_MACRO](../message/ee_run_macro) メッセージを送る前にこのメンバーを sizeof( RUN\_MACRO\_INFO ) に設定します。

_pszMacroFile_

> 起動したいマクロ ファイルのパスとファイル名を指定します。

_pszText_

> 起動したいメモリのマクロ テキストを指定します。

_nFlags_

> 次の値のいずれかを指定します。
>
> |     |     |
> | --- | --- |
> | RUN\_FILE | pszMacroFile パラメータは有効です。 |
> | RUN\_TEXT | pszText パラメータは有効です。 |

_nDefMacroLang_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | MACRO\_LANG\_JSCRIPT | マクロは JScript です。 |
> | MACRO\_LANG\_V8 | マクロは V8 です。 |
> | MACRO\_LANG\_VBSCRIPT | マクロは VBScript です。 |
> | MACRO\_LANG\_UNKNOWN | マクロ言語は不明です。 |
> | MACRO\_SYNC\_ONLY | マクロを同期実行します。 |

_ptOrgPos_

> マクロの既定位置を指定します。

_ptCodePos_

> マクロのコード位置を指定します。

_ptErrorPos_

> マクロのエラー位置を指定します。

_hstrResult_

> 出力。マクロが戻る出力の文字列へのハンドルを受信します。発信者は GlobalFree 機能を使用して、このハンドルをフリーにすることができます。

## バージョン

> Version 9.00 以上で利用できます。