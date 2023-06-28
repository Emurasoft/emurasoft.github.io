# Add 方法

添加一个新的项目到菜单末尾。

#### \[JavaScript\]

popupmenu. **Add**( _strText_, _id_, _flags_ );

#### \[VBScript\]

popupmenu. **Add** _strText_, _id_, _flags_

## 参数

_strText_

指定要显示的文本。如果 eeMenuSeparator 在 _flags_ 参数中被设置，必须指定一个空字符串。

_id_

指定新菜单项目的标识符。Track 方法把标识符作为返回值。如果 eeMenuSeparator 在 _flags_ 参数中被设置，必须指定 0。

_flags_

指定项目的状态。能指定下列标志。

|     |     |
| --- | --- |
| eeMenuChecked | 把一个选中标记放在菜单项目旁。Places a check mark next to the menu item. |
| eeMenuGrayed | 禁用菜单项目并且让它变为灰色，这样就不能选择它。 |
| eeMenuSeparator | 画一条水平分隔线。这个标志不能与其他标志合用。 |

## 版本

支持 EmEditor 5.00 或之后的版本。