# FileDialog 메서드

사용자가 드라이브, 디렉터리, 및 열 파일의 이름을 지정하도록 하는 열기 또는 다른이름으로 저장 대화 상자를 표시합니다.

#### \[JavaScript\]

_strFileName_ = editor. **FileDialog**( _nType_ \[, _nFlags_ \[, _strTitle_ \[, _strFilter_ \[, _nDefFilterIndex_ \[, _strDefPath_ \[, _strDefFolder_ \[, _strDefExt_ \]\]\]\]\]\]\] );

#### \[VBScript\]

_strFileName_ = editor. **FileDialog**( _nType_ \[, _nFlags_ \[, _strTitle_ \[, _strFilter_ \[, _nDefFilterIndex_ \[, _strDefPath_ \[, _strDefFolder_ \[, _strDefExt_ \]\]\]\]\]\]\] )

## 매개 변수

_nType_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| eeFileDialogOpen | 열기 대화 상자를 생성합니다. |
| eeFileDialogSaveAs | 다른 이름으로 저장 대화 상자를 생성합니다. |

_nFlags_

선택 사항입니다. 다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| eeFileDialogCreatePrompt | 사용자가 존재하지 않는 파일을 지정하는 경우, 이 플래그가 사용자에게 파일을 생성하는 권한을 확인하는<br> 대화 상자를 표시하게 합니다. |
| eeFileDialogDontAddToRecent | 사용자의 가장 최근 사용한 문서를 포함하는<br> 파일 시스템 디렉토리에서 선택된 파일에 링크를 추가하는 것으로부터 시스템을 방지합니다. |
| eeFileDialogFileMustExist | 사용자가 **파일 이름** 입력 칸에 존재하는 파일의 이름만을 입력할 수 있도록 지정합니다.<br> 이 플래그가 지정되고 사용자가 유효하지 않은 이름을 입력하는 경우, 대화 상자 프로시저가 메시지 박스에 경고문을 표시합니다.<br> 이 플래그가 지정된 경우, eeFileDialogPathMustExist 플래그도 사용됩니다. |
| eeFileDialogNoChangeDir | 사용자가 파일을 검색하는 동안 디렉토리를 변경한 경우<br> 현재 디렉토리를 기존의 값으로 복원합니다. |
| eeFileDialogNoDereferenceLinks | 선택된 바로가기 (.LNK) 파일의 파일 이름과 경로를 반환하는 대화 상자를 지시합니다.<br> 이 값이 지정되지 않은 경우, 대화 상자는 바로가기에 의해 참조되는 파일의 파일 이름과 경로를<br> 반환합니다. |
| eeFileDialogNoNetworkButton | **네트워크** 버튼을 숨기고 비활성화 합니다. |
| eeFileDialogNoReadOnlyReturn | 반환된 파일이 **읽기 전용** 체크 박스가 선택되어 있지 않고,<br> 쓰기 보호 디렉토리가 되지 않게 지정합니다. |
| eeFileDialogNoTestFileCreate | 대화 상자를 닫기 전에 파일이 생성되지 않도록 지정합니다. |
| eeFileDialogNoValidate | 일반 대화상자가 반환된 파일 이름에 유효하지 않은 문자를 허용하도록 지정합니다. |
| eeFileDialogOverwritePrompt | 선택된 파일이 이미 존재하는 경우, 메시지 상자를 생성하는<br> **다른 이름으로 저장** 대화 상자를 발생합니다. |
| eeFileDialogPathMustExist | 사용자가 유효한 경로와 파일 이름만을 입력할수 있도록 지정합니다. |
| eeFileDialogShareAware | 기능이 네트워크 공유 위반 때문에 실패한 경우, 오류를 무시하고 대화상자가<br> 선택된 파일 이름을 반환하도록 지정합니다. |

_strTitle_

선택 사항입니다. 대화 상자의 제목을 지정합니다. 빈 문자열인 경우, 기본 제목
( **열기** 또는 **다른 이름으로 저장**)이 사용됩니다.

_strFilter_

선택 사항입니다. 필터를 지정합니다. 문자열을 반드시 다음과 같은 형식이어야 합니다:

"Text Files\|\*.txt\|All Files\|\*.\*\|\|"

빈 문자열인 경우, 필터가 사용되지 않습니다.

_nDefFilterIndex_

선택 사항입니다. 처음에 선택한 필터의 한 기본 색인을 지정합니다.

_strDefPath_

선택 사항입니다. 처음에 선택한 경로를 지정합니다.

_strDefFolder_

선택 사항입니다. 처음에 선택한 폴더를 지정합니다.

_strDefExt_

선택 사항입니다. 기본 파일 확장자를 지정합니다.

## 반환 값

성공 시 선택한 파일의 전체 경로와 이름을 반환합니다.
사용자가 **취소** 버튼을 선택한 경우 빈 문자열을 반환합니다.

## 버전

엠에디터 프로페셔널 버전 8.00 이상에서만 지원됩니다.