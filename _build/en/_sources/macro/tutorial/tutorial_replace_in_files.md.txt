# 多檔取代

要多檔取代，用 [ReplaceInFiles 方法](../editor/editor_replaceinfiles).

下面的例子演示了如何在 HTML 檔案中用取代 <H4> ... </H4> 取代 <H3> ... </H3>。

#### \[JavaScript\]

editor.ReplaceInFiles( "<H3>(.\*?)</H3>", "<H4>\\\1<H4>", "C:\\\web\\\\*.htm", eeFindReplaceRegExp
\| eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\\Backup" );

#### \[VBScript\]

editor.ReplaceInFiles "<H3>(.\*?)</H3>", "<H4>\\1<H4>", "C:\\web\\\*.htm", eeFindReplaceRegExp
Or eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\Backup"