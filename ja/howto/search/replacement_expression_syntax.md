# 置換表現構文

正規表現または数値範囲を使用して置換する際、JavaScript を置換表現に使用できます。

\[置換\] ダイアログ ボックスおよび \[ファイルから置換\] ダイアログ ボックスでは、次の表現が \[置換後の文字列\] ドロップダウン リスト
ボックスで使用できます。

| | |
| --- | --- |
| \\0 | 正規表現全体への後方参照を示します。 |
| \\1 - \\9 | 後方参照は、一致した部分式への参照です。参照は部分式が一致したものであり、表現そのものではありません。後方参照はエスケープ文字"\\"とそれに続く数字"1"-"9"から成り立っています。 |
| $10, $11, $12, ... | 9 を超える後方参照を示します。\\k<10>, \\k<11>, \\k<12>, ... と等価です。 |
| \\k<name> | 名前付き後方参照を示します。名前付き後方参照は、以前に一致した (?<name>expression) のフォームの捕獲式グループへの参照です。"name" が数字の場合、数字の後方参照を示し、\\1, \\2, \\3, ... と等価です。 |
| \\n | 改行 |
| \\r | ファイルから置換では、復帰文字として使用します。 [改行コードの指定方法](search_nl) もお読みください。 |
| \\t | タブ |
| \\L | 次に続く文字列を小文字に変換します。 |
| \\U | 次に続く文字列を大文字に変換します。 |
| \\H | 次に続く文字列を半角に変換します。 |
| \\F | 次に続く文字列を全角に変換します。 |
| \\Nc | 次に続く文字列を [Unicode正規化形式C (正準合成)](../../cmd/convert/unicode_norm_fc) を使用して変換します。 |
| \\Nd | 次に続く文字列を [Unicode正規化形式D (正準分解)](../../cmd/convert/unicode_norm_fd) を使用して変換します。 |
| \\NC | 次に続く文字列を [Unicode正規化形式KC (互換合成)](../../cmd/convert/unicode_norm_fkc) を使用して変換します。 |
| \\ND | 次に続く文字列を [Unicode正規化形式KD (互換分解)](../../cmd/convert/unicode_norm_fkd) を使用して変換します。 |
| \\E | 以前の \\L、\\U、\\F、\\H、\\Nc、\\Nd、\\NC、または \\ND による変換を終了します。 |
| \\J | 文字列全体が JavaScript の表現であることを指定します。\\J は置換表現の最初に位置している必要があり、\\E で終了することはできません。後方参照と一緒に指定することができます。スクリプト内で cell 関数も使用できます。[cell 関数 (beta)](#cell-function-beta)を参照してください。
| \\V | \\J と同じですが、\\V は Chakra エンジンの代わりに V8 JavaScript エンジンを使用します。 |
| \\D | [数値範囲表現](number_range_syntax) の日付/時刻タイプが使用された一致の場合、この表現は日付フォーマットを指定します。\\Tと組み合わせて使用することもできます。 [利用可能な日、月、年形式のフォーマットを参照](https://docs.microsoft.com/ja-jp/windows/win32/intl/day--month--year--and-era-format-pictures)。[日付フォーマット例](#date-format-example)を参照してください。
| \\T | [数値範囲表現](number_range_syntax) の日付/時刻タイプが使用された一致の場合、この表現は時刻フォーマットを指定します。\\Dと組み合わせて使用することもできます。 [利用可能な時刻、分、秒形式のフォーマットを参照](https://docs.microsoft.com/ja-jp/windows/win32/intl/day--month--year--and-era-format-pictures)。[時刻フォーマット例](#time-format-example)を参照してください。
| (?Ntrue\_expression:false\_expression) | 部分式 N が一致した場合、true\_expression に変換されます。一致しない場合は false\_expression に変換されます。例えば、(?1foo:bar) は部分式 \\1 が一致すると foo と置換され、一致しないと  bar と置換されます。(?{1}foo:bar) と書くこともできます。 |
| $(Path) | ファイル パス |
| $(Dir) | ファイル ディレクトリ |
| $(Filename) | 拡張子無しファイル名 |
| $(FilenameEx) | 拡張子付きファイル名 |
| $(Ext) | ファイル拡張子 |
| $(Lines) | 行数 (ファイルから置換では使用できません) |
| $(CsvColumns) | CSV 列数 (ファイルから置換では使用できません) |

## cell 関数 (beta)

\\J が指定されている場合、JavaScript で cell 関数が使用できます。この関数は CSV モードで指定するセルのテキストを取得します。

例えば、<table><tbody><tr><th>置換表現</th><th>意味</th></tr><tr><td>\J&quot;\0&quot;+&quot;abc&quot;</td><td>一致した文字列の最後に&quot;abc&quot;を追加します。</td></tr><tr><td>\J&quot;\0&quot;.substr(0,5);</td><td>一致した文字列の最初の5桁を返します。</td></tr><tr><td>\J\0*100;</td><td>一致した数字に100を掛けます。</td></tr><tr><td>\JparseFloat(\0).toFixed(2);</td><td>一致した数字の小数点以下第2位に四捨五入します。</td></tr><tr><td>\Jcell(-1)</td><td>左隣のセル内のテキストを返します。</td></tr><tr><td>\JparseFloat(cell(-1))<br>+parseFloat(cell(-2))</td><td>左隣の2個の小数の合計を返します。</td></tr></tbody></table>

### 

#### \[JavaScript\]

```
str = cell( iColumn [, yLine [, flags ] ] );
```

### Parameters

_iColumn_

取得するテキストの列のインデックスを指定します。flags に 8 が指定されていない場合は、現在位置からの相対位置になります。

_yLine_

取得するテキストの行番号を指定します。flags に 8 が指定されていない場合は、現在位置からの相対位置になります。省略すると、0 が指定されたことになります。

_flags_

次の値の組み合わせを指定します。ただし、0、1、2 は一緒には指定することはできません。省略すると 1 が指定されたことになります。

|     |     |
| --- | --- |
| 0 | 出力テキストには囲む2重引用符も区切り文字列も含まれません。 |
| 1 | 出力テキストには囲む2重引用符が含まれますが、区切り文字列は含まれません。 |
| 2 | 出力テキストには囲む2重引用符も区切り文字列も含まれます。 |
| 8 | _yLine_ と _iColumn_ パラメータは 1 から始まる絶対値で指定します。 |

(date-format-example)=
## 日付フォーマット例

例えば、一致した日付/時刻が「2022-03-31 21:30」の場合:<table><tbody><tr><th>置換表現</th><th>結果</th></tr><tr><td>\DM/d/yyyy</td><td>3/31/2022</td></tr><tr><td>\Dyyyy年M月d日</td><td>&nbsp;2022年3月31日</td></tr><tr><td>\D'month='M'day='d\THH:mm</td><td>month=3day=3121:30</td></tr></tbody></table>

(time-format-example)=
## 時刻フォーマット例

例えば、一致した日付/時刻が「2022-03-31 21:30」の場合:<table><tbody><tr><th>置換表現</th><th>結果</th></tr><tr><td>\THH:mm</td><td>21:30</td></tr><tr><td>\Th:mmtt</td><td>9:30PM</td></tr><tr><td>\THH:mm\D-yyyy-MM-dd</td><td>21:30-2022-03-31</td></tr></tbody></table>

## 注意

EmEditor では、最近の JavaScript/ECMAScript の新しいメソッドは利用できません。置換表現で使用できる JavaScript は、Chakra (Microsoft Edge Legacy に相当) を使用しているため、ECMAScript 5.1 までをサポートしています。ECMAScript 5.1 より後に追加されたメソッドは利用できません。新しいメソッドを使用する前に、必須バージョンの要件を満たしているか確認してください。

## 参考

- [正規表現構文](search_regexp_syntax)
