# Unpivot 方法 (Document ����)

通过平展 CSV 数据将列转换为行。

#### \[JavaScript\]

document. **Unpivot**( strSelect, strAttrLabel, strValueLabel, nFooter );

#### \[VBScript\]

document. **Unpivot** strSelect, strAttrLabel, strValueLabel, nFooter

## 参数

_strSelect_

> 指定用于选择要逆透视的列的字符串。例如，"2-5"，"3-"，"1,3,5"。如果该参数为空或省略，则会体现为 "2-"。

_strAttrLabel_

> 指定要创建的属性列的标题标签。

_strValueLabel_

> 指定要创建的值列的标题标签。

_nFooter_

> 指定页脚中的行数。页脚行不会被转换。

## 示例

逆透视除第一列之外的所有列。最后一行被忽略。

#### \[JavaScript\]

document.Unpivot( "2-", "Attribute", "Value", 1 );

#### \[VBScript\]

document.Unpivot( "2-", "Attribute", "Value", 1 )

## 版本

支持 EmEditor Professional v21.4 或之后的版本。