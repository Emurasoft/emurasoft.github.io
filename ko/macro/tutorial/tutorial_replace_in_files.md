# 파일 내 바꾸기 (튜토리얼)

경로에 지정된 파일 내에서 문자열을 대체하려면,
[ReplaceInFiles 메서드](../editor/editor_replaceinfiles) 를 사용합니다.

다음의 예문은 HTML 파일 내에서 <H3> ... </H3>을
<H4> ... </H4>로 대체하는 법을 나타냅니다.

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
