# Text 속성 (Selection 개체)

선택된 텍스트를 검색하거나 현재 위치에 문자열을 삽입합니다.

## 

### \[JavaScript\]

```
str = document.selection.Text;
document.selection.Text = str;
```

### \[VBScript\]

```
str = document.selection.Text
document.selection.Text = str
```

## 예시

### \[JavaScript\]

```
str = document.selection.Text;
alert( "The selected text is " + str );
document.selection.Text = "Hello";
```

### \[VBScript\]

```
str = document.selection.Text
alert "The selected text is " & str
document.selection.Text = "Hello"
```

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
