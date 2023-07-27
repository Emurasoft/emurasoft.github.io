# EmEditor Professional と EmEditor Standard の両方の新機能 (EmEditor v3.37 からの新機能)

## 新しいコマンド

- [\[常に最上位 \- オン\] コマンド](../cmd/window/window_always_top_on)
- [\[常に最上位 \- オフ\] コマンド](../cmd/window/window_always_top_off)

## 新オプションが追加された既存のダイアログ ボックス

- [\[カスタマイズ\] ダイアログ ボックス](../dlg/customize/index)
- [設定のプロパティ](../dlg/properties/index) の [\[ファイル\] タブ](../dlg/properties/file/index)

## その他の新機能

- [\[ファイルから検索\] コマンド](../cmd/search/grep) を実行中に、途中でキャンセルできるようになりました。
- 正規表現を使った [\[ファイルから検索\] コマンド](../cmd/search/grep) でマルチ
バイト文字が利用できるようになりました。
- 正規表現を使用した検索が高速になりました。
- 他の EmEditor の検索方法を見直し、EmEditor の起動が早くなりました。
- 各ダイアログ ボックスに\[ヘルプ\] ボタンを追加し、ダイアログ
ボックスについてのヘルプが表示できるようになりました。
- ヘルプを充実し、 [コマンド リファレンス](../cmd/index) や [よくある質問と回答集](../faq/index) を含む詳細なヘルプを閲覧できるようになりました。
- Windows 2000/XP/2003 版では、コア部分だけでなくダイアログ ボックスなどでも内部のコードがほとんどすべて Unicode
対応になりました。
- [コマンド ライン](../howto/file/file_commandline) のオプションに、/?
を追加しました。
- 既定では、文字列を挿入してから [\[元に戻す\] コマンド](../cmd/edit/edit_undo) を実行すると、挿入した文字列が一度に戻るようになりました。この動作は、 [\[カスタマイズ\] ダイアログ](../dlg/customize/index) の [\[高度\] タブ](../dlg/customize/advanced/index) の\[文字単位で元に戻す
(EmEditorを再起動する必要あり)\] チェック ボックスをチェックすることにより、以前の動作に戻ります。
- 補足説明ファイル (emeditor.txt) を廃止し、ヘルプにすべての情報を統合しました。
- プラグイン開発用に新しいメッセージ [EE\_SET\_SEL\_TYPE](../plugin/message/ee_set_sel_type)、 [EE\_GET\_STATUSA](../plugin/message/ee_get_statusa)、 [EE\_GET\_STATUSW](../plugin/message/ee_get_statusw)、 [EE\_INSERT\_FILEA](../plugin/message/ee_insert_filea)、 [EE\_INSERT\_FILEW](../plugin/message/ee_insert_filew)、 [EE\_GET\_ANCHOR\_POS](../plugin/message/ee_get_anchor_pos)、 [EE\_SET\_ANCHOR\_POS](../plugin/message/ee_set_anchor_pos)
を追加し、 [EE\_INSERT\_STRINGA](../plugin/message/ee_insert_stringa)、 [EE\_INSERT\_STRINGW](../plugin/message/ee_insert_stringw)、 [EE\_GET\_VERSION](../plugin/message/ee_get_version)、 [EE\_INFO](../plugin/message/ee_info)、 [EE\_SET\_CARET\_POS](../plugin/message/ee_set_caret_pos)
メッセージの機能を拡張しました。
