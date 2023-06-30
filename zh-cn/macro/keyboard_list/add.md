# Add 方法 (KeyboardList ����)

添加一个项目。

#### \[JavaScript\]

list. **Add**( _nKey_, _nFlags_, _nCommand_ );

#### \[VBScript\]

list. **Add** _nKey_, _nFlags_, _nCommand_

## 参数

_nKey_

指定要添加的项目的按键。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeVirtualKey | 指定对象的 Key 成员是一个虚拟键代码。如果这个标志没有指定，那么对象的 Key 成员被假定为指定一个字符代码。 |
| eeShift | 指定必须按下 SHIFT 键当按下加速键时。 |
| eeCtrl | 指定必须按下 CTRL 键当按下加速键时。 |
| eeAlt | 指定必须按下 ALT 键当按下加速键时。 |

_nCommand_

指定要添加的项目的命令 ID。

## 版本

支持 EmEditor 7.00 或之后的版本。