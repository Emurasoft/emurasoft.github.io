# Add メソッド (KeyboardList �R���N�V����)

アイテムを追加します。

#### \[JavaScript\]

list. **Add**( _nKey_, _nFlags_, _nCommand_ );

#### \[VBScript\]

list. **Add** _nKey_, _nFlags_, _nCommand_

## パラメータ

_nKey_

追加するアイテムのキーを指定します。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeVirtualKey | オブジェクトの Key プロパティは、仮想キー コードであることを示します。このフラグが指定されていない場合、Key プロパティは文字コードを示すことになります。 |
| eeShift | SHIFT キーを押しながら、指定するキーを押すことを示します。 |
| eeCtrl | CTRL キーを押しながら、指定するキーを押すことを示します。 |
| eeAlt | ALT キーを押しながら、指定するキーを押すことを示します。 |

_nCommand_

追加するアイテムのコマンド  ID を指定します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
