# Using Command Line Options

Command line options can be specified in the Run dialog box on the Start menu or a  Command Prompt window.

## Syntax

### Open a file or files

> " _File1_" " _File2_" " _File3_" ... \[/r\] \[/fh\] \[/nr\] \[/sp\] \[/l _LineNumber_\] \[/cl _ColumnNumber_\]
> \[/cp _encoding_\] \[/c " _Config_"\] \[/mf " _MacroPath_"\]

### Create a new file

> \[/cd\] \[/sp\] \[/c " _Config_"\] \[/mf " _MacroPath_"\]

### Create a new file and paste

> \[/i\] \[/cd\] \[/sp\] \[/c " _Config_"\] \[/mf " _MacroPath_"\]

### Create a new file and paste with quote

> \[/iq\] \[/cd\] \[/sp\] \[/c " _Config_"\] \[/mf " _MacroPath_"\]

### Create a new file and paste with quote and returns

> \[/iqr\] \[/cd\] \[/sp\] \[/c " _Config_"\]
> \[/mf " _MacroPath_"\]

### Display the Tray Icon

> /ti

### Print a file

> " _File_" /p \[/nr\] \[/sp\] \[/cp encoding\]

### Compare two files

> /cmp " _File1_" " _File2_"

### Convert a file encoding

> " _SrcFile_" \[/nr\] \[/sp\] \[/cp _EncodingToOpen_\] \[/c " _Config_"\] /cps _EncodingToSave_ /ss+ /sa " _DestFile_"
>
> To save
> without the Unicode signature (BOM), use /ss- instead of /ss+.

### Display Find in Files dialog box

> /fd

### Display Replace in Files dialog box

> /rd

### Find in files

> /fc " _FindWhat_" \[/fr\] \[/fw\] \[/x\] \[/fn\] \[/fu " _FilesToIgnore_"\]
> \[/cp _encoding_\] " _path_"
>
> This command is called internally when the Find button is selected in the Find in Files dialog box. To search without matching case, use /fi instead
> of /fc.

### Replace in files

> /fc " _FindWhat_" \[/fr\] \[/fw\] \[/x\] \[/ko\] \[/fu " _FilesToIgnore_"\] \[/cp
> _encoding_\] " _path_" /rw " _ReplaceWith_" \[/bk " _BackupFolder_"\]
>
> This command is called internally when the Replace All button is selected in the
> Replace in Files dialog box. To search without matching case, use /fi instead of /fc. /ko and /bk cannot be specified simultaneously.

### Open a file and replace

> " _File_"
> /rc " _FindWhat_" \[/fw\] \[/x\] \[/cp encoding\] /rw " _ReplaceWith_"
>
> This command is called internally during the Replace in Files process. To search without matching
> case, use /ri instead of /rc.

### Restore workspace

> /ws
>
> This command is called internally when the Restore Workspace command is selected.

### Save workspace

> /wss
>
> This command is called internally when the Save Workspace command is selected.

### Grab text with EmEditor

> /eh
>
> This command is called from the Tray Icon when the shortcut key to grab text with EmEditor defined in the Customize Tray Icon dialog box is pressed.

### Display Help

> /?

## Options

|     |     |
| --- | --- |
| /? | displays Help. |
| /act | activates EmEditor if it is already running, or launches EmEditor if it is not already running. |
| /bk " _BackupFolder_" | specifies a backup folder when replacing in files. |
| /c " _Config_" | sets the configuration. |
| /ca | closes all documents. |
| /car | closes all documents including a hidden window if the "Quick Start" option is enabled. |
| /cd | set the current directory as the default folder in the Open dialog box. |
| /cjl | customizes the Jump List on Windows 7 or later. |
| /cl _ColumnNumber_ | logical column number. A negative number means the number of characters from the end of the line. |
| /clw | clears the workspace. |
| /cmp | compares two files. |
| /cp _Encoding_ | sets an encoding to open as.  An encoding can be one of [Encoding Constants](../../macro/const/const_encoding). A combination with following values can be specified.

|     |     |
| --- | --- |
| 131072 | Detects Unicode signature (BOM). |
| 262144 | Detects UTF-8. |
| 524288 | Detects HTML/XML Charset. |
| 1048576 | Detects all encodings. | |
| /cps _Encoding_ | sets an encoding to save as.  An encoding can be one of [Encoding Constants](../../macro/const/const_encoding). |
| /csv " _CSVName_" | sets the initial CSV mode, and the CSV detection is disabled. _CSVName_ can be the name of the CSV format or the index number. If 0 is specified, the normal mode is used. |
| /di | specifies the working folder when creating a new document. Used internally by EmEditor. |
| /eh | grabs a text box contents. |
| /fc " _FindWhat_" | find in files (case sensitive). |
| /fd | displays the [**Find in Files**dialog box](../../dlg/find_in_files/index). |
| /ff " _FindWhat_" | find a string directly within the opened document. Can be combined with <br> /mc or /x. |
| /fi " _FindWhat_" | find in files (ignore case). |
| /fh | highlights searched strings. |
| /fhf | filters using the last searched string(s). |
| /fn | displays only file names when finding in file. |
| /fu " _FilesToIgnore_" | ignores the following file or folder names. |
| /fr | search in sub folders when finding in <br>files (use with /fc or /fi). |
| /fw | searches only words. |
| /hide | runs EmEditor as a hidden window when the "Quick Start" option is enabled. |
| /i | pastes a text string from the Clipboard. |
| /ipi | refreshes the plug-in list. used from plug-in installers. |
| /iq | pastes a text string in quotes from the Clipboard. |
| /iqr | pastes a text string in quotes and returns from the Clipboard. |
| /ko | keeps modified files open when replacing in files. |
| /l _LineNumber_ | move cursor to the logical line number. A negative number means the number of lines from the bottom of the file. |
| /layout " _Layout_" | uses a specified layout. |
| /max _limit_ | Stops find or replace in files when the number of matches reaches this number. |
| /mc | matches cases when /ff is used to find a string. |
| /mf | specifies a macro file to run. |
| /n | always start as a new file. |
| /ncp | suppresses "The specified file does not exist. Open as a new file?" prompt when a specified file is not found. <br> This option does not apply when restoring files from a workspace. |
| /ne | specifies event-triggered macros should be disabled. |
| /ng | always creates a new group window. |
| /nr | does not add the file path to the recent file list. |
| /od | displays the Open dialog box to select files to open. |
| /p | prints the file. |
| /pos left top right bottom | specifies the window position with four integers (left, top, right, bottom). |
| /r | read-only mode. |
| /rc " _FindWhat_" | replaces in files (case sensitive). |
| /rd | displays the [**Replace in**\<br>**Files** dialog box](../../dlg/replace_in_files/index). |
| /rh | opens HTML files as read-only. Used internally. |
| /ri " _FindWhat_" | replaces in files (ignore case). |
| /rr | opens files in folders recursively. |
| /rw | specifies a string to be replaced with. |
| /sa " _DestFile_" | specifies a file name to save as after the encoding conversion. |
| /sca | saves and closes all opened documents. |
| /scrlf | saves the file using CR+LF as newline characters after the encoding conversion. |
| /scr | saves the file using the CR only as newline characters after the encoding conversion. |
| /slf | saves the file using the LF only as newline characters after the encoding conversion. |
| /sp | specifies that a new separate process from other EmEditor windows should be run. This option is useful when a new EmEditor window must be launched from another application because the application must monitor the process termination so it can <br> detect the file modification. If this is specified, however, some features including tab operations will be disabled, and will void support. |
| /ss+ | saves the file with a Unicode signature (BOM) after the encoding conversion. |
| /ss- | saves the file without a Unicode signature (BOM) after the encoding conversion. |
| /ti | displays the Tray Icon. |
| /uob | uses the Output Bar to display the Find in Files results. |
| /x | finds or finds in files using a regular expression. |
| /xnr | finds or finds in files using a number range expression. |
| /ws | restores the workspace. |
| /wsf "WorkspaceFile" | restores the specified workspace. |
| /wss | saves the workspace. |

## Examples

/rr \*.htm

> opens all .htm files including all sub folders.

/p "filename"

> prints filename.

/r "filename"

> opens filename in read only
> mode.

/c "Normal" "filename"

> opens filename in the
> default configuration.

/l 123 "filename"

> opens filename, jumps to
> the 123rd line and displays it.

/l -1 "filename"

> opens filename, jumps to the last line and displays it.

/ff "what" /mc "filename"

> opens filename, and finds what matching cases.

/fh

> highlights string of last search.

/ti

> opens as a tray icon.

/fi "ABC" "c:\\Temp\\\*.txt"

> searches for the string ABC
> from all files with the extension .txt on the c:\\Temp folder while ignoring case.

/fi "abc" /fr /fw /fn /fu "\_\*;\*.bak" /cp 65536 "c:\\test\\\*.htm;\*.txt"

> searches for the string abc from all files with the extension .htm and .txt on the c:\\test folder while ignoring case. it searches sub folders, searches only words, displays only file names,
> ignores file or folder names matching "\_\*;\*.bak", and uses the system default encoding.

/fc "\[a-e\]" /fr /x /fu "\_\*;\*.bak" /cp 65536
"c:\\test\\\*.htm;\*.txt"

> searches for text matching a regular expression \[a-e\] from all files with the extension .htm and .txt on the c:\\test folder while not ignoring case. it searches sub folders, ignores file or folder
> names matching "\_\*;\*.bak", and uses the system default encoding.

"c:\\test\\utf16.txt" /cp 65537 /cps 65001 /ss- /sa "c:\\test\\utf8.txt" /scrlf

> converts a UTF-16LE file c:\\test\\utf16.txt to UTF-8 without a Unicode signature and saves as c:\\test\\utf8.txt. The newline characters is converted to CR+LF.

/layout "Focus Mode"

> uses the "Focus Mode" layout.

## Tips

- The string searched for in files must be after /fc or /fi.
- If no options are specified, the selected file will simply be opened.
- If /c is not specified and the associated extensions of the
configuration are the same, open the file with that configuration.
- If a folder name is specified instead of a file name, the Open dialog box with that folder will be displayed.
- Command line options are case sensitive. For instance /r will not be recognized if written as /R.
- Escape sequences are always on when searching from the command line.
- A hyphen (-) can be used instead of a slash (/). For instance, -sp can be used instead of /sp.
- To set EmEditor as the default text editor for Git, open Git Bash and type: git config --global core.editor "emeditor.exe -sp".