# KeyboardList 컬렉션

KeyboardList 컬렉션은 [KeyboardItem 개체](../keyboard_item/index) 의 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](count)** | 항목의 수를 검색합니다. |
| **[Item](item)** | 지정된 인덱스를 위해 [KeyboardItem 개체](../keyboard_item/index) 를 검색합니다. |

## 메서드

|     |     |
| --- | --- |
| **[Add](add)** | 항목을 추가합니다. |
| **[Remove](remove)** | 항목을 제거합니다. |

## 예시

#### \[JavaScript\]

list = new Enumerator( document.Config.Keyboard.List );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Key );

}

#### \[VBScript\]

For Each item In document.Config.Keyboard.List

alert item.Key

Next

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.


```{toctree}
:maxdepth: 1
add
count
item
remove
```
