# \[検索\] ダイアログ ボックス

このダイアログ ボックスは、 [\[検索\] コマンド](../../cmd/search/edit_find) を実行すると表示されます。ここで指定する文字列とオプションで検索します。

## \[検索する文字列\] ドロップダウン リスト ボックス

検索する文字列を指定します。複数行テキスト ボックスの場合、Ctrl + Enter キーを使用して改行コードを挿入することができます。ドロップダウン リストが表示されている間に、Alt + Delete キーを押すことにより、選択した履歴の項目をクリアすることができます。

## \[>\] ボタン

このボタンをクリックすると、利用可能なコマンドの一覧が表示されます。

|     |     |
| --- | --- |
| **選択テキストまたはカーソル位置の単語** | これがチェックされていると、テキストが選択されていれば選択テキストで、そうでなければカーソル位置の単語で \[検索する文字列\] ドロップダウン リスト ボックスを初期化します。 |
| **選択テキスト** | これがチェックされていると、選択されたテキストで \[検索する文字列\] ドロップダウン リスト ボックスを初期化します。 |
| **カーソル位置の単語** | これがチェックされていると、カーソル位置の単語で \[検索する文字列\] ドロップダウン リスト ボックスを初期化します。 |
| **最後に使った値** | これがチェックされていると、最後に使用した文字列で \[検索する文字列\] ドロップダウン リスト ボックスを初期化します。 |
| **固定値** | これがチェックされていると、固定値で \[検索する文字列\] ドロップダウン リスト ボックスを初期化します。 |
| **既定として保存** | 次回ダイアログ ボックスが表示されたときの既定値として、このオプション (選択テキスト、カーソル位置の単語、最後に使った値、固定値) を保存します。 |
| **複数行** | ドロップダウン リスト ボックスの単一行と複数行を切り替えます。 |
| **エディタのフォントを使用** | これがチェックされていると、\[検索する文字列\] ドロップダウン リスト ボックスにエディタと同じフォントを使用します。 |
| **自動強調** | これがチェックされていると、\[検索する文字列\] ドロップダウン リスト ボックスにタイプするにつれて自動的に一致する文字列を強調表示します。ダイアログ ボックスを閉じると強調表示が無効になります。このオプションは \[検索\] ツール バーにも影響します。 |
| **連続の一覧から選択** | 連続の一覧で定義した文字列を選択します。 |

コマンドには、利用できる正規表現、またはエスケープ シーケンスの一覧が含まれることがあります。その中から項目を選択すると、その内容が、隣のテキスト ボックスに挿入されます。

## \[大文字と小文字を区別する\] チェック ボックス

検索する文字列の大文字と小文字を区別して検索します。

## \[単語のみ検索する\] チェック ボックス

単語のみ検索します。単語のみというのは、置換前の文字列の前後が、A～Z、a～z、0～9、\_
のいずれの文字でも囲まれていない場合のことです。全角文字で囲まれている場合は常に単語とみなされます。正規表現の場合、このチェック ボックスを使用すると正しく検索できない場合があります。正規表現を使用する場合は、これをチェックせずに、単語の区切り表現 (\\<、\\>、\\b) を使用してください。

## \[インクリメンタル サーチ\] チェック ボックス

これがチェックされていると、 \[検索\] ドロップダウン リスト ボックスに文字を入力すると同時に検索を開始します。

## \[グループのすべての文書から検索\] チェック ボックス

同じフレーム ウィンドウ内に開いているすべての文書から検索します。

## \[選択した範囲のみ\] チェック ボックス

選択された文書のみを対象とします。

## \[折り返しあり\] チェック ボックス

下方向の検索の時は、ファイルの最後まで検索しても見つからない場合にファイルの先頭から検索を続けます。上方向の検索の時は、ファイルの先頭まで検索しても見つからない場合にファイルの最後から検索を続けます。

## \[一致する文字列を数える\] チェック ボックス

これがチェックされていると、EmEditor は、文書内の一致した文字列の数を数えて、結果をステータス バーに表示します。リスト ボックスにリンク ファイルが含まれている場合で、\[次を複数検索\] または \[前を複数検索\] ボタンを選択する場合、このオプションは無視されます。

## \[終了したら閉じる\] チェック ボックス

検索を終了したらダイアログ ボックスを閉じます。

## \[(無し)\] ラジオ ボタン

文字列が文字通り一致するべきであることを指定します。

## \[正規表現\] ラジオ ボタン

[正規表現](../../howto/search/search_regexp) を有効にします。

## \[エスケープ シーケンス\] ラジオ ボタン

エスケープ シーケンスを有効にします。エスケープ シーケンスとして次の文字を表現できます。

|     |     |
| --- | --- |
| **\\a** | 警告 (ベル) |
| **\\b** | バックスペース |
| **\\f** | 改頁 |
| **\\n** | 改行 |
| **\\t** | 水平タブ |
| **\\v** | 垂直タブ |
| **\\\\** | 円記号 (バックスラッシュ) |
| **\\oooooo** | 8 進数表記による Unicode 文字 |
| **\\xhhhh** | 16 進数表記による Unicode 文字 |

ヌル文字 (\\0) は使えません。\\r の代わりに \\n を使用します。

## \[数値範囲\] ラジオ ボタン

[数値範囲](../../howto/search/number_range_syntax) を有効にします。

## \[前を検索\] ボタン

現在位置から前に検索します。

## \[次を検索\] ボタン

現在位置から次に検索します。

## \[すべてを選択\] ボタン

一致するすべての文字列を検索して選択します。

## \[ブックマーク\] ボタン

指定文字列に一致するすべての行にブックマークを設定します。

## \[抽出\] ボタン

文書を新規作成して、指定文字列に一致するすべての行を抽出します。右側の ▼ ボタンをクリックすると、コンテキスト メニューが表示され、 [\[抽出オプション\] ダイアログ ボックス](../extract_options/index) にアクセスすることができます。

## \[置換 >>\] ボタン

このボタンをクリックすると、検索文字列や各オプションをそのまま保存し、現在のダイアログ ボックスを閉じて、 [\[置換\] ダイアログ ボックス](../replace/index) に切り替わります。

## \[閉じる\] ボタン

このダイアログ ボックスを閉じます。

## \[高度\] ボタン

これをクリックすると、 [\[高度\] ダイアログ ボックス](../advanced/index) を表示し、高度なオプションを指定できるようになります。

さらに、このダイアログ ボックスから、次のダイアログ ボックスに移動することもできます。

## \[連続へ追加\] ボタン

現在の設定を連続一覧に追加します。

## \[連続 >>\] ボタン

このボタンをクリックして、\[検索\] ダイアログ ボックスと \[連続検索\] ダイアログ
ボックスを切り替えます。

次のコントロールは、ダイアログ ボックスが \[連続検索\] ダイアログ ボックスに拡張されたときのみ表示されます。

## \[連続へ保存\] ボタン

現在の設定を連続一覧に保存します。

## リスト ボックス

連続検索で使用する検索の一覧を表示します。条件の列には次の省略文字が使用されます。

|     |     |
| --- | --- |
| C | 大文字と小文字を区別する |
| R | 正規表現を使用する |
| W | 単語のみ検索する |
| E | CSVの埋め込み改行コードのみを検索する |
| S | CRとLFを区別する |
| D | 正規表現「.」が改行コードに一致することができる |
| B | Boost.Regexを正規表現エンジンとして使用する |
| O | Onigmoを正規表現エンジンとして使用する |

## \[すべて有効/無効にする\] チェック ボックス

一覧のすべての項目の有効と無効を切り替えます。

## \[インポート\] ボタン

以前に TSV 形式でエクスポートされた検索条件を含むファイルをインポートします。

## \[エクスポート\] ボタン

定義された検索条件をファイルにエクスポートします。TSV 形式以外に、JavaScript または VBScript のマクロ形式でエクスポートすることもできます。

## \[前を複数検索\] ボタン

現在位置から前に複数の選択項目を検索します。

## \[次を複数検索\] ボタン

現在位置から次に複数の選択項目を検索します。

## \[連続ブックマーク\] ボタン

連続一覧から選択項目に一致するすべての行にブックマークを設定します。

## \[連続抽出\] ボタン

文書を新規作成して、連続一覧から選択項目に一致するすべての行を抽出します。右側の ▼ ボタンをクリックすると、コンテキスト メニューが表示され、 [\[連続オプション\] ダイアログ ボックス](../batch_options/index) にアクセスすることができます。

## \[すべてフィルター\] ボタン

連続一覧から選択項目に一致するすべての行をフィルターします。

## \[フィルター中止\] ボタン

フィルターを中止します。

## \[<< 連続\] ボタン

このボタンをクリックして、\[連続検索\] ダイアログ ボックスと \[検索\] ダイアログ
ボックスを切り替えます。

このダイアログ ボックスは右下をマウスでドラッグすると、サイズを変更することができます。複数行で入力できる状態のとき、Ctrl + Enter キーを使用して改行コードを挿入することができます。

さらに、このダイアログ ボックスから、次のダイアログ ボックスに移動することもできます。

[\[高度\] ダイアログ ボックス](../advanced/index) (\[高度\] ボタンを選択)

[\[抽出オプション\] ダイアログ ボックス](../extract_options/index) (\[抽出オプション\] を選択)

[\[連続オプション\] ダイアログ ボックス](../batch_options/index) (\[連続オプション\] を選択)

