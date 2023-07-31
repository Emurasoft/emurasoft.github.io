# OutputBar 개체

## 속성

|     |     |
| --- | --- |
| **[CurrentDirectory](current_directory)** | 출력 모음의 현재 디렉토리를 설정합니다. |
| **[Visible](visible)** | 출력 모음을 보이거나 숨깁니다. |

## 메서드

|     |     |
| --- | --- |
| **[Clear](clear)** | 출력 모음의 내용을 지웁니다. |
| **[SetFocus](set_focus)** | 출력 모음에 키보드 포커스를 설정합니다. |
| **[write](write)** | 출력 모음에 문자열을 추가합니다. |
| **[writeln](writeln)** | 출력 모음에 문자열과 새로운 줄을 추가합니다. |

## 예시

### \[JavaScript\]

```
OutputBar.Clear();
OutputBar.writeln( "Hello!" );
OutputBar.Visible = true;
OutputBar.SetFocus();
```

### \[VBScript\]

```
OutputBar.Clear
OutputBar.writeln "Hello!"
OutputBar.Visible = True
OutputBar.SetFocus
```

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.


```{toctree}
:hidden:
:maxdepth: 1
clear
current_directory
set_focus
visible
write
writeln
```
