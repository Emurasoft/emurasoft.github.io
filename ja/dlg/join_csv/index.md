# \[CSV の結合\] ダイアログ ボックス

このダイアログ ボックスは、 [\[CSVの結合\] コマンド](../../cmd/csv/join_csv) を実行するか、ツール バーで \[CSVの結合\] ボタンをクリックすると表示されます。

## \[CSV 文書 1\] ドロップダウン リスト ボックス

第1文書を選択します。

## \[CSV 文書 2\] ドロップダウン リスト ボックス

第2文書を選択します。これら 2 個の CSV 文書は、各文書に共通のキー列の値を使用して結合されます。

## \[Key1/Key2 列\] ドロップダウン リスト ボックス

キー列を選択します。

## \[一意キー\] チェック ボックス

キー列の各行が異なる値を含んでいる場合、キー列は一意キー列になり、このチェック ボックスを設定することにより、結合の操作の速度を最適化します。

## \[一致しない行を含める\] チェック ボックス

結合する時、マッチしないすべての行を含めます。これは、両方のチェック ボックスが設定されていれば、SQL における OUTER JOIN に相当し、左のチェック ボックスだけが設定されていれば、LEFT JOIN に相当し、右のチェック ボックスだけが設定されていれば、RIGHT JOIN に相当し、両方ともチェックされていなければ INNER JOIN に相当します。

## \[ヘディングを無視する\] チェック ボックス

これがチェックされていると、ヘディングを無視します。元のヘディングは結合された文書に保持されます。

## \[条件\] ドロップ ダウン リスト ボックス

条件を選択します。

## \[大文字と小文字を区別\] テキスト ボックス

これがチェックされていると、大文字小文字を区別して比較します。

## \[区切り\] テキスト ボックス

\[条件\] ドロップ ダウン リスト ボックスで \[両方の分割文字列が一致\]、\[Key1 は分割した Key2 に一致\]、\[Key2 は分割した Key1 に一致\] のいずれかが選択されている場合、文字列を分割するのに使用する区切り文字列を指定します。

## \[分割数を制限\] チェック ボックス、テキスト ボックス

分割の最大数を指定します。

## \[CSV 文書/列\] リスト ボックス

この一覧には、両方の文書のすべての列が含まれています。出力に含めたい列のみチェックしたり、出力の列の順番を変更することができます。

## \[すべて有効/無効にする\] チェック ボックス

このチェック ボックスを使用して一覧のすべての項目の有効と無効を切り替えることができます。

## \[上へ\] ボタン

一覧の選択項目を上へ移動します。

## \[下へ\] ボタン

一覧の選択項目を下へ移動します。

## \[前の列と結合する\] ラジオ ボタン

このボタンがチェックされていると、EmEditor は現在の列をその前の列と結合します。

## \[連結する\] ラジオ ボタン

このボタンがチェックされていると、EmEditor は現在の列をその前の列と連結します。

## \[最初の空でない値を使用する\] ラジオ ボタン

このボタンがチェックされていると、EmEditorは最初の空でない値を使用して、現在の列をその前の列と連結します。

## \[エクスポート\] ボタン

現在の設定を JavaScript または VBScript マクロ ファイルにエクスポートします。エクスポートされたマクロ ファイルは、同じ操作を実行する時に使用することができます。

## \[今すぐ結合\] ボタン

CSV 文書の結合を開始します。

