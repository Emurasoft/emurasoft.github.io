# HighlightList 컬렉션

HighlightList 컬렉션은 [HighlightItem 개체](../highlight_item/index) 의 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](count)** | 항목의 수를 검색합니다. |
| **[Item](item)** | 지정된 인덱스를 위한 [HighlightItem 개체](../highlight_item/index) 를 검색합니다. |

## 메서드

|     |     |
| --- | --- |
| **[Add](add)** | 항목을 추가합니다. |
| **[Remove](remove)** | 항목을 제거합니다. |

## 예시

### \[JavaScript\]

```
list = new Enumerator( document.Config.Highlight.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.Highlight.List
alert item.Name
Next
```

## 버전

Supported on EmEditor Professional Version 7.00 또는 later.


```{toctree}
:maxdepth: 1
add
count
item
remove
```
