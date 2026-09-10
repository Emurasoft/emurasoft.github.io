# WebBar 对象

## 属性

|     |     |
| --- | --- |
| **[scrollX](scrollx)** | 返回滚动条的水平位置。 |
| **[scrollY](scrolly)** | 返回滚动条的垂直位置。 |
| **[Visible](visible)** | 显示或隐藏网页浏览器。 |

## 方法

|     |     |
| --- | --- |
| **[Open](open)** | 打开指定 URL 的网站。 |
| **[scrollBy](scrollby)** | 按指定的相对量滚动窗口。 |
| **[scrollTo](scrollto)** | 将窗口滚动到指定的位置。 |
| **[SetFocus](set_focus)** | 将键盘焦点设置到网页浏览器。 |

## 示例

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

支持 EmEditor Professional 版 23.0 或之后的版本。


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
