# 文字列を置換する ()

文字列を置換するために、チュートリアルのマクロに、次のように 9 行目と 10 行目を追加します。

## \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
document.selection.ChangeCase( eeCaseUpperCase );
if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "見つかりました！"
);
n = document.selection.Replace( "editor", "######", eeReplaceAll );
alert( n + " 個の文字列が見つかりました！" );
```

## \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseLowerCase
If document.selection.Find( "Em", eeFindPrevious ) Then alert "見つかりました！"
n = document.selection.Replace( "editor", "######", eeReplaceAll )
alert n & " 個の文字列が見つかりました！"
上記のマクロを保存して別の EmEditor ウィンドウで実行すると、大文字と小文字を区別せずに 2 個の "editor" という文字列が
"######" に置き換わり、最後に「2個の文字列が見つかりました！」というメッセージ ボックスが表示されるはずです。
[Replace メソッド](../selection/selectionreplace) は、第 1
引数で検索する文字列を指定し、第 2 引数で置換後の文字列を指定し、第 3 引数で様々なフラグの組み合わせを指定します。戻り値は置換した文字列の数を返します。第
3 引数で、eeReplaceAll を指定した場合は、すべて一度に置換を行うので、戻り値は 1 以上の数値を返すこともあります。第 3
引数で指定できるフラグについて、詳しくは、 [Replace メソッド](../selection/selectionreplace) の引数の説明を参照してください。
[Find メソッド](../selection/selectionfind) の場合と同様、 [Replace \
メソッド](../selection/selectionreplace) の場合も、通常、検索した文字列が見つからなくても、マクロの実行が停止することはありませんが、例外として、[マクロ] メニューの
[[一時オプションを設定して実行] コマンド](../../cmd/macros/macrorunoptions) を選択して、 [[マクロ一時オプション] \
ダイアログ ボックス](../../dlg/macrotempoptions/index) を表示し、[検索に失敗したら中止] チェック ボックスをチェックして実行すると、検索した文字列が見つからなかった場合に、マクロの実行が停止されます。詳しくは、チュートリアルの [文字列を検索する](tutorialfind) を参照してください。
```
