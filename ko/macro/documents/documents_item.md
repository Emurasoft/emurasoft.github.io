# Item 속성 (Documents 컬렉션)

지정된 인덱스의 문서를 위한 document 개체를 검색합니다.

## 

### \[JavaScript\]

```
doc = editor.Documents.Item( Index );
```

### \[VBScript\]

```
doc = editor.Documents.Item( Index )
```

## 매개 변수

_Index_

문서의 인덱스를 1로 시작하는 정수로 지정합니다.

## 예시

### \[JavaScript\]

```
alert( "Full Name for the first document: " + editor.Documents.Item(1).FullName );
```

### \[VBScript\]

```
alert "Full Name for the first document: " & editor.Documents.Item(1).FullName
```

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.
