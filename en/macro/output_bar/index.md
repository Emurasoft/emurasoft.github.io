# OutputBar Object

## Properties

|     |     |
| --- | --- |
| **[CurrentDirectory](current_directory)** | Sets the current directory for the output bar. |
| **[Visible](visible)** | Shows or hides the output bar. |
| **[Text](text)** | Retrieves the entire text in the output bar. |

## Methods

|     |     |
| --- | --- |
| **[Clear](clear)** | Clears the contents of the output bar. |
| **[SetFocus](set_focus)** | Sets the keyboard focus to the output bar. |
| **[write](write)** | Appends a string to the output bar. |
| **[writeln](writeln)** | Appends a string and a newline character to the output bar. |

## Examples

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

## Version

Supported on EmEditor Professional Version 7.00 or later.


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
