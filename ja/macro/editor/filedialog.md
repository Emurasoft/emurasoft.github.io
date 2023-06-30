# FileDialog メソッド ()

ファイルを開く、または名前を付けて保存ダイアログ ボックスを表示して、開くファイルのドライブ、ディレクトリ、名前を指定します。

#### \[JavaScript\]

_strFileName_ = editor. **FileDialog**( _nType_ \[, _nFlags_ \[, _strTitle_ \[, _strFilter_ \[, _nDefFilterIndex_ \[, _strDefPath_ \[, _strDefFolder_ \[, _strDefExt_ \]\]\]\]\]\]\] );

#### \[VBScript\]

_strFileName_ = editor. **FileDialog**( _nType_ \[, _nFlags_ \[, _strTitle_ \[, _strFilter_ \[, _nDefFilterIndex_ \[, _strDefPath_ \[, _strDefFolder_ \[, _strDefExt_ \]\]\]\]\]\]\] )

## パラメータ

_nType_

以下の値のいずれかの値を指定します。

|     |     |
| --- | --- |
| eeFileDialogOpen | ファイルを開くダイアログ ボックスを作成します。 |
| eeFileDialogSaveAs | 名前を付けて保存ダイアログ ボックスを作成します。 |

_nFlags_

省略可能。次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeFileDialogCreatePrompt | ユーザーが存在しないファイルを指定すると、ファイルを作成するかどうかを確認するプロンプト メッセージが表示されます。 |
| eeFileDialogDontAddToRecent | 最近使用した文書を含むシステム ディレクトリへのリンクの作成を防ぎます。 |
| eeFileDialogFileMustExist | \[ファイル名\] フィールドには、既存のファイル名のみを入力することができることを指定します。これが指定されているときにユーザーが不正なファイル名を入力すると、警告メッセージ ボックスが表示されます。このフラグを指定する場合は、eeFileDialogPathMustExist フラグも同時に指定する必要があります。 |
| eeFileDialogNoChangeDir | ユーザーがファイルを探すためにディレクトリを変更しても、現在のディレクトリを復元します。 |
| eeFileDialogNoDereferenceLinks | 選択されたショートカット (.LNK) ファイルのパスとファイル名を返します。このフラグが指定されていない場合、ショートカットで参照されたファイルのパスとファイルを返します。 |
| eeFileDialogNoNetworkButton | \[ネットワーク\] ボタンを非表示にします。 |
| eeFileDialogNoReadOnlyReturn | 返されるファイルが書き換え禁止属性でなく、書き換え禁止ディレクトリの中のファイルではないことを指定します。 |
| eeFileDialogNoTestFileCreate | ダイアログ ボックスが閉じられる前にファイルが作成されないことを指定します。 |
| eeFileDialogNoValidate | 返されるファイル名に不正な文字が許可されることを指定します。 |
| eeFileDialogOverwritePrompt | 名前を付けて保存ダイアログ ボックスで、既存のファイル名を指定するとメッセージ ボックスが表示されることを指定します。 |
| eeFileDialogPathMustExist | ユーザーが正しいパスとファイル名のみを入力できることを指定します。 |
| eeFileDialogShareAware | ネットワーク共有違反で関数が失敗しても、エラーが無視され選択されたファイルが返されることを指定します。 |

_strTitle_

省略可能。ダイアログ ボックスのタイトルを指定します。空の文字列を指定すると、既定のタイトル (\[ファイルを開く\] または \[名前を付けて保存\]) が使用されます。

_strFilter_

省略可能。フィルタを指定します。文字列は次の形式である必要があります。

"Text Files\|\*.txt\|All Files\|\*.\*\|\|"

空の文字列が指定されると、フィルタは使用されません。

_nDefFilterIndex_

省略可能。初期状態で選択されるフィルタを 1 を基底とするインデックスで指定します。

_strDefPath_

省略可能。初期状態で選択されるパスを指定します。

_strDefFolder_

省略可能。初期状態で選択されるフォルダを指定します。

_strDefExt_

省略可能。既定のファイル拡張子を指定します。

## 戻り値

成功すると選択されたファイルの完全パスと名前を返します。ユーザーがキャンセルをクリックすると空の文字列を返します 。

## バージョン

EmEditor Professional Version 8.00 以上で利用できます。