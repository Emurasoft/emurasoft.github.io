# Q. What are examples of External Tools configuration?

- OpenInternet Explorer

Command: C:\\Program Files\\Internet Explorer\\iexplore.exe

Arguments: $(Path)

Initial Directory: $(Dir)

Icon Path: C:\\Program Files\\Internet Explorer\\iexplore.exe

CheckSave File

- OpenExplorer

Command: %WinDir%\\explorer.exe

Arguments: $(Dir)

Initial Directory: $(Dir)

Icon Path: %WinDir%\\explorer.exe

- OpenCommand Prompt

Command: %WinDir%\\system32\\cmd.exe

Arguments: $(Dir)

Initial Directory: $(Dir)

Icon Path: %WinDir%\\system32\\cmd.exe

- Compile byVisual C++

Command: %WinDir%\\system32\\cmd.exe

Arguments: /k "C:\\Program Files\\Visual Studio\\Vc7\\bin\\vcvars32.bat"&&cl $(Path)

Initial Directory: $(Dir)

Icon Path: C:\\Program Files\\Visual Studio\\Common7\\IDE\\devenv.exe

CheckSave File

- Run associated program

Command: $(Path)

Arguments:

Initial Directory: $(Dir)

Icon Path:

CheckSave File

- SearchGoogle for a word at cursor or a selected text.

Command: http://google.com/search?q=$(CurText)

Arguments:

Initial Directory:

Icon Path:

- Check out fromMicrosoft Visual SourceSafe

Command: %WinDir%\\system32\\cmd.exe

Arguments: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkout
$/(path)/$(Filename).$(Ext) -y(user name)

Initial Directory: $(Dir)

Icon Path: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

- Check in toMicrosoft Visual SourceSafe

Command: %WinDir%\\system32\\cmd.exe

Arguments: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkin
$/(path)/$(Filename).$(Ext) -y(user name)

Initial Directory: $(Dir)

Icon Path: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

CheckSave File

You can use the following predefined arguments inCommand,Arguments,Initial Directory, andIcon Path.

$(Path) The full path name of the file.

$(Dir) The directory name of the file.

$(Filename) The file name without its extension.

$(Ext) The file name extension.

$(CurLine) The logical line number of the cursor.

$(CurText) The selected text if selected, or the word at the cursor if not
selected.

You can also specify environment variables, such as %WinDir%
