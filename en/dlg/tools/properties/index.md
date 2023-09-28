# External Tool Properties dialog box

This dialog box appears when the
**Properties** button on the **External Tools** dialog box is selected.

## 

### Title text box

The name of the tool or command that will appear on the **External Tools**
submenu of the **Tools** menu.

### Command text box

Specifies the path to the .exe, .com, .bat, .cmd, or other files that you
intend to launch.

### Arguments text box

Specifies the arguments that are passed to the tool when the tool is
launched. Use the **Arrow** (**>**) button to select from a
list of predefined arguments. You can also specify environment variables, such as
%WinDir%.

### Initial Directory text box

Specifies the working directory of the tool. Use the
**Arrow** (**>**) button to select a directory. You
can also specify environment variables, such as %WinDir%.

### Icon Path text box

Enter the file name you sampled the icon from.

### Current Icon list box

List of icons you can use and the current icon selected.

### Save File check box

If this is checked, EmEditor will save the current open document before
launching the tool.

### Use Current Environment Variables check box

If this is checked, external tools will use current environment variables when launched. If not, external tools will use environment variables inherited from the parent process (EmEditor).

### Use Output Bar check box

If this is checked, EmEditor will redirect the standard output and standard error output to the Output Bar.

### Set Focus in Output Bar check box

If this is checked, EmEditor will set the keyboard focus to the Output Bar.

### Close on Exit check box

If this is checked, the Output Bar will be closed after the tool process is terminated.

### Input drop-down list box

Select the standard input for the external tool.

|     |     |
| --- | --- |
| None | No standard input is used. |
| Selection | The selected text is used as the standard input. |
| Document | The entire document is used as the standard input. |
| Custom | Specifies the standard input in customized format. If this is selected, the **Custom** text box and the **Add EOF** check box must also be specified. |

### Custom text box

Specifies the customized standard input. This text box is enabled only if **Custom** is selected in the **Input** drop-down list box.

### Add EOF (Ctrl+Z, U+001A or 1AH) check box

If this is checked, the **End of File** character (U+001A or 1AH) will be added to the end of the customized standard input. The EOF character is generally not necessary, but some old applications might need the EOF character.

### Output drop-down list box

Select the standard output for the external tool.

|     |     |
| --- | --- |
| Discard | The standard output will be discarded. |
| Replace Selection | The standard output will replace the selected text. |
| Replace Document | The standard output will replace the entire document. |
| Insert before Selection | The standard output will be inserted before the selected text. |
| Insert after Selection | The standard output will be inserted after the selected text. |
| Show as Tool Tip | The standard output will be displayed as a tool tip. |
| Create New Document | The standard output will be contents of a new document. |

### Encoding drop-down list box

Select the encoding for the Output Bar.

### Standard Error drop-down list box

Select how you want to display the standard error for the external tool.

|     |     |
| --- | --- |
| Discard | The standard error will be discarded. |
| Replace Selection | The standard error will replace the selected text. |
| Replace Document | The standard error will replace the entire document. |
| Insert before Selection | The standard error will be inserted before the selected text. |
| Insert after Selection | The standard error will be inserted after the selected text. |
| Show as Tool Tip | The standard error will be displayed as a tool tip. |
| Create New Document | The standard error will be contents of a new document. |
| Display as Output Bar | The standard error will be displayed in the Output Bar. |

### ... button

Click this button to find the specified file.

### \> button

Use this button to select from a list of predefined arguments.

## See also

[Q. \
Examples of external tool definitions?](../../../faq/tools/tools_external)

