# WebBar オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [scrollX](scrollx) | スクロール バーの水平方向の位置を返します。 |
| [scrollY](scrolly) | スクロール バーの垂直方向の位置を返します。 |
| [Visible](visible) | Webブラウザの表示/非表示を切り替えます。 |

## メソッド

|     |     |
| --- | --- |
| [Open](open) | 指定する URL のWebサイトを開きます。 |
| [scrollBy](scrollby) | スクロール バーを指定する差分だけ移動します。 |
| [scrollTo](scrollto) | スクロール バーを指定する位置に移動します。 |
| [SetFocus](set_focus) | Webブラウザにキーボード フォーカスを設定します。 |

## 例

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

## バージョン

EmEditor Professional Version 23.0 以上で利用できます。


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
