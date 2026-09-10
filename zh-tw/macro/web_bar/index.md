# WebBar 對象

## 屬性

|     |     |
| --- | --- |
| **[scrollX](scrollx)** | 傳回捲動條的水平位置。 |
| **[scrollY](scrolly)** | 傳回捲動條的垂直位置。 |
| **[Visible](visible)** | 顯示或隱藏網頁瀏覽器。 |

## 方法

|     |     |
| --- | --- |
| **[Open](open)** | 打開指定 URL 的網站。 |
| **[scrollBy](scrollby)** | 依指定的相對距離捲動視窗。 |
| **[scrollTo](scrollto)** | 將視窗捲動到指定的位置。 |
| **[SetFocus](set_focus)** | 將鍵盤焦點設定到網頁瀏覽器。 |

## 範例

### \[JavaScript\]

```
WebBar.Open( "https://www.emeditor.com/" );
WebBar.SetFocus();
```

### \[VBScript\]

```
WebBar.Open "https://www.emeditor.com/"
WebBar.SetFocus
```

## 版本

支持 EmEditor Professional 版 23.0 或之後的版本。


```{toctree}
:hidden:
:maxdepth: 1
scrollx
scrolly
visible
open
scrollby
scrollto
set_focus
```
