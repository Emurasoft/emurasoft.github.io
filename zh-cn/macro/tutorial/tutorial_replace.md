# 替换一个字符串 (�̳�)

要替换一个字符串，添加第九行到我们所示范的宏中:

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

document.selection.CharLeft( false, 12 );

document.selection.DeleteLeft( 15 );

document.selection.CharRight( true, 9 );

document.selection.ChangeCase( eeCaseUpperCase );

if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!"
);

n = document.selection.Replace( "editor", "######", eeReplaceAll );

alert( n + " strings found!" );

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

document.selection.CharLeft False, 12

document.selection.DeleteLeft 15

document.selection.CharRight True, 9

document.selection.ChangeCase eeCaseLowerCase

If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"

n = document.selection.Replace( "editor", "######", eeReplaceAll )

alert n & " strings found!"

保存该宏并在一个新的 EmEditor 窗口中运行它。注意两个"editor" 字符串已经被不区分大小写地搜索了，并且被 "######" 所替换，还有一个消息框会显示 " Two strings found!" 。

[Replace 方法](../selection/selection_replace) 的第一个参数指定要搜索的字符串，第二个参数指定要替换为的字符串，第三个参数指定标志的组合。该方法返回字符串被替换的次数。如果你指定 eeReplaceAll 在第三个参数中，该方法会立即替换字符串并且可能会返回大于 1 的一个数字。有关第三个参数的标志，详见 [Replace 方法](../selection/selection_replace) 的参数说明。

通常在 [Replace 方法](../selection/selection_replace)，与 [Find 方法](../selection/selection_find) 相同，不会终止执行一个宏当没有找到搜索字符串。但是，有一个例外。如果你用 **宏** 菜单下的 [**使用临时选项运行** 命令](../../cmd/macros/macro_run_options)，并在弹出的 [**宏临时选项** 对话框](../../dlg/macro_temp_options/index) 中勾选了 **搜索失败即停止** 复选框，那么宏就会被终止当没有找到搜索字符串时。详见教程中的 [查找一个字符串](tutorial_find)。