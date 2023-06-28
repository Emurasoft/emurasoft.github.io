# 選択した文字列を取得する

選択した文字列を取得するには、 [Text プロパティ](../selection/selection_text) を利用します。

この例では、選択した文字列を取得して表示します。

#### \[JavaScript\]

str = document.selection.Text;

alert( str );

#### \[VBScript\]

str = document.selection.Text

alert str