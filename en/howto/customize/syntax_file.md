# To Create a New Syntax File

1. First export a current syntax file so you have a structure to work with.
To export a current syntax file, select a configuration that offers syntax
highlighting such as Perl. Select **Properties for Current Configuration**
from the **Tools** menu and select the **Highlight** **(1)** tab.
Click on the **Export** button, select the location where you would like to
save the syntax file, and give it a descriptive name.
2. Open the exported syntax file and note the structure. You will want to
specify some of the options as well as replace the existing keywords with
keywords specific to the new syntax file you are creating. An explanation of
the options, which correspond to the settings on the **Highlight (1)** and
**Highlight (2)** pages in **Properties for Current Configuration**,
follows:

|     |     |
| --- | --- |
| #Highlight= | Either **on** or **off** depending on whether or not <br> you want to highlight syntax. |
| #BeginTag= | Specify the character used as an opening tag. For example, <br> < for HTML syntax. |
| #EndTag= | Specify the character used as a closing tag. For example, <br> \> for HTML syntax. |
| #CommentBegin= | Specify the character(s) used to mark the beginning of <br> comments. For example, /\* for C++ syntax. |
| #CommentEnd= | Specify the character(s) used to mark the end of comments. <br> For example, \*/ for C++ syntax. |
| #LineComment1= | Specify the character(s) used to mark line comments. For <br> example, // for C++ syntax. |
| #LineComment2= | Specify additional character(s) used to mark line <br> comments. |
| #SingleQuote= | Either **on** or **off** depending on whether or not <br> you want text strings enclosed in single quote marks to be highlighted. |
| #DoubleQuote= | Either **on** or **off** depending on whether or not <br> you want text strings enclosed in double quote marks to be highlighted. |
| #ContinueQuote= | Either **on** or **off** depending on whether or not you want text <br> strings enclosed in quotes to span lines. |
| #Escape= | Specify the character used as an escape for quote marks. |
| #ScriptBegin= | Specify the character(s) used to mark the beginning of a <br> script. |
| #ScriptEnd= | Specify the character(s) used to mark the end of a script. |
| #SpecialSyntax= | Specify **HTML**, **HTML-Embedded**, or **off** <br> depending on the mix of HTML and script languages, if any, in the same <br> document. <br> <br>- **HTML** is used when HTML tags specifying the script <br>   language ( **<SCRIPT type=...>**) exist in the **HTML** document. <br>   HTML is also appropriate for ASP files that include scripts beginning with <br>   the <% mark. This is usually the case for VBScript, JavaScript, PerlScript, <br>   CSS, etc. <br>- **HTML-Embedded** is appropriate when working with script <br>   languages such as PHP or JSP and the characters that normally mark the <br>   beginning of scripts in such languages are specified with #ScriptBegin. |
| #HighlightBraces= | Either **on** or **off** depending on whether or not <br> you want braces to be highlighted. |
| #Keyword= | #Keyword options include:<br>- **color** = Specify the <br>   color of the highlight. You can preview the color choices on the **Display** tab<br>   in <br>   **Properties for Current Configuration**. If you <br>   scroll through the list located there you will notice Highlight (1) - <br>   (10).<br>- **word** = Specifying **on** will highlight keywords only if they <br>   are whole words. For example, if the keyword is run and you specify **word=on**, the <br>   **run** portion of **runner** will not be <br>   highlighted.<br>- **rightall** = Either **on** or **off** depending on whether or <br>   not you want to highlight everything to the right of a keyword match in <br>   addition to the keyword.<br>- **case** = Either **on** or **off** depending on whether or not <br>   you want to enable case sensitivity for keyword matches.<br>- **insidetag** = Specifying **on** will highlight keywords only if <br>   they occur within tags.<br>- **regexp=** Specifying **on** will highlight keywords matched <br>   by using a regular expression. |

3. Once you have completed and saved your syntax file you can create a new
configuration and import the newly created syntax file or import the newly
created syntax file into an existing configuration.

## Tips

- In the syntax file, the escape character is ' **^**', and the following three characters must be escaped: ' **#**', ' **;**', and ' **^**' itself.
