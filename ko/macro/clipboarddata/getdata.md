# getData 메서드 (clipboardData ��ü)

클립보드로부터 지정된 형식 내에서 데이터를 검색합니다.

#### \[JavaScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, _iPos_ );

#### \[VBScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, _iPos_ )

## 매개 변수

_sDataFormat_

다음 데이터 형식 값을 하나 이상 지정하는 문자열입니다.

|     |     |
| --- | --- |
| Text | 텍스트를 포함한 모든 형식을 지정합니다. |
| LineText | 줄 텍스트 형식을 지정합니다. |
| BoxText | 박스 텍스트 형식을 지정합니다. |
| html | HTML 형식을 지정합니다. |

_iPos_

선택 사항입니다. 이전의 클립보드 데이터를 검색하고 싶은 경우, 클립보드 기록 내 위치를 지정합니다.
-1 또는 생략된 경우에는 현재 데이터가 검색됩니다. _sDataFormat_ 매개 변수에 "html"이 지정된 경우에 이 값은 0 또는 -1 이여야만 합니다.

## 예시

#### \[JavaScript\]

str = clipboardData.getData("Text");

#### \[VBScript\]

str = clipboardData.getData("Text")

다음의 매크로는 클립보드 기록을 표시하며 텍스트에 삽입될 항목을 선택합니다.

#### \[JavaScript\]

menu = CreatePopupMenu();

i = 0;

do {

str = clipboardData.getData("text", i);

if( str.length == 0 ) break;

str = str.substr( 0, 40 )

menu.Add( str, i + 100 );

i++;

} while( 1 );

result = menu.Track( 0 );

if( result != 0 ) {

s = clipboardData.getData("text", result - 100);

document.write( s );

}

다음의 매크로는 HTML 형식으로 클립보드 내용을 붙여 넣습니다.

#### \[JavaScript\]

str = clipboardData.getData("html");

document.selection.Text = str;

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.