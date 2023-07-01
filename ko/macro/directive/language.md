# \#language 지침서 (Script ��ħ��)

사용할 스크립트 언어를 지정합니다. 이것을 지정함으로 JavaScript 과 VBScript 이외의
ActiveScript 언어가 사용됩니다. 이 지침서는 메인 기본 코드 위 스크립트의 첫 줄에 지정되어야 합니다.

#language = "ScriptName"

## 매개 변수

_ScriptName_

> ProgID를 사용하여 스크립트 언어를 지정합니다. 이 스크립트가 사용되기 이전에
> 스크립트 엔진이 설치되어야 합니다.

## 예시

다양한 스크립트 언어를 사용하여 커서 위치에 "Hello!"를 삽입합니다.

#### \[PerlScript\]

#language = "PerlScript"

$Window->document->write( 'Hello!' );

#### \[PHPScript\]

#language = "PHPScript"

$Window->document->write( "Hello!" );

#### \[Python\]

#language = "Python"

Window.document.write( 'Hello' );

#### \[RubyScript\]

#language = "RubyScript"

Window.document.write( "Hello!" );

위에서 나열되지 않은 다른 언어를 사용하기 원하는 경우에는,
레지스트리 편집기 (regedit.exe)를 사용하고 {F0B7A1A2-9847-11CF-8F20-00805F2CD064} 키를 검색합니다.
검색한 키가 원하는 스크립트 언어에 해당하는 경우 그 언어에 대한 ProgID를 찾을 수 있습니다.

## 참고

JavaScript 또는 VBScript 이외의 스크립트 언어를 사용하는 경우,
("ee"로 시작하는) 매크로 상수는 정의되지 않습니다.
이러한 상수를 사용하려면 정수 값으로 상수들을 지정해야 합니다.
예를 들어, 이러한 값들은 JavaScript로 다음의 줄을 실행하여 검색할 수 있습니다:

alert( eeEncodingSystemDefault );

이러한 상수 값은 차후에 변경될 수 있습니다.

매크로는 JavaScript 와 VBScript를 제외한 다른 스크립트 언어로는 자동으로 녹화될 수 없습니다.
JavaScript 또는 VBScript 이외의 다른 스크립트 언어로 쓰는 법은 지원되지 않습니다.

## 버전

엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.
