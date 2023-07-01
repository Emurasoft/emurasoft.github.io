# OutputBar オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [CurrentDirectory](current_directory) | アウトプット バーにカレント ディレクトリを設定します。 |
| [Visible](visible) | アウトプット バーを表示、または非表示にします。 |
| [Text](text) | アウトプット バー内のすべてのテキストを取得します。 |

## メソッド

|     |     |
| --- | --- |
| [Clear](clear) | アウトプット バーの中身をクリアします。 |
| [SetFocus](set_focus) | アウトプット バーにキーボード フォーカスを設定します。 |
| [write](write) | アウトプット バーに文字列を追加します。 |
| [writeln](writeln) | アウトプット バーに文字列と改行コードを追加します。 |

## 例

#### \[JavaScript\]

OutputBar.Clear();

OutputBar.writeln( "Hello!" );

OutputBar.Visible = true;

OutputBar.SetFocus();

#### \[VBScript\]

OutputBar.Clear

OutputBar.writeln "Hello!"

OutputBar.Visible = True

OutputBar.SetFocus

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。


```{toctree}
:maxdepth: 1
clear
current_directory
set_focus
text
visible
write
writeln
```
