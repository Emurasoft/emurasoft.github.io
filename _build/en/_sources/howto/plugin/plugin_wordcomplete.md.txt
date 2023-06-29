# To Use Word Complete Plug-in

The **Word Complete** plug-in is installed by default with EmEditor Professional. As you type in the document, this plug-in displays the list filled with previously used words and highlighted words defined in EmEditor, and lets you select a
word from the list to complete your typing.

The Word Complete plug-in can also complete recently searched strings. This process works the same as completing words, but instead of completing words, the plug-in completes strings.

To use the Word Complete plug-in:

1. Click ![](../../images/wordcomplete.gif) on the **Plug-Ins** bar. Or on the Tools menu, point to **Plug-ins**, and then click **Word Complete** so that it is checked.
2. Type the first few characters of the word you want to insert into the document, and a list filled with previously used words and highlighted words defined in EmEditor will appear.
3. Use the **UP** or **DOWN** key to select the word to insert, and press **Enter**.

## Plug-in Properties

### Dictionaries

|     |     |
| --- | --- |
| **Highlight Words** | The strings defined in the **Highlight (1) page** of Configuration Properties are used as the candidates. |
| **Used Words in Document** | The words in the current document are used as the candidates. |
| **Limit Lines** | Limits words within the specified lines before and after the current cursor position. |
| **Include Previous Document** | Includes the previous document for the candidate list. |
| **Include All Documents in Group** | Includes all the documents in the same group window. |
| **Only if Same Configuration** | Includes all the documents but only with the same configuration as the current document. |
| **Words in Dictionary File** | The words in a separate file are used as the candidates. |
| **Dictionary File** | Specifies the full path and the file name of a separate file that should be used as the candidate list. |
| **Free Format (if not checked, line by line)** | Specifies that any files containing words separated by spaces can be used as dictionary files. If not checked, each word must be separated by a newline character. |
| **Clipboard Contents** | The words in the Clipboard are used as the candidates. |
| **File Names** | File names within the same folder as the current document are used as the candidates. |
| **Searched Strings** | Shows the history of strings searched for in the past. |
| **Refresh Rate** | Specifies how often the candidates are refreshed so the candidate list is updated with recently typed words. The higher this rate is, the fewer characters must be typed before the list is updated. |

### Matching Criteria

|     |     |
| --- | --- |
| **Match Case** | Specifies whether a case should be matched. For instance, suppose **ABC** and **abc** are found in the current document (or a dictionary file). If **Never** is selected, either **ABC** or **abc** can be <br> used as a candidate, and typing either **A** or **a** displays either **ABC** or **abc**, whichever the first one loaded. If **Only in Candidates** is selected, both **ABC** and **abc** <br> are used as a candidate, and typing **A** or **a** displays both **ABC** and **abc**. If **Both in Candidates and in Typing** is selected, both **ABC** and<br> **abc** are used as a candidate, but typing **A** displays only **ABC**, and typing **a** displays only **abc**. If **Never and Keep Original Text when Completes** is selected, the behavior is the same as **Never** except that typing **A** and selecting **abc** in the candidate list will yield **Abc**. |
| **Priority** | If **Last Used Word First** is selected, the last selected word will be initially selected when the candidate list is displayed. If **Alphabetical Order** is selected, the top item of the matched items will be <br> initially selected. |
| **Word Type** | If **Normal Words** is selected, each word begins with an alphabet and ends with alphabets or numbers. If **Dot Syntax** is selected, each word can include a dot ( **.**). If **HTML/XML** <br> is selected, each word can begin with **<** or **&**, can contain **/** or **-** in the middle of the word, and can end with **>** or **;**. If<br> **Custom** is selected, a user can define how words can be listed in the text boxes below. |
| **First Characters** | If **Custom** is selected in the **Word Type** drop-down list, enters first character that each word can begin with, in addition to alphabets. |
| **Mid Characters** | If **Custom** is selected in the **Word Type** drop-down list, enters characters that each word can contain between the first character and the last character, in addition to alphabets and numbers. |
| **Last Characters** | If **Custom** is selected in the **Word Type** drop-down list, enters last character that each word can end with, but should not contain in the first or mid characters. |

### Options

|     |     |
| --- | --- |
| **Display Icons in the Candidate List** | Displays small icons at the left of each item in the candidate list. |
| **Automatically Complete when Only One Candidate is Available** | Allows the plug-in to complete automatically when a user presses the keyboard shortcut assigned to **Show Candidates Manually** (typically **CTRL** + **SPACE**) if only one item is available for <br> the candidates. |
| **Use Highlight Colors in the Candidate List** | Colors the candidate list with colors defined as highlighted strings. |
| **Automatically Hide the List when No Candidate List** | Automatically hides the candidate list if no item matches when you type. |
| **Show Only Matched Words in the Candidate List** | Limits the candidate list only to matched words. |
| **Exclude Matched and Same-Length Word from the Candidate List** | Automatically excludes matched words with the same length as the typed word. |
| **Automatically Show the Candidate List as Typed** | Automatically displays the candidate list as you type. |
| **Number of Characters** | Number of characters typed before the plug-in displays the candidate list automatically. |
| **Delay Time** | Time that the plug-in waits until it displays the candidate list automatically after it finds matched words. |

### Keyboard

|     |     |
| --- | --- |
| **Commands** | Lists available commands. |
| **Press New Shortcut Key** | Enter shortcut key for the selected command. |
| **Current Keys** | Current keys assigned to the selected command. |
| **Description** | Description for the selected command. |

## Tips

By default, EmEditor monitors the keystrokes and automatically display the list when you start typing a word. To disable this behavior, right-click the plug-in button on the **Plug-ins** bar, select the **Properties**, and clear the **Automatically Show the Candidate List as Typed** check box. You can still display the list by pressing the keyboard
shortcut. The default keyboard shortcut is **CTRL + SPACE,** but you can assign another keyboard shortcut by selecting the Keyboard page on the **Properties**. The options in the **plug-in Properties** can be
set for each configuration.