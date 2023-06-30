# QueryStatusByID 方法 (Editor ��H)

檢索指定命令的目前的狀態，是否已被勾選和啟用。

#### \[JavaScript\]

_nStatus_ = editor. **QueryStatusByID**( _nID_ );

#### \[VBScript\]

_nStatus_ = editor. **QueryStatusByID**( _nID_ )

## 參數

_nID_

指定表示要執行的命令 ID 的一個整數。詳見 **[命令參考](../../cmd/index)** 來檢視可用命令清單。不是所有命令都可以或被支持。

## 返回值

Returns a combination of the following values.

|     |     |
| --- | --- |
| eeStatusEnabled | 命令被啟用。 |
| eeStatusLatched | 命令被勾選。 |

## 版本

支持 EmEditor 4.00 或之後的版本。