# プラグインへのメッセージ

| メッセージ | 説明 |
| --- | --- |
| [EP\_DISABLE\_AUTO\_COMPLETE](ep_disable_auto_complete) | かっこ/引用符機能の自動完了を無効にするかどうかを尋ねます。 |
| [EP\_GET\_BITMAP](ep_get_bitmap) | ツールバーに表示される様々なサイズと色数のプラグイン ボタンのビットマップのリソースIDを取得します。 |
| [EP\_GET\_INFO](ep_get_info) | プラグインに関するさまざまな情報を取得します。(Version 5.00 以上で対応) |
| [EP\_GET\_MASK](ep_get_mask) | ツールバーに表示されるプラグイン ボタンのマスク カラーを取得します |
| [EP\_GET\_NAME](ep_get_name) | プラグインの名前を取得します。 |
| [EP\_GET\_VERSION](ep_get_version) | プラグインのバージョンを取得します。 |
| [EP\_QUERY\_PROPERTIES](ep_query_properties) | プロパティが利用可能かどうかを調べます。 |
| [EP\_QUERY\_UNINSTALL](ep_query_uninstall) | アンインストールが利用可能かどうかを調べます。 |
| [EP\_SET\_PROPERTIES](ep_set_properties) | プロパティの表示を指示します。 |
| [EP\_SET\_UNINSTALL](ep_set_uninstall) | アンインストールを実行します。 |
| [EP\_PRE\_TRANSLATE\_MSG](ep_pre_translate_msg) | Windows メッセージを変換する前に呼び出されます。 |
| [EP\_USE\_DROPPED\_FILES](ep_use_dropped_files) | プラグインがドロップされたファイルを使用したいかどうかを取得します。 |
| [EP\_USER\_MSG](ep_user_msg) | プラグインへユーザー定義メッセージを送信します。 |
| [EP\_SYNC\_NOW](ep_sync_now) | 同期機能がサポートされていれば、プラグインへ今すぐ同期するように指示します。 |

これらのメッセージは、 [プラグインのエクスポート関数 PlugInProc](../exports/index)
で利用されます。

これらの定数は、ヘッダ (plugin.h) で定義されています。

```{toctree}
:maxdepth: 1
ep_disable_auto_complete
ep_get_bitmap
ep_get_info
ep_get_mask
ep_get_name
ep_get_version
ep_pre_translate_msg
ep_query_properties
ep_query_uninstall
ep_set_properties
ep_set_uninstall
ep_sync_now
ep_use_dropped_files
ep_user_msg
```
