# Editor Object

## Properties

|     |     |
| --- | --- |
| **[ActiveDocument](editor_activedocument)** | Retrieves the Document Object for the current document. |
| **[Configs](configs)** | Retrieves the Configs Collection. |
| **[CsvList](csv_list)** | Retrieves or sets the CsvList Collection. |
| **[Documents](editor_documents)** | Retrieves the Documents Collection for the currently opened documents. |
| **[EnableTab](editor_enabletab)** | Sets or retrieves whether the tab is enabled. |
| **[filters](filters)** | Retrieves the Filters collection. |
| **[FullName](editor_fullname)** | Retrieves the full specification of the EmEditor executable file (emeditor.exe), <br> including the path. |
| **[FuzzyOptions](fuzzy_options)** | Retrieves the FuzzyOptions object. |
| **[LangID](langid)** | Retrieves the currently selected language ID. |
| **[regex](regex)** | Retrieves the Regex object. |
| **[RegisteredName](registeredname)** | Retrieves the registered name. |
| **[Version](editor_version)** | Retrieves the string indicating the current version of EmEditor. |

## Methods

|     |     |
| --- | --- |
| **[BatchFindInFiles](editor_batchfindinfiles)** | Searches multiple files for multiple strings. |
| **[BatchReplaceInFiles](editor_batchreplaceinfiles)** | Replaces multiple strings in multiple files. |
| **[Compare](compare)** | Compares two documents. |
| **[GetUnicodeName](getunicodename)** | Retrieves the Unicode name of the specified character or string. |
| **[ExecuteCommandByID](editor_executecommandbyid)** | Executes the command identified by an integer indicating the Command ID. |
| **[ExecuteMacro](editor_executemacro)** | Executes the specified macro. |
| **[ExecutePlugin](editor_executeplugin)** | Executes the specified plug-in. |
| **[FileDialog](filedialog)** | Displays an Open or Save As dialog box that lets the user specify the drive, directory, and the name of a file to open. |
| **[FindInFiles](editor_findinfiles)** | Searches multiple files for matching string. |
| [**GetProfileInt**](getprofileint) | Retrieves the integer value for the specified entry from the Registry or an INI file depending on the EmEditor <br> settings. |
| [**GetProfileString**](getprofilestring) | Retrieves the string value for the specified <br> entry from the Registry or an INI file depending on the EmEditor settings. |
| [**Join**](join) | Combines two CSV documents specifying key columns, using a method similar to JOIN operations, and creates a new document. |
| **[NewFile](editor_newfile)** | Creates a new file. |
| **[OpenFile](editor_openfile)** | Opens an existing file. |
| **[QueryStatusByID](editor_querystatusbyid)** | Retrieves the current status of the specified command, whether it is <br> enabled and checked. |
| **[QueryStringByID](editor_querystringbyid)** | Retrieves the string associated with the specified command. |
| **[RefreshCommonSettings](refresh_common_settings)** | Loads common settings and refreshes the EmEditor window. |
| **[ReplaceInFiles](editor_replaceinfiles)** | Replaces text in multiple files. |
| **[SaveAll](editor_saveall)** | Saves all currently open files. |
| **[SaveCloseAll](editor_savecloseall)** | Saves and Closes all open files. |
| **[Stderr](stderr)** | Writes a string to standard error. |
| [**WriteProfileInt**](writeprofileint) | Sets an integer value into the Registry or an INI <br> file depending on the EmEditor settings. |
| [**WriteProfileString**](writeprofilestring) | Sets a string value into the Registry or an INI file depending on the <br> EmEditor settings. |

## Version

Supported on EmEditor Professional Version 4.00 or later.


```{toctree}
:hidden:
:maxdepth: 1
compare
configs
csv_list
editor_activedocument
editor_batchfindinfiles
editor_batchreplaceinfiles
editor_documents
editor_enabletab
editor_executecommandbyid
editor_executemacro
editor_executeplugin
editor_findinfiles
editor_fullname
editor_newfile
editor_openfile
editor_querystatusbyid
editor_querystringbyid
editor_replaceinfiles
editor_saveall
editor_savecloseall
editor_version
filedialog
filters
fuzzy_options
getprofileint
getprofilestring
getunicodename
join
langid
refresh_common_settings
regex
registeredname
stderr
writeprofileint
writeprofilestring
```
