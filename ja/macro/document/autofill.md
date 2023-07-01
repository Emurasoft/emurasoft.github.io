# AutoFill メソッド ()

CSV 文書に対してオートフィル、またはフラッシュ フィルを実行します。

#### \[JavaScript\]

_nResults_ = document. **AutoFill**( _xSrcCellStart_, _ySrcCellStart_, _xSrcCellEnd_, _ySrcCellEnd_, _xDestCellStart_, _yDestCellStart_, _xDestCellEnd_, _yDestCellEnd_, _nFlags_, _nIncrement_ );

#### \[VBScript\]

_nResults_ = document. **AutoFill**( _xSrcCellStart_, _ySrcCellStart_, _xSrcCellEnd_, _ySrcCellEnd_, _xDestCellStart_, _yDestCellStart_, _xDestCellEnd_, _yDestCellEnd_, _nFlags_, _nIncrement_ )

## Parameters

_xSrcCellStart_

元のセルの開始位置の列番号を指定します。

_ySrcCellStart_

元のセルの開始位置の行番号を指定します。

_xSrcCellEnd_

元のセルの終了位置の列番号を指定します。

_ySrcCellEnd_

元のセルの終了位置の行番号を指定します。

_xDestCellStart_

目標のセルの開始位置の列番号を指定します。

_yDestCellStart_

目標のセルの開始位置の行番号を指定します。

_xDestCellEnd_

目標のセルの終了位置の列番号を指定します。

_yDestCellEnd_

目標のセルの終了位置の行番号を指定します。

_nFlags_

次の値の組み合わせを指定します。省略すると、eeFillDefault が指定されることになります。

|     |     |
| --- | --- |
| eeFillDefault | EmEditor が目標のセルに入力する値を決定します。 |
| eeFillCopy | ソース範囲からターゲット範囲に値をコピーし、必要に応じて繰り返します。 |
| eeFillSeries | ソース範囲の値をターゲット範囲に連続する数値として適用します。 |
| eeFlashFill | フラッシュ フィルの動作を実行します。つまり、検出されたパターンに基づいて、ソース範囲の値をターゲット範囲に適用します。このフラグは垂直方向にのみ適用されます。 |
| eeFillDontOverwrite | オートフィルの動作はターゲット範囲にある既存のセルを上書きしないこととします。これは eeFlashFill と共に使用することはできません。 |
| eeFillRepeat | オートフィルの動作は最終行まで空でないセルの値を使用して繰り返されます。これは eeFlashFill と共に使用することはできません。 |

_nIncrement_

単一のセルのみ選択されていて、 _dwFlags_ フィールドに eeFlashFill が指定されている場合、連番の増加数を指定します。省略すると 1 が指定されることになります。

## 戻り値

戻り値は、メッセージが成功すると、次の値の組み合わせになります。戻り値が 0 の場合、オートフィルまたはフラッシュ フィルの動作を完了するためのパターンが検出できなかったことを意味します。負の値はメッセージが失敗したことを意味します。

|     |     |
| --- | --- |
| eeFillCopy | ソース範囲からターゲット範囲に値をコピーし、必要に応じて繰り返します。 |
| eeFillSeries | ソース範囲の値をターゲット範囲に連続する数値として適用します。 |
| eeFlashFill | フラッシュ フィルの動作を実行します。つまり、検出されたパターンに基づいて、ソース範囲の値をターゲット範囲に適用します。このフラグは垂直方向にのみ適用されます。 |

## 例

#### \[JavaScript\]

nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries \| eeFillDontOverwrite );

if( nResults >= 0 ) {

alert( "Success" );

}

#### \[VBScript\]

nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries \| eeFillDontOverwrite );

If nResults >= 0 Then

alert "Success"

End If

## バージョン

EmEditor Professional Version 17.5 以上で利用できます。
