# Editor 개체

## 속성

|     |     |
| --- | --- |
| **[ActiveDocument](editor_activedocument)** | 현재 문서의 Document 개체를 검색합니다. |
| **[Configs](configs)** | Configs 컬렉션을 검색합니다. |
| **[Documents](editor_documents)** | 현재 열려있는 문서를 위한 Documents 컬렉션을 검색합니다. |
| **[EnableTab](editor_enabletab)** | 탭이 활성화되어 있는지 여부를 설정하거나 검색합니다. |
| **[FullName](editor_fullname)** | 경로를 포함한 엠에디터 실행 파일 (emeditor.exe)의 전체 사양을 검색합니다. |
| **[Version](editor_version)** | 현재 엠에디터 버전을 나타내는 문자열을 검색합니다. |

## 메서드

|     |     |
| --- | --- |
| **[ExecuteCommandByID](editor_executecommandbyid)** | 명령 ID를 나타내는 정수로 식별된 명령을 실행합니다. |
| **[FileDialog](filedialog)** | 사용자가 드라이브, 디렉터리, 및 열 파일의 이름을 지정하도록 하는<br> 열기 또는 다른이름으로 저장 대화 상자를 표시합니다. |
| **[FindInFiles](editor_findinfiles)** | 일치하는 문자열을 위해 여러 파일을 검색합니다. |
| [**GetProfileInt**](getprofileint) | 엠에디터의 설정에 따라 레지스트리 또는 INI 파일로부터<br> 지정된 엔트리의 정수 값을 검색합니다. |
| [**GetProfileString**](getprofilestring) | 엠에디터의 설정에 따라 레지스트리 또는 INI 파일로부터<br> 지정된 엔트리의 문자열 값을 검색합니다. |
| **[NewFile](editor_newfile)** | 새로운 파일을 생성합니다. |
| **[OpenFile](editor_openfile)** | 기존 파일을 엽니다. |
| **[QueryStatusByID](editor_querystatusbyid)** | 활성화되고 있으며 선택되어 있는지 지정된 명령의 현재 상태를 검색합니다. |
| **[QueryStringByID](editor_querystringbyid)** | 지정된 명령과 연관된 문자열을 검색합니다. |
| **[ReplaceInFiles](editor_replaceinfiles)** | 여러 파일 내에서 텍스트를 대체합니다. |
| **[SaveAll](editor_saveall)** | 현재 열려있는 파일들을 모두 저장합니다. |
| **[SaveCloseAll](editor_savecloseall)** | 열려있는 모든 파일을 저장하고 닫습니다. |
| [**WriteProfileInt**](writeprofileint) | 엠에디터 설정에 따라 레지스트리 또는 INI 파일에 정수 값을 설정합니다. |
| [**WriteProfileString**](writeprofilestring) | 엠에디터 설정에 따라 레지스트리 또는 INI 파일에 문자열 값을 설정합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.


```{toctree}
:hidden:
:maxdepth: 1
configs
editor_activedocument
editor_documents
editor_enabletab
editor_executecommandbyid
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
getprofileint
getprofilestring
writeprofileint
writeprofilestring
```
