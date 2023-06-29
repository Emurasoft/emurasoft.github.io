# To Use Snippets Plug-in

The **Snippets** plug-in is installed by default with EmEditor Professional. This plug-in allows you to insert words and phrases quickly. A snippet is a piece of text that you insert into your document and may contain plain text, placeholders, shell code, a macro, or regular expressions to
transform text and various built-in and user-defined parameters. In the Snippets plug-in, you can create two types of items - snippets and macros.

To use the **Snippets** plug-in, Click **![Snippets](../../images/plugin_snippets.gif)** on the **Plug-ins** bar. Or on the **Tools** menu, point to **Plug-ins**, and then click **Snippets**. The **Snippets** custom bar will appear.

Right-clicking on the Snippets bar shows the following options:

|     |     |
| --- | --- |
| Insert | inserts the selected snippet. |
| Edit | edits the selected snippet. |
| Select Snippet | Displays a dialog box where you can type a few characters to select a snippet to insert. |
| New Snippet | creates a new snippet. |
| New Macro | creates a new macro. |
| New Folder | creates a new folder. |
| Move Up | moves the selected snippet up on the list. |
| Move Down | moves the selected snippet down on the list. |
| Delete | deletes the selected snippet. |
| Delete All | deletes all of the snippets. |
| Import to This Folder | imports snippets to this folder. |
| Import to Root | imports snippets to the root folder. |
| Export This Folder | exports all snippets in this folder to the specified destination. |
| Export All | exports all snippets to the specified destination. |
| Reset All (Import Default) | resets all snippets and imports the default list of snippets. |
| Trigger Keys | shows or hides trigger keys. |
| Configurations | shows or hides configurations. |
| Plug-in Properties | displays the plug-in properties. |
| Name | arranges by name. |
| Type | arranges by type. |
| Text | arranges by text. |
| Tip | arranges by tip. |
| Trigger | arranges by trigger. |
| Ascending Order | arranges in ascending order. |
| Descending Order | arranges in descending order. |
| Auto Arrange | arranges snippets automatically. |
| Properties | displays the properties of the selected snippet or snippet folder. |

## Snippets Plug-in Properties

To adjust the properties of the Snippets plug-in, right-click the Snippets Plug-in button on the Plug-ins bar and select Properties.

### General tab

|     |     |
| --- | --- |
| Custom Bar Position | sets the custom bar position. |
| Run Background | allows the snippets to work even if you close the Snippets custom bar. |
| Default Shortcut Key | specifies the default shortcut key; the initial default shortcut key is TAB. |
| Verbosity | adjusts the frequency of tips. |
| Delay Time | adjusts the delay time before a tip appears. |

### Global Parameters tab

|     |     |
| --- | --- |
| Add | adds a parameter and specifies its value. |
| Delete | deletes a parameter. |

### Keyboard page

|     |     |
| --- | --- |
| Commands | lists available commands. (Popup Menu or Select Snippets) |
| Press New Shortcut Key | allows you to enter shortcut key for the selected command. |
| Current Keys | Current keys assigned to the selected command. |
| Description | Description for the selected command. |
| Assign button | Assign the shortcut key to the currently selected command. |
| Delete button | Delete the currently selected shortcut key. |

## Snippets Folders Properties

To adjust the properties of each of the snippets folders, right-click on a folder in the Snippets custom bar, and select Properties.

### General tab

|     |     |
| --- | --- |
| Name | specifies the name of the snippets folder. |

### Configurations tab

|     |     |
| --- | --- |
| Auto complete only with the following configurations | specifies which configurations to auto complete with. |
| Snippets | sets the configuration to edit with for snippets. |
| Macros | sets the configuration to edit with for macros. |

## Snippets Properties

To adjust the properties of each of the snippets, right-click on a snippet in the Snippets custom bar, and select Properties.

### General tab

|     |     |
| --- | --- |
| Name | specifies the name of the snippets folder. |
| Trigger | specifies the trigger for the snippet. |
| Shortcut | specifies the shortcut for the snippet. |
| Tip | specifies the tip for the snippet. |
| Type | specifies the type (Snippet or Macro). |
| Text | specifies the text of the snippet. |
| Edit | allows a user to edit the snippet in the EmEditor window. |

### Configurations tab

|     |     |
| --- | --- |
| Auto complete only with the following configurations | specifies which configurations to auto complete with. |
| Snippets | sets the configuration to edit with for snippets. |
| Macros | sets the configuration to edit with for macros. |

## Snippet Syntax

### Plain text

You may include any plain text you want to insert into your document. To write plain text, most characters can be used, however, if you want to include \\, $, or \` in your plain text, they must be escaped as \\\, \\$, and \\\`.

### Placeholders

After you insert a snippet, the cursor position jumps between placeholders, and pressing the TAB key will jump forward to the next placeholder.

You can define these tab stops within your snippet as ${n:default} where default is the default value that first appears when the snippet is inserted. When there is no default value, you can omit {} so the tab stop appears as $n, where n is an integer value between 0 and 9. When a user inserts a
snippet, the first cursor position is at $1, and pressing TAB will forward the tab stop to next placeholder $2, $3, ... etc. The last tab stop is at $0.

For instance, the following snippet inserts a hyperlink in HTML, and the first cursor position is at $1. While the cursor is at $1, if the user presses the TAB key, the cursor jumps to $2, and then to $0.

<a target="$1" href="$2">$0</a>

Snippets can include default values. The following snippet inserts a hyperlink with a default value.

<a target="${1:\_blank}" href="${2:url}">$0</a>

You can include a placeholder within a placeholder. The following snippet inserts a hyperlink tag with the target parameter selected. A user can decide to overtype the argument, delete it, or press the TAB key again to proceed to the next placeholder.

<a ${1: target="${2:\_blank}"} href="${3:url}">$0</a>

### Mirrors

If you use the same placeholder index, all the values in these placeholders become the same or mirrored. The following snippet inserts a “for” loop. In this case, the value i is the default value for the placeholder $2, and placeholders with the same index are used in two other places. While the
cursor is at ${2:i}, changing the value of i will be mirrored into the other places.

for( ${1:int} ${2:i} = ${3:0}; $2 != ${4:10}; $2++ ){

$0

}

### Transformation

You can transform the value of one placeholder into another by using a regular expression and a replace format. The syntax is: ${n/regexp/replace\_format/option} where

n: the index of the placeholder

regexp: regular expression to search for

replace\_format: replace format

option:

**i** : ignore cases

**g** : global option

The following example copies characters entered in the first line to the second line, except the first character is capitalized.

$1

${1/./\\U\\0/}

### Predefined parameters:

$1 Placeholder 1

$2 Placeholder 2

$3 Placeholder 3

$4 Placeholder 4

$5 Placeholder 5

...

$9 Placeholder 9

$0 Last Placeholder

${n:default} Placeholder n with default Text

${Path} The full path name of the file.

${Dir} The directory name of the current file.

${Filename} The file name without its extension.

${FilenameEx} The file name with its extension.

${Ext} The file name extension.

${LineText} Line at cursor position.

${WordText} Word at cursor position.

${SelText} The selected text.

${CurCol} The logical column number of the cursor.

${CurLine} The logical line number of the cursor.

${Date} Today's date.

${Time} The current time.

${Charset} Charset (used in HTML meta tag)

${TabSize} The tab size.

${IndentSize} The indent size.

${AutoIndent} 1 if auto indent is on, 0 if not.

${UseSpacesForTabs} 1 if "Use Spaces for Tabs" is on, 0 if not.

${AppVersion} The version of EmEditor.

${PluginVersion} The version of the Snippets plug-in.

${TM\_FILENAME} Same as ${FilenameEx}.

${TM\_CURRENT\_LINE} Same as ${LineText}.

${TM\_CURRENT\_WORD} Same as ${WordText}.

${TM\_DIRECTORY} Same as ${Dir}.

${TM\_FILEPATH} Same as ${Path}.

${TM\_LINE\_INDEX} Same as ${CurCol}.

${TM\_LINE\_NUMBER} Same as ${CurLine}.

${TM\_SELECTED\_TEXT} Same as ${SelText}.

${TM\_SOFT\_TABS} Same as ${UseSpacesForTabs}.

${TM\_TAB\_SIZE} Same as ${TabSize}.

${PickFullPath,title,filter} The full path name of the selected file. The title is the title of the dialog box, and the filter is the file filter in the format: Text files\|\*.txt\|All files\|\*.\*\|\|

${PickRelativePath,title,filter} The relative path name of the selected file. The title is the title of the dialog box, and the filter is the file filter in the format: Text files\|\*.txt\|All files\|\*.\*\|\|

${PickColor} The RGB value of the selected color.

${DefColor} The RGB value of the recently selected color.

You can also create your own parameter in this form ${parameter\_name} where parameter\_name is not predefined in the above list. When a new user parameter is used, a dialog box appears where you can insert a new value, unless the value of a parameter can be saved in the Global Parameter tab of the
Plug-in properties.

### Shell Codes

You can define a shell code that can run a console application and then pass strings to its standard input. The standard output, as well as the standard error, from the console application is redirected to the cursor position of your text document. A shell
code must be specified by the following format:

\`\- appname

stdin1

stdin2

...

\`

If the result string ends with a newline character (CR, LF or CR+LF), the newline character will be removed. For instance the following snippet inserts the contents of the ${name} parameter in upper characters.

\`\- powershell -

\# prompts for name then echos the hello greeting

\\$name = "${name}".ToUpper()

"Hello \\$name!"

exit

\`

If you don't want to parse snippet parameters, you can write:

\`!\- appname

stdin1

stdin2

...

\`

If you want to run a command used in command prompt, you can define a shell code that can be passed into the Command Prompt window (cmd.exe) in this form \`#cmd shell\_code\`. The value you specify is passed to cmd.exe in this form: "%COMSPEC% /c shell\_code". The standard output, as well as the standard error, from the console application is redirected to the
cursor position of your text document. For instance the following snippet inserts the current folder listing. You can include as many shell codes as you want within each snippet.

\`#cmd DIR\`

### Macros

You can include a macro in a snippet in the form of \`# \`. The first character # indicates this is a macro, not a shell code. If this is an ActiveScript other than JavaScript, such as VBScript, PerlScript, PHPScript, or RubyScript, you will need to define the language using "#language=". For
instance, if you wish to use VBScript, you would write \`#language="VBScript"...\`. The **Interface** object is used to pass values between the snippets and the EmEditor macro engine. The following sample inserts the contents of the Clipboard to the cursor position.

The clipboard contains \`# Interface.write( clipboardData.getData("") );\`.

Interface.write() method passes the macro result to the snippet. You can also use Interface.writeln() instead to add a carriage return and a newline character (CR+LF) at the end of the result. You can include as many macros as you want within each snippet.

### Parameters within default value, shell code or macros

The placeholder default values can contain parameters, shell code or a macro. The following snippet inserts a <p> tag with the selected text between <p> and </p> if a selection exists.

<p>${0:${SelText}}</p>

Shell code and macros can contain parameters within their code or macro. The following snippet displays a dialog box where a user enters a value for the ${name} parameter to continue.

\`# var s = "${name}";

for( var i = 0; i != 5; i++ ){

Interface.writeln( s );

}

\`

You will need to be careful that all \ and \` and $ are proceeded by a \\. For instance, the following snippet inserts "C:\\Program Files\\EmEditor".

\`# Interface.writeln( "C:\\\\\\Program Files\\\\\\EmEditor" ); \`

This is because a backslash must be written as \\\, and JavaScript also converts a backslash to \\\. As a result, a backslash converts to four backslashes (\\\\\\).

If you don't want backslashes converted and if you don't need to include any parameters within a shell code or macro, you can include an exclamation mark (!) at the beginning of the code. That is--in shell code, you would write \`!...\` and in macros, you would write \`!#...\`. Therefore, the previous
example can be rewritten as:

\`!# Interface.writeln( "C:\\\Program Files\\\EmEditor" ); \`

## Tips

- Press the **F6** key or **ESC** key to set the keyboard focus back to the editor.
- The custom bar position can be set from top, bottom, right or left by right-clicking the plug-in button on the **Plug-ins** bar, and selecting the **Properties**.