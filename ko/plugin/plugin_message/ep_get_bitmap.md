# EP\_GET\_BITMAP

도구 모음에 표시되는 플러그 인의 다양한 크기와 색 농도를 위해 비트맵 resource IDs를 검색합니다.

EP\_GET\_BITMAP

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## 매개 변수

_hwndParent_

EmEditor 프레임 창의 창 핸들입니다.

_flags_

검색할 비트맵의 색 농도와 비트맵 크기를 지정합니다. 다음의 flag들의 결합입니다.

|     |     |
| --- | --- |
| **값** | **의미** |
| BITMAP\_SMALL | 스몰 비트맵 (16x16 픽셀) |
| BITMAP\_LARGE | 라지 비트맵 (24x24 픽셀) |
| BITMAP\_16\_COLOR | 16 색상 비트맵 |
| BITMAP\_24BIT\_COLOR | 24비트 색상 (트루 컬러) 비트맵 |
| BITMAP\_256\_COLOR | 256 색상 비트맵 |
| BITMAP\_DEFAULT | 기본 상태 비트맵 |
| BITMAP\_DISABLED | 비활성화 상태 비트맵 |
| BITMAP\_HOT | 핫 상태 비트맵 |

## 반환 값

필요한 크가와 색농도의 비트맵 resource ID를 반환해야 합니다. 반환 값이 0인경우, EmEditor는 스몰 16 색상
비트맵을 검색하기 위해 GetBitmapID 내보내기 기능을 사용합니다.
