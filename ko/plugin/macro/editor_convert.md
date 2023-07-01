# Editor\_Convert

문자를 변환합니다. 이 인라인 함수를 사용하거나
[EE\_CONVERT](../message/ee_convert) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_Convert( HWND hwnd, UINT nFlags );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nFlags_

> 다음의 값들의 결합을 지정할 수 있습니다.
>
> |     |     |
> | --- | --- |
> | **값** | **의미** |
> | FLAG\_MAKE\_LOWER | 소문자로 변환합니다. |
> | FLAG\_MAKE\_UPPER | 대문자로 변환합니다. |
> | FLAG\_HAN\_TO\_ZEN | 전자 문자로 변환합니다. |
> | FLAG\_ZEN\_TO\_HAN. | 반자 문자로 변환합니다. |
> | FLAG\_CAPITALIZE | 각 단어의 첫 문자를 대문자로 변환합니다. |
> | FLAG\_CONVERT\_SELECT\_ALL | 전체 텍스트를 변환합니다. 플래그가 설정되지 않은 경우, EE\_CONVERT는<br> 선택 영역안의 문자만을 변환합니다. |
> | FLAG\_CONVERT\_KATA | 가타카나로 변환합니다. |
> | FLAG\_CONVERT\_ALPHANUMERIC | 알파벳과 숫자로 변환합니다. |
> | FLAG\_CONVERT\_MARK | 마크로 변환합니다. |
> | FLAG\_CONVERT\_SPACE | 공백으로 변환합니다. |
> | FLAG\_CONVERT\_KANA\_MARK | 가나 마크로 변환합니다. |

## 반환 값

> 메시지가 성공한 경우,반환 값은 0 이 아닙니다.메시지가 실패한 경우,반환 값은 0입니다.
