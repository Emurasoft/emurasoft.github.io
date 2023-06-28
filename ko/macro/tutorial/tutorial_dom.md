# 매크로의 사양 (문서 개체 모델)

엠에디터 매크로 문서 개체 모델 (DOM)의 사양에서, **[Window 개체](../window/index)** 는
현재 범위입니다. 다시 말해, 명시적 범위에 없는 속성과 메서드는 현재
**[Window 개체](../window/index)** 를 참결합니다.
예를 들어, 첫번째 문서는 웹 브라우저에 사용되는 스크립에 적용되는
Window 개체의 **[document 속성](../window/window_document)** 입니다.
웹 브라우서 스크립에 익숙한 사용자들에게는 다음과 같은 코드가 더 친근할 것입니다:

#### \[JavaScript\]

document.write("EmEditor supports macros.");

#### \[VBScript\]

document.write "EmEditor supports macros."

위의 예제들은 같은 결과를 생성합니다;
**[Text 속성](../selection/selection_text)** 과
**[write 메서드](../document/document_write)** 의 동작은 동일합니다.

엠에디터 매크로에서 여러개의 개체를 사용할 수 있습니다.
개체 지향 프로그래밍(OOP)을 얻는것 뿐만 아니라 확장성을 허용하고
단일 매크로에서 여러 창과 문서를 조작하는 것과 같은 미래의 향상된 매크로를 조정하기 위해
이 방법으로 매크로를 디자인 하였습니다.

엠에디터 매크로에서 다음과 같은 개체들을 사용할 수 있습니다:

- **[Window 개체](../window/index)** \-
기본 범위가 되며, 따라서 개체 이름을 지정할 필요가 없습니다.
Windows 사용자 인터페이스에 메서드와 속성을 제공합니다.
**[document 속성](../window/window_document)** 은
현재 문서에 **[Document 개체](../document/index)** 의 속성과 메서드를 사용하도록 합니다.
또한, **[editor 속성](../window/window_editor)** 은
**[Editor 개체](../editor/index)** 에 접근할 수 있도록 합니다.

- **[Document 개체](../document/index)** \-
전체 문서의 요소에 적용하고 문서의 파일이름, 설정 이름, 및 읽기 전용 상태와 같은
파일에 대한 세부 내용을 포함한 열린 문서의 메서드와 속성을 제공합니다.
더 나아가, **[selection 속성](../document/document_selection)** 은 현재 선택된 범위와 커서
위치에 **[Selection 개체](../selection/index)** 를 사용하도록 합니다.

- **[Selection 개체](../selection/index)** \-
현재 선택된 범위와 커서 위치에 메서드와 속성을 제공합니다.
선택된 범위에서 선택 변경, 문자 변환, 커서 이동, 검색, 및 바꾸기와 같은 많은 메서드와 속성을 제공합니다.

- **[Editor 개체](../editor/index)** \- EmEditor
전체적인 엠에디터 응용 프로그램에 메서드와 속성을 제공합니다.
예를 들어, 엠에디터 실행 파일의 버전과 경로를 제공하고, 새로운 파일이나 지정된 파일을 여는데 사용되는
메서드와 속성을 제공합니다.

## 다음 항목: