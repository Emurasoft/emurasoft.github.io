# Editor\_RunMacro

マクロを起動します。このインライン関数を使うか、または [EE\_RUN\_MACRO](../message/ee_run_macro) メッセージを直接送ることができます。

Editor\_RunMacro( HWND _hwnd_, UINT _nFlags_, UINT _nDefMacroLang_, LPCWSTR _pszMacroFile_, LPCWSTR _pszText_, const POINT\_PTR\* _pptOrgPos_, POINT\_PTR\* _pptCodePos_, POINT\_PTR\* _pptErrorPos_, HGLOBAL\* _phstrResult_ );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

次の値のいずれかを指定します。

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile パラメータは有効です。 |
| RUN\_TEXT | pszText パラメータは有効です。 |

_nDefMacroLang_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | マクロは JScript です。 |
| MACRO\_LANG\_V8 | マクロは V8 です。 |
| MACRO\_LANG\_VBSCRIPT | マクロは VBScript です。 |
| MACRO\_LANG\_UNKNOWN | マクロ言語は不明です。 |
| MACRO\_SYNC\_ONLY | マクロを同期実行します。 |

_pszMacroFile_

起動したいマクロ ファイルのパスと名前を指定します。

_pszText_

起動したいメモリのマクロ テキストを指定します。

_pptOrgPos_

マクロの既定位置を指定します。

_pptCodePos_

マクロのコード位置を指定します。

_pptErrorPos_

マクロのエラー位置を受信します。

_phstrResult_

マクロが戻る出力文字列へのハンドルを受信します。発信者が GlobalFree 機能を使用することでこのハンドルをフリーにできます。

## 戻り値

戻り値は下記のいずれかになります。

|     |     |
| --- | --- |
| S\_OK | 成功。 |
| S\_FALSE | 構文エラーが起こったようなマクロ エラーです。 |
| S\_EDIT\_TEMP | マクロ エラーが起こりました。しかし、ソース コードがテキスト ファイルではないため、編集するためにソース コードを開くことができませんでした。発信者は ptErrorPos パラメータが提供している情報を参照し、カーソル位置の設定と同時にソース ファイルを開いてください。 |
| E\_FAIL | 致命的なエラーが起こりました。 |

## バージョン

Version 9.00 以上で利用できます。
