# 在文件中替换

要在文件中替换，用 [ReplaceInFiles 方法](../editor/editor_replaceinfiles).

下面的例子演示了如何在 HTML 文件中用替换 <H4> ... </H4> 替换 <H3> ... </H3>。

#### \[JavaScript\]

editor.ReplaceInFiles( "<H3>(.\*?)</H3>", "<H4>\\\1<H4>", "C:\\\web\\\\*.htm", eeFindReplaceRegExp
\| eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\\Backup" );

#### \[VBScript\]

editor.ReplaceInFiles "<H3>(.\*?)</H3>", "<H4>\\1<H4>", "C:\\web\\\*.htm", eeFindReplaceRegExp
Or eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\Backup"