# Configs 컬렉션

Configs 컬렉션은 [**Config** 개체](../config/index) 의 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](count)** | 구성의 수를 검색합니다. |
| **[Item](item)** | 지정된 인덱스의 구성을 위한 [**Config** 개체](../config/index) 를 검색합니다. |

## 예시

### \[JavaScript\]

```
cfgs = new Enumerator( editor.Configs );
for( ; !cfgs.atEnd(); cfgs.moveNext() ){
cfg = cfgs.item();
alert( cfg.Name );
}
```

### \[VBScript\]

```
For Each cfg In editor.Configs
alert cfg.Name
Next
```

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.


```{toctree}
:hidden:
:maxdepth: 1
count
item
```
