# QueryStatusByID 方法 (Editor 对象)

检索指定命令的当前状态，是否已被勾选和启用。

## 

### \[JavaScript\]

```
nStatus = editor.QueryStatusByID( nID );
```

### \[VBScript\]

```
nStatus = editor.QueryStatusByID( nID )
```

## 参数

_nID_

指定表示要执行的命令 ID 的一个整数。详见 **[命令参考](../../cmd/index)** 来查看可用命令列表。不是所有命令都可以或被支持。

## 返回值

Returns a combination of the following values.

|     |     |
| --- | --- |
| eeStatusEnabled | 命令被启用。 |
| eeStatusLatched | 命令被勾选。 |

## 版本

支持 EmEditor 4.00 或之后的版本。
