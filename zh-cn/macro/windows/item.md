# Item 属性 (Windows ����)

为指定索引的窗口检索窗口对象。

## 

### \[JavaScript\]

```
wnd = shell.windows.Item( Index );
```

### \[VBScript\]

```
wnd = shell.windows.Item( Index )
```

## 参数

_Index_

用以 1 为基准的整数指定窗口的索引。

## 示例

### \[JavaScript\]

```
alert( "Name of the first window: " + shell.windows.Item(1).Caption );
```

### \[VBScript\]

```
alert "Name of the first window: " + shell.windows.Item(1).Caption
```

## 版本

支持 EmEditor 7.00 或之后的版本。
