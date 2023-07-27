# EP\_DISABLE\_AUTO\_COMPLETE

かっこ/引用符機能の自動完了を無効にするかどうかを尋ねます。この機能は、設定プロパティの [\[強調(2)\] タブ](../../dlg/properties/highlight2/index) にある\[対応するかっこを強調する\] チェック ボックスによって定義されます。

EP\_DISABLE\_AUTO\_COMPLETE

hwnd = hwndParent;

wParam = 0;

lParam = 0;

## パラメータ

_hwndParent_

プラグイン設定用ダイアログボックスのウィンドウ ハンドルが格納されています。

## 戻り値

自動完了機能が無効なら TRUE を、有効なら FALSE を返します。

## バージョン

Version 9.00 以上で利用できます。
