# OutputBar 對象

## 屬性

|     |     |
| --- | --- |
| **[CurrentDirectory](current_directory)** | 為輸出列設置當前目錄。 |
| **[Visible](visible)** | 顯示或隱藏輸出列。 |
| **[Text](text)** | 在匯出欄中檢索整個文字。 |

## 方法

|     |     |
| --- | --- |
| **[Clear](clear)** | 清除輸出列的內容。 |
| **[SetFocus](set_focus)** | 把鍵盤焦點設置到輸出列上。 |
| **[write](write)** | 追加一個字符串到輸出列上。 |
| **[writeln](writeln)** | 追加一個字符串和一個新行到輸出列上。 |

## 示例

### \[JavaScript\]

```
OutputBar.Clear();
OutputBar.writeln( "Hello!" );
OutputBar.Visible = true;
OutputBar.SetFocus();
```

### \[VBScript\]

```
OutputBar.Clear
OutputBar.writeln "Hello!"
OutputBar.Visible = True
OutputBar.SetFocus
```

## 版本

支持 EmEditor 7.00 或之後的版本。


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
