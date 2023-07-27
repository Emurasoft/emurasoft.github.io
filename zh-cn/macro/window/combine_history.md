# CombineHistory 属性 (Window ����)

指定要不要合并撤消/重做记录。

## 

### \[JavaScript\]

```
b =CombineHistory;
CombineHistory = b;
```

### \[VBScript\]

```
b =CombineHistory
CombineHistory = b;
```

## 示例

### \[JavaScript\]

```
CombineHistory = true;
document.writeln( "ABC" );
document.writeln( "DEF" );
CombineHistory = false;
```

### \[VBScript\]

```
CombineHistory = True
document.writeln "ABC"
document.writeln "DEF"
CombineHistory = False
```

## 版本

支持 EmEditor Professional 15.5 或之后的版本。
