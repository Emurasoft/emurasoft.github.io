# NoWrapList 컬렉션

NoWrapList 컬렉션은 [NoWrapItem 개체](../no_wrap_item/index) 의 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](count)** | 항목의 수를 검색합니다. |
| **[Item](item)** | 지정된 인덱스를 위한 [NoWrapItem 개체](../no_wrap_item/index) 를 검색합니다. |

## 메서드

|     |     |
| --- | --- |
| **[Add](add)** | 항목을 추가합니다. |
| **[Remove](remove)** | 항목을 제거합니다. |

## 예시

### \[JavaScript\]

```
list = new Enumerator( document.Config.NoWrap.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.NoWrap.List
alert item.Name
Next
```

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.


```{toctree}
:maxdepth: 1
add
count
item
remove
```
