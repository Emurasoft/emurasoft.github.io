# Item プロパティ (DisplayList �R���N�V����)

指定のインデックスの [DisplayItem オブジェクト](../display_item/index) を取得します。

#### \[JavaScript\]

_item_ =
list. **Item**( _Index_ );

#### \[VBScript\]

_item_ =
list. **Item**( _Index_ )

## パラメータ

_Index_

アイテムのインデックスを １ から始まる整数として指定します。

オブジェクトが色の一覧の場合、次の値のいずれかになります。

|     |     |
| --- | --- |
| eeColorNormal | 通常 |
| eeColorSelection | 選択状態 |
| eeColorCurrentLine | カーソルのある行 |
| eeColorQuote | 引用マークで始まる行 |
| eeColorURL | URL |
| eeColorMailTo | メール アドレス |
| eeColorTag | ファイルから検索ハイパーリンクを含むタグ |
| eeColorSingleQuotes | 1重引用符で囲まれた文字列 '...' |
| eeColorDoubleQuotes | 2重引用符で囲まれた文字列 "..." |
| eeColorComment | コメント |
| eeColorScript | スクリプト |
| eeColorBraces | 対応するかっこ |
| eeColorInsideTag | HTML/XMLタグ |
| eeColorHighlight1 | 強調文字列(1) |
| eeColorHighlight2 | 強調文字列(2) |
| eeColorHighlight3 | 強調文字列(3) |
| eeColorHighlight4 | 強調文字列(4) |
| eeColorHighlight5 | 強調文字列(5) |
| eeColorHighlight6 | 強調文字列(6) |
| eeColorHighlight7 | 強調文字列(7) |
| eeColorHighlight8 | 強調文字列(8) |
| eeColorHighlight9 | 強調文字列(9) |
| eeColorHighlight10 | 強調文字列(10) |
| eeColorReturn | 改行コード、タブ、EOF |
| eeColorCursorLine | 水平/垂直罫線 |
| eeColorPageBreak | ページ区切り線/部分編集 |
| eeColorLineNumbers | 行番号 (数字) |
| eeColorRuler | ルーラー/列ヘッダー (数字) |
| eeColorOutside | 表示領域の外側 |
| eeColorCompareChange | 比較 \- 変更行 |
| eeColorCompareChar | 比較 \- 変更文字 |
| eeColorCompareAdded | 比較 \- 追加 |
| eeColorCompareDeleted | 比較 \- 削除 |
| eeColorCompareBlank | 比較 \- 空白 |
| eeColorSpell | 不正なスペル |
| eeColorUnicode | Unicode文字 |
| eeColorVerticalSel | 箱型選択枠 |
| eeColorHexSel | 16進数表示の選択枠 |
| eeColorIndentGuides | インデント ガイド |
| eeColorHorzGrid | 水平グリッド |
| eeColorOutline | アウトライン |
| eeColorLineNumberLines | 行番号 (線) |
| eeColorRulerLines | ルーラー/列ヘッダー (線) |
| eeColorVerticalSeparator | 垂直区切り線 |
| eeColorHtmlCharRef | HTML文字参照 |
| eeColorUcn | Universal Character Names/パーセント エンコーディング |
| eeColorAutoMarker | 自動マーカー |
| eeColorMarker1 | マーカー (1) |
| eeColorMarker2 | マーカー (2) |
| eeColorMarker3 | マーカー (3) |
| eeColorMarker4 | マーカー (4) |
| eeColorMarker5 | マーカー (5) |
| eeColorMarker6 | マーカー (6) |
| eeColorMarker7 | マーカー (7) |
| eeColorMarker8 | マーカー (8) |
| eeColorMarker9 | マーカー (9) |
| eeColorMarker10 | マーカー (10) |
| eeColorMatchingTag | 対応タグ |
| eeColorBookmark | ブックマークされた行 |
| eeColorUserDefinedGuides | ユーザー定義ガイド |
| eeColorIndicatorModified | 垂直インジケーター \- 変更行 |
| eeColorIndicatorSaved | 垂直インジケーター \- 保存行 |
| eeColorIndicatorBookmark | 垂直インジケーター \- ブックマーク |
| eeColorMarkerModified | スクロール バー マーカー \- 変更行 |
| eeColorMarkerSaved | スクロール バー マーカー \- 保存行 |
| eeColorMarkerBookmark | スクロール バー マーカー \- ブックマーク |
| eeColorMarkerFound | スクロール バー マーカー \- 検索 |
| eeColorMarkerCursor | スクロール バー マーカー \- カーソル位置 |
| eeColorMarkerCompareChange | スクロール バー マーカー \- 比較 \- 変更行 |
| eeColorMarkerCompareAdded | スクロール バー マーカー \- 比較 \- 追加 |
| eeColorMarkerCompareDeleted | スクロール バー マーカー \- 比較 \- 削除 |
| eeColorHeadings | ヘディング |
| eeColorSearchSel | 選択範囲 |
| eeColorFilter | フィルター |
| eeColorLinkUrlVisited | URL (表示済み) |
| eeColorLinkIdVisited | メール アドレス (表示済み) |
| eeColorLinkTagVisited | ファイルから検索ハイパーリンク (表示済み) |
| eeColorCellText | CSVセル選択テキスト |
| eeColorCellBorder | CSVセル選択枠 |
| eeColorFilterSeparator | フィルター区切り |
| eeColorMinimapBackground | ミニマップ背景 |
| eeColorMinimapView | ミニマップ ビュー |
| eeColorLinkIpv4 | IPv4 アドレス |
| eeColorLinkIpv4Visited | IPv4 アドレス (表示済み) |
| eeColorLinkIpv6 | IPv6 アドレス |
| eeColorLinkIpv6Visited | IPv6 アドレス (表示済み) |
| eeColorHexColor | 16進数表記のカラー コード - #ff0080 |
| eeColorRgbColor | RGB 表記のカラー コード - rgb(255,0,128) |
| eeColorLineNumberHovered | 行番号 (ポイント) |
| eeColorRulerHovered | ルーラー/列ヘッダー (ポイント) |
| eeColorLineNumberSel | 行番号 (行選択) |
| eeColorRulerSel | ルーラー/列ヘッダー (列選択) |
| eeColorLineNumberCurr | 行番号 (選択) |
| eeColorRulerCurr | ルーラー/列ヘッダー (選択) |
| eeColorOpenFilter | 開くフィルター |
| eeColorMultiSelection | 複数選択のある行 |
| eeColorValidatorError | 構文チェックのエラー |
| eeColorValidatorWarning | 構文チェックの警告 |
| eeColorValidatorMessage | 構文チェックのメッセージ |
| eeColorEvenLines | 偶数行 |
| eeColorInvalidCharacters | 警告すべき文字 |

オブジェクトが検索の一覧の場合、検索の回数が指定されます。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。