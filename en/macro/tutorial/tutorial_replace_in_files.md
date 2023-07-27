# Replace in Files (Tutorial)

To replace a string within specified files in a path, use [ReplaceInFiles Method](../editor/editor_replaceinfiles).

The following example demonstrates how to replace <H3> ... </H3> in a HTML file with <H4> ... </H4>.

## \[JavaScript\]

```
editor.ReplaceInFiles( "<H3>(.\*?)</H3>", "<H4>\\\1<H4>", "C:\\\web\\\\*.htm", eeFindReplaceRegExp
\| eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\\Backup" );
```

## \[VBScript\]

```
editor.ReplaceInFiles "<H3>(.\*?)</H3>", "<H4>\\1<H4>", "C:\\web\\\*.htm", eeFindReplaceRegExp
Or eeReplaceBackup, eeEncodingSystemDefault, "\*.bak", "C:\\Backup"
```
