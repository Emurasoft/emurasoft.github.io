# Documents 컬렉션

Documents 컬렉션은 프레임 창에 document 개체의 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](documents_count)** | 문서의 수를 검색합니다. |
| **[Item](documents_item)** | 지정된 인덱스의 문서를 위한 document 개체를 검색합니다. |

## 예시

### \[JavaScript\]

```
docs = new Enumerator( editor.Documents );
for( ; !docs.atEnd(); docs.moveNext() ){
doc = docs.item();
alert( doc.Name );
}
```

### \[VBScript\]

```
For Each doc In editor.Documents
alert doc.FullName
Next
```

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.


```{toctree}
:hidden:
:maxdepth: 1
documents_count
documents_item
```
