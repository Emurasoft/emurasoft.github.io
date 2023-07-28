# 文字列を検索する (チュートリアル)

文字列を検索するために、チュートリアルのマクロに、次のように 8 行目を追加します。

## 

### \[JavaScript\]

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
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseLowerCase
If document.selection.Find( "Em", eeFindPrevious ) Then alert "見つかりました！"
上記のマクロを保存して別の EmEditor ウィンドウで実行すると、"Em" を検索して選択し、メッセージ ボックスで "見つかりました！"
という文字列を表示します。
[Find メソッド](../selection/selectionfind) は、第 1 引数で検索する文字列を指定し、第 2
引数で検索方法のフラグを指定します。この場合は、eeFindPrevious を指定してカーソル位置から上方向に検索しています。 [Find \
メソッド](../selection/selectionfind) は文字列の検索に成功すると、1 を返し、検索した文字列が見つからない場合は 0
を返します。このチュートリアルの例では、文字列が見つかったので、1 を返したため、if 構文の条件が成立し、その後の
[alert メソッド](../window/windowalert) が実行されたのです。 [alert \
メソッド](../window/windowalert) は、引数の文字列を OK ボタン付きの単純なメッセージ ボックスで表示します。この場合は、"見つかりました！" という文字列を表示しています。
[Find メソッド](../selection/selectionfind) を使うと、第 2
引数で、様々なフラグを指定することができます。詳しくは、 [Find メソッド](../selection/selectionfind) の引数の説明を参照してください。
通常、検索した文字列が見つからなくても、マクロの実行が停止することはありませんが、例外として、[マクロ] メニューの [一時オプションを設定して実行]
コマンドで [検索に失敗したら中止] チェック
ボックスをチェックして実行すると、検索した文字列が見つからなかった場合に、マクロの実行が停止されます。これによって、例えば、指定した文字列を検索して他の文字列を挿入するというような操作を何回も繰り返し実行したい場合で、繰り返し回数があらかじめ正確にわからない場合、多めに回数を指定して検索に失敗したら中止するという使い方を、マクロを変更せずに簡単に実行できます。
もし、[一時オプションを設定して実行] コマンドを使用せずに、検索に失敗したら中止したい場合は、マクロを変更する必要があります。 [Find \
メソッド](../selection/selectionfind) の戻り値が 0 の場合にマクロを中止すればいいので、例えば、次のように記述することができます。
```

### \[JavaScript\]

```
if( !document.selection.Find( "xx", eeFindPrevious ) )  throw new
Error("Cannot find xx");
```

### \[VBScript\]

```
If Not document.selection.Find( "xx", eeFindPrevious )  Then Err.Raise
vbObjectError + 1, "Find Error", "Cannot find xx"
さらに、 [FindRepeat メソッド](../selection/selectionfindrepeat) を使うと、前回検索した文字列を再度検索したり、カーソル位置の単語を検索することができます。次のようにフラグを指定して実行すると、該当するキーボードのコマンドに相当する検索を行います。
|     |     |
| --- | --- |
| eeFindRepeatNext | カーソル位置から下方向に前回検索した文字列を再度検索します。F3 に相当。 |
| eeFindRepeatPrevious | カーソル位置から上方向に前回検索した文字列を再度検索します。Shift + F3 に相当。 |
| eeFindRepeatNext + eeFindRepeatWord | カーソル位置から下方向に選択されている文字列、またはカーソル位置の単語を検索します。Ctrl + F3 に相当。 |
| eeFindRepeatPrevious + eeFindRepeatWord | カーソル位置から上方向に選択されている文字列、またはカーソル位置の単語を検索します。Ctrl + Shift + F3 に相当。 |
```

## 次のトピック
