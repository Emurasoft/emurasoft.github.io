# ファイルから置換する ()

指定するパスの複数のファイルから文字列を置換するには、 [ReplaceInFiles \
メソッド](../editor/editor_replaceinfiles) を利用します。

この例では、HTMLファイルの <H3> ... </H3> を <H4> ... </H4> に置換します。

#### \[JavaScript\]

editor.ReplaceInFiles( "<H3>(.\*?)</H3>", "<H4>\\\1<H4>", "C:\\\web\\\\*.htm", eeFindReplaceRegExp
\| eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\\Backup" );

#### \[VBScript\]

editor.ReplaceInFiles "<H3>(.\*?)</H3>", "<H4>\\1<H4>", "C:\\web\\\*.htm", eeFindReplaceRegExp
Or eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\Backup"