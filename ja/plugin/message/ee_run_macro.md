# EE\_RUN\_MACRO

マクロを起動します。このメッセージを直接送るか、または [Editor\_RunMacro](../macro/editor_runmacro) インライン関数を使うことができます。

EE\_RUN\_MACRO

wParam = 0;

lParam = (LPARAM) (RUN\_MACRO\_INFO\*) pRMI;

## パラメータ

_pRMI_

> [RUN\_MACRO\_INFO](../structure/run_macro_info) 構造体へのポインタです。

## 戻り値

> 次のうちのいずれかを指定します。
>
> |     |     |
> | --- | --- |
> | S\_OK | 成功。 |
> | S\_FALSE | 構文エラーが発生したようなマクロエラー。 |
> | S\_EDIT\_TEMP | マクロエラーが発生しました。ソース コードはテキストファイルではないため、編集するためのソース コードを開くことができません。発信者は ptErrorPos パラメータが提供する情報を参照し、カーソル位置を設定してソース ファイルを開いてください。 |
> | E\_FAIL | 致命的なエラーが発生しました。 |

## バージョン

> Version 9.00 以上で利用できます。