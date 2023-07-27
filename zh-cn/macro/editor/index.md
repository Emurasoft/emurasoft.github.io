# Editor 对象

## 属性

|     |     |
| --- | --- |
|[ActiveDocument](editor_activedocument) | 为当前文档，检索 Document 对象。 |
|[Configs](configs) | 检索 Configs 集合。 |
|[CsvList](csv_list) | 检索或设置 CsvList 集合。 |
|[Documents](editor_documents) | 为当前打开的文档，检索 Documents 集合。 |
|[EnableTab](editor_enabletab) | 设置或检索是否标签页被启用。 |
|[filters](filters) | 检索 Filters 集合。 |
|[FullName](editor_fullname) | 检索 EmEditor 可执行文件 (emeditor.exe) 的完整规格，包括路径。 |
|[FuzzyOptions](fuzzy_options) | 检索 FuzzyOptions 对象。 |
|[LangID](langid) | 检索当前选取的语言 ID。 |
|[regex](regex) | 检索 Regex 对象。 |
|[RegisteredName](registeredname) | 检索注册名。 |
|[Version](editor_version) | 检索 表示当前 EmEditor 版本的字符串。 |

## 方法

|     |     |
| --- | --- |
|[BatchFindInFiles](editor_batchfindinfiles) | 在多个文件中搜索多个字符串。 |
|[BatchReplaceInFiles](editor_batchreplaceinfiles) | 在多个文件中替换多个字符串。 |
|[Compare](compare) | 比较两个文档。 |
|[GetUnicodeName](getunicodename) | 检索指定字符或字符串的 Unicode 名。 |
|[ExecuteCommandByID](editor_executecommandbyid) | 执行由一个表示命令 ID 整数标识的命令。 |
|[ExecuteMacro](editor_executemacro) | 执行一个指定的宏。 |
|[ExecutePlugin](editor_executeplugin) | 执行指定插件。 |
|[FileDialog](filedialog) | 显示一个“打开”或“另存为”对话框，让用户指定驱动器、目录以及要打开的文件名。 |
|[FindInFiles](editor_findinfiles) | 在多个文件中搜索匹配的字符串。 |
| [GetProfileInt](getprofileint) | 按 EmEidtor 的设定，从注册表或一个 INI 文件上检索指定项目的整数值。 |
| [GetProfileString](getprofilestring) | 按 EmEidtor 的设定，从注册表或一个 INI 文件上检索指定项目的字符串值。 |
| [Join](join) | 按指定键列，用一个与 JOIN 操作类似的方法合并两个 CSV 文档，并创建一个新文档。 |
|[NewFile](editor_newfile) | 新建一个文件。 |
|[OpenFile](editor_openfile) | 打开一个已存在的文件。 |
|[QueryStatusByID](editor_querystatusbyid) | 检索指定命令的当前状态，是否已被勾选和启用。 |
|[QueryStringByID](editor_querystringbyid) | 检索与指定命令相关联的字符串。 |
|[RefreshCommonSettings](refresh_common_settings) | 加载常用设置并刷新 EmEditor 窗口。 |
|[ReplaceInFiles](editor_replaceinfiles) | 在多个文件中替换文本。 |
|[SaveAll](editor_saveall) | 保存所有当前打开的文件。 |
|[SaveCloseAll](editor_savecloseall) | 保存并关闭所有打开的文件。 |
|[Stderr](stderr) | 将字符串写入标准错误。 |
| [WriteProfileInt](writeprofileint) | 按 EmEditor 的设定，把一个整数值设置到注册表或一个 INI 文件中。 |
| [WriteProfileString](writeprofilestring) | 按 EmEditor 的设定，把一个字符串值设置到注册表或一个 INI 文件中。 |

## 版本

支持 EmEditor 4.00 或之后的版本。


```{toctree}
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
