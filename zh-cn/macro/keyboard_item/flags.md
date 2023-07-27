# Flags 属性 (KeyboardItem ����)

指定对象的标志。

## 

### \[JavaScript\]

```
n = item.Flags;
item.Flags = n;
```

### \[VBScript\]

```
n = item.Flags
item.Flags = n
```

## 参数

_n_

从下列值中选择。

|     |     |
| --- | --- |
| eeVirtualKey | 指定对象的 Key 成员是一个虚拟键代码。如果这个标志没有指定，那么对象的 Key 成员被假定为指定一个字符代码。 |
| eeShift | 指定必须按下 SHIFT 键当按下加速键时。 |
| eeCtrl | 指定必须按下 CTRL 键当按下加速键时。 |
| eeAlt | 指定必须按下 ALT 键当按下加速键时。 |

## 版本

支持 EmEditor 7.00 或之后的版本。
