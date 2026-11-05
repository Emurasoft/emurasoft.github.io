# OutputBar Object

## Properties

|     |     |
| --- | --- |
| **[CurrentDirectory](current_directory)** | Sets the current directory for the Output Bar. |
| **[Visible](visible)** | Shows or hides the Output Bar. |
| **[Text](text)** | Retrieves the entire text in the Output Bar. |

## Methods

|     |     |
| --- | --- |
| **[Clear](clear)** | Clears the contents of the Output Bar. |
| **[SetFocus](set_focus)** | Sets the keyboard focus to the Output Bar. |
| **[write](write)** | Appends a string to the Output Bar. |
| **[writeln](writeln)** | Appends a string and a newline character to the Output Bar. |

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
:hidden:
:maxdepth: 1
clear
current_directory
set_focus
text
visible
write
writeln
```
