# AssociationList 컬렉션

AssociationList 컬렉션은 [AssociationItem 개체](../association_item/index) 의 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](count)** | 항목의 수를 검사합니다. |
| **[Item](item)** | 지정된 인덱스의 [AssociationItem 개체](../association_item/index) 를 검사합니다. |

## 메서드

|     |     |
| --- | --- |
| **[Add](add)** | 항목을 추가합니다. |
| **[Remove](remove)** | 항목을 제거합니다. |

## 예시

### \[JavaScript\]

```
list = new Enumerator( document.Config.Association.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.Association.List
alert item.Name
Next
```

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.


```{toctree}
:hidden:
:maxdepth: 1
add
count
item
remove
```
