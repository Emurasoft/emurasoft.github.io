# EP\_SET\_UNINSTALL

플러그 인을 제거합니다.

EP\_SET\_UNINSTALL

hwnd = hwndParent;

wParam = (WPARAM) (LPTSTR) pszUninstallCommand;

lParam = (LPARAM) (LPTSTR) pszUninstallParam;

## 매개 변수

_hwndParent_

> 플러그 인 설정 대화 상자의 창 핸들입니다.

_pszUninstallCommand_

> 반환 값이 UNINSTALL\_RUN\_COMMAND일 때 실행할 명령을 지정합니다.

_pszUninstallParam_

> 반환 값이 UNINSTALL\_RUN\_COMMAND일 때 실행할 명령의 매개 변수를 지정합니다.

## 반환 값

> 반환 값은 다음의 값 중 하나입니다.
>
> |     |     |
> | --- | --- |
> | UNINSTALL\_FALSE | 제거하지 않습니다. |
> | UNINSTALL\_SIMPLE\_DELETE | 플러그 인 DLL파일을 간단히 제거합니다. |
> | UNINSTALL\_RUN\_COMMAND | 지정된 명령을 실행합니다. |
>
> 반환 값이 TRUE인 경우, 플러그 인이 제거됩니다. 반환 값이 FALSE인 경우 플러그 인은 제거되지 않습니다.

## 버전

> 버전 3 이상에서만 지원됩니다.
> 하지만, 반환 값 UNINSTALL\_RUN\_COMMAND 와 pszUninstallCommand 매개변수와 pszUninstallParam 매개변수는
> EmEditor 버전 6 이상에서만 지원됩니다.
