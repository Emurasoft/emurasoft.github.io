# DroppedFiles 컬렉션

DroppedFiles 컬렉션은 프레임 창에 삭제된 파일의 이름 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](count)** | 삭제된 파일의 이름을 검색합니다. |
| **[Item](item)** | 지정된 인덱스의 삭제된 파일을 위해 파일 이름을 검색합니다. |

## 예시

#### \[JavaScript\]

files = new Enumerator( DroppedFiles );

for( ; !files.atEnd(); files.moveNext() ){

alert( files.item() );

}

#### \[VBScript\]

For Each str In DroppedFiles

alert str

Next

## 버전

엠에디터 프로페셔널 버전 8.00 이상에서만 지원됩니다.

```{toctree}
:maxdepth: 1
count
item
```
