# To Use Projects Plug-in

TheProjects plug-in is installed by default with EmEditor Professional. This plug-in displays folder trees and allows you to open files from the folder trees.

To create a new project using theProjects plug-in:

1. Click![](../../images/projects.gif) on theProjects bar. Or on theTools menu, point toPlug-ins, and then clickProjects. TheProjects custom bar will appear.
2. Right-click in theProjects bar, and selectNew Projects.
3. Right-click onUntitled Project, and selectAdd Existing Files.
4. Select all files you want to include in the project.

## 

### The Projects Plug-in Commands

Right clicking on the Projects bar shows the following options:

|     |     |
| --- | --- |
|Expand/Collapse | expands or collapses the node. |
|Open All | opens all files in the folder. |
|Open | opens the file. |
|Open as Read-Only | opens the file as read-only. |
|Open with Encoding | opens the file with a specified encoding. |
|New Folder | creates a new folder. |
|Cut | cuts the selected item and moves it to the Clipboard. |
|Copy | copies the selected item and pastes it to the Clipboard. |
|Paste | inserts the contents of the Clipboard. |
|Remove | removes the selected item. |
|Rename | renames the selected item. |
|Run Solution | runs the solution. |
|New Solution | creates a new solution. |
|Open Solution | opens an existing solution. |
|Save Solution As | saves the solution file with a new name. |
|List of Recent Solutions | opens a specified recently accessed solution (multiple items). |
|New Project | creates a new project. |
|Open Project | opens an existing project. |
|Save Project As | saves the project file with a new name. |
|Add Existing Files | adds existing files to the project. |
|Add Active File | adds the active file to the project. |
|Add All Open Files | adds the all open files to the project. |
|List of Recent Projects | opens a specified recently accessed project (multiple items). |
|Set as Startup Project | sets the specified project as the startup project. |
|File Name Only | displays the file name only for each item. |
|Relative Path | displays the relative path for each item. |
|Full Path | displays the full path for each item. |
|Refresh Symbol List | refreshes the symbol list for the current project. |
|Refresh All Symbol Lists | refreshes the symbol lists for all projects. |
|Symbol List | shows or hides the symbol list. |
|Configuration | lists the available configurations. |
|Platform | lists the available platforms. |
|Properties for Current Solution Template | displays the properties for the current solution template. |
|Solution Templates | defines solution templates. |
|Plug-in Properties | displays the plug-in properties. |
|List of Tools | runs a specified tool. |

### The Projects plug-in toolbar

|     |     |
| --- | --- |
|![](../../images/newsolution.gif) New Solution | creates a new solution. |
|![](../../images/opensolution.gif) Open Solution | opens an existing solution. |
|![](../../images/runsolution.gif) Run Solution | runs the open solution. |
|![](../../images/parameterinformation.gif) Parameter Information | displays the parameter information. |
|![](../../images/gotodefinition.gif) Go to Definition | causes the cursor to jump to definitions. |
|![](../../images/popbrowsecontent.gif) Pop Browse Context | causes the cursor to return to the previous. |
|![](../../images/symbollist.gif) Symbol List | displays a list of symbols. |
|![](../../images/propertiesforcurrentsolutiontemplate.gif) Properties for Current Solution Template | displays the customizable properties for the current solution template. The General tab includes the Solution Format, File Extension, and Read Only option. The Configurations tab includes Configurations, Platforms, and Macros. The <br> Symbols tab includes, Refresh All Symbol Lists Automatically and Additional Parameters to Ctags. The Tools tab includes customizable tools. The Keyboard page includes the option to assign commands to keyboard shortcuts for this plug-in. |
|![](../../images/solutiontemplates.gif) Solution Templates | displays theSolution Template dialog box. |
|![](../../images/pluginproperties.gif) Plug-in Properties | displays the plug-in Properties. |

### Solution Templates

Every solution you create, open or save in the Projects plug-in belongs to a solution template. Each solution template specifies the associated file extension's characteristics, including solution formats, macros, tools, and keyboard shortcuts.
When you open a solution file, a solution template associated with the file extension is selected and behaves per the characteristics defined for the template.

### Solution Templates dialog box

This dialog box appears when you click the ![](../../images/solutiontemplates.gif) button. Available solution templates are displayed in the list. Click the Properties button to display the properties of the selected solution template.

### Solution Template Properties

General tab

|     |     |
| --- | --- |
|Solution Format | selects a solution format. Currently, onlyEmEditor andVisual Studio can be selected. |
|File Extension | specifies the file extension for solution files. When you open a solution file, a solution template associated with the file extension is selected. |
|Read Only | specifies whether the solution is read only. If you set to read only, you won't be able to add files to the solution, and the project files won't be overridden when a solution is saved. |
|Files to Include | specifies file types that are included when you drag and drop files <br> to a project tree. For example, you would specify "\*.c;\*.cpp" if you <br> would like to include both .c and .cpp files. |
|Files to Exclude | specifies file types that are excluded when you drag and drop files <br> to a project tree. For example, you would specify "\*.com;\*.exe" if <br> you would like to exclude both .com and .exe files. |
|Folder to Exclude | specifies folder names that are excluded when you drag and drop <br> files to a project tree. For example, you would specify <br> "\*folder1;folder2" if you would like to exclude both "folder1" and <br> "folder2" folders. |

Configurations tab

|     |     |
| --- | --- |
|Configurations | selects a defined configuration. Selecting <New> allows you to define a new configuration. Selecting <Edit> allows you to delete a configuration. |
|Platforms | selects a defined platform. Selecting <New> allows you to define a new platform. Selecting <Edit> allows you to delete a platform. |
|Macros | displays the list of defined macros. It allows you to specify a value for each macro and for the combination of each configuration and platform. |
|New | creates a new macro. |
|Delete | deletes a selected macro. |
|Rename | renames a selected macro. |

Symbols tab

|     |     |
| --- | --- |
|Refresh All Symbol Lists Automatically | specifies whether to update the symbol list when a new file is added. |
|Additional Parameters to Ctags (advanced option) | specifies additional parameters to Ctags. This is an advanced option, and setting wrong parameters may prevent the symbol list from working properly. |

Tools tab

|     |     |
| --- | --- |
|Tools | displays the list of defined tools. |
|New | creates a new tool. |
|Delete | deletes the selected tool. |
|Copy | copies the selected tool. |
|Up | moves the selected tool up on the list. |
|Down | moves the selected tool down on the list. |
|Properties | shows or edits the selected tool properties. |

Keyboard page

|     |     |
| --- | --- |
|Commands | lists available commands. |
|Press New Shortcut Key | enter shortcut key for the selected command. |
|Current Keys | current keys assigned to the selected command. |
|Assign | assigns the shortcut key to the currently selected command. |
|Delete | deletes the selected key. |

### Creating Configurations and Macros for Solutions

Under Configurations properties in the Properties for Current Solution Template dialog box, you can create new and edit configurations and macros. To create a new configuration:

1. Click <Default> under configurations, then click <New>.
2. You can specify the configuration name. For example, create a configuration named, Debug.
3. You can create macros for each configuration.
4. Under macros, click New. Name the macro OPTIONS and specify its value as /D \_Debug.
5. Now create another configuration named Release.
6. Under the Release configuration, for the macro named OPTIONS, specify its value as /O1.
7. Now you have specified configurations, and macros for each configuration.

### Creating Tools for Solutions

Under Tools properties, in the Properties for Current Solution Template dialog box, you can create new tools. Tools Properties allows you to specify the Title, Command, Arguments, Initial Directory, Icon Path, and Current Icon, among other
options. The Tools Properties provides some predefined Arguments, such as File Path and Current Line. To create a new tool:

1. Click New in the Tools Properties dialog box.
2. Name the tool, Compile.
3. Specify the Command, for example, C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\bin\\cl.exe.
4. Specify the Argument, for example, $(OPTIONS) $(Path).
5. Specify the Initial Directory, for example, $(Dir).
6. Specify the Icon Path and Current Icon.
7. Click the Saves Files button to direct the tool to save the files.
8. Click the Use Output Bar to specify the desired Output Encoding.
9. When finished, click OK.

### Predefined Arguments

|     |     |
| --- | --- |
|$(Path) | the full path and name of the active document. |
|$(Dir) | the <br> directory of the active document. |
|$(Filename) | the file name of the active document without file extension. |
|$(Ext) | the file <br> extension of the active document. |
|$(RelPath) | the <br> relative path and name of the active document. |
|$(CurLine) | the line <br> number of current line. |
|$(CurText) | the word of <br> the current cursor position. |
|$(Solution) | the full path and name of the solution file. |
|$(Project) | the full path and name of the project file. |
|$(SolutionDir) | the directory of the solution. |
|$(ConfigurationName) | the active configuration name. |
|$(PlatformName) | the active platform name. |
|$(FrameworkSDKDir) | framework <br> SDK directory with trailing backslash. |
|$(VCInstallDir) | the Visual <br> C++ install directory with trailing backslash. |
|$(VSInstallDir) | the Visual <br> Studio install directory with trailing backslash. |
|$(WindowsSdkDir) | the Windows <br> SDK install directory without trailing backslash. |
|$(LatestFrameworkDir) | the <br> Framework directory. |
|$(SourceSafe) | full path and name of Visual SourceSafe executable (ss.exe). |
|$(SccProjectName) | the project <br> name for SourceSafe. |

### Sub Arguments

|     |     |
| --- | --- |
|f | file name without extension. |
|d | directory. |
|x | file extension. |

### Examples

|     |     |
| --- | --- |
|$(Project,d) | returns the directory of the project file. |
|$(Solution,f) | returns the file name without extension of the solution file. |
|$(Solution,f).$(Solution,x) | returns the file name with extension of the solution file. |

## Tips

- Press theF6 key orESC key to set the keyboard focus back to the editor.
- You may saveUntitled Project by right-clicking onUntitled Project, and selectingSave Project As.
