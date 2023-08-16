# SIZE\_PTR

様々なサイズを表すのに使用します。32 ビット用プラグインでは、SIZE 構造体と同じ意味です。64 ビット用プラグインでは、各フィールドが 32 ビットから 64 ビットに拡張されます。

```
typedef struct tagSIZE_PTR {
	LONG_PTR cx;
	LONG_PTR cy;
} SIZE_PTR, *PSIZE_PTR;
```

## フィールド

_cx_

水平方向の値を指定します。

_cy_

垂直方向の値を指定します。
