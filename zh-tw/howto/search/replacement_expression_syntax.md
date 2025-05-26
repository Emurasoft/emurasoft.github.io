# 取代運算式語法

當用規則運算式或數字範圍取代時，可以用取代運算式。

下清單達式是可用於 **取代** 對話方塊以及 **多檔取代** 對話方塊中的 **取代為** 文字方塊內。

| | |
| --- | --- |
| \\0 | 把整個規則運算式作為指定為反向參考。 |
| \\1 - \\9 | 指定一個反向參考 \- 一個反向參考是上一個被符合的子運算式的引用。引用的內容是與子運算式相符合的內容，而不是運算式本身。一個反向參考由逸出序列 "\\" 加一個 "1" 到 "9" 的數字組成。"\\1" 指的是第一個子運算式，"\\2" 是第 2 個，以此類推。 |
| $10, $11, $12, ... | 表示超過 9 個的反向參考。相當於 \\k<10>，\\k<11>，\\k<12>，...。 |
| \\k<name> | 表示一個已命名的反向參考。已命名的反向參考是用以下形式引用之前符合的已命名的捕獲組：(?<name>expression)。如果 "name" 是一個數字，則它表示一個已編號的反向參考，相當於 \\1，\\2，\\3，...。 |
| \\n | 一個換行符號。 |
| \\r | 在 **多檔取代** 表示一個歸位符。請參考 [指定換行符號](search_nl)。 |
| \\t | 一個 tab。 |
| \\L | 強制所有後續取代字元要小寫。 |
| \\U | 強制所有後續取代字元要大寫。 |
| \\H | 強制所有後續取代字元要是半形字元。 |
| \\F | 強制所有後續取代字元要是全形字元。 |
| \\Nc | 強制使用 [Unicode 正規化表單 C（標準組合）](../../cmd/convert/unicode_norm_fc) 轉換所有後續取代字元。 |
| \\Nd | 強制使用 [Unicode 正規化表單 D（標準分解）](../../cmd/convert/unicode_norm_fd) 轉換所有後續取代字元。 |
| \\NC | 強制使用 [Unicode 正規化表單 KC（相容性組合）](../../cmd/convert/unicode_norm_fkc) 轉換所有後續取代字元。 |
| \\ND | 強制使用 [Unicode 正規化表單 KD（相容性分解）](../../cmd/convert/unicode_norm_fkd) 轉換所有後續取代字元。 |
| \\E | 關閉之前的 \\L，\\U，\\F，\\H，\\Nc，\\Nd，\\NC，或 \\ND。 |
| \\J | 指定運算式使用 JavaScript。\\J 必須放在取代運算式的開頭。可以與反向參考結合使用。還可以在指令碼中使用 **cell** 函數。請看 [cell function (beta)](#cell-function-beta)。
| \\V | 與 \\J 相同，只是 \\V 使用 **V8 JavaScript** 引擎而不是 **Chakra** 引擎。 |
| \\D | 如果 [**數字範圍運算式**](number_range_syntax) 的類型為日期/時間，並用於符合字串，則該運算式指定了一種日期格式。它可以與 **\\T** 結合使用。[請參閱可用的日、月和年格式圖片。](https://docs.microsoft.com/zh-tw/windows/win32/intl/day--month--year--and-era-format-pictures) 參見[日期格式範例](#date-format-example)
| \\T | 如果 [**數字範圍運算式**](number_range_syntax) 的類型為日期/時間，並用於符合字串，則該運算式指定了一種時間格式。它可以與 **\\D** 結合使用。[請參閱可用的小時、分鐘和秒格式圖片。](https://docs.microsoft.com/zh-tw/windows/win32/intl/hour--minute--and-second-format-pictures) 參見[時間格式範例](#time-format-example)
| (?n:true\_expression:false\_expression) | 如果符合子運算式 N，則評估 true\_expression 並將其發送到匯出，否則評估 false\_expression 並將其發送到匯出。例如，(?1foo:bar)，如果符合子運算式 \\1，會用 foo取代每個符合，反之則用 bar。另外，您也可以用這種方式寫該運算式：(?{1}foo:bar) |
| $(Path) | 檔案路徑。 |
| $(Dir) | 檔案目錄。 |
| $(Filename) | 不含副檔名的檔案名。 |
| $(FilenameEx) | 含副檔名的檔案名。 |
| $(Ext) | 副檔名。 |
| $(Lines) | 行數（不能用於 **多檔取代**）。 |
| $(CsvColumns) | CSV 欄數（不能用於 **多檔取代**）。 |

(cell-function-beta)=
## cell 函數 (beta)

如果指定了 **\\J**，則可以在 JavaScript 中使用 **cell** 函數。此函數檢索指定 CSV 儲存格中的文字。

<table><tbody><tr><th>取代運算式</th><th>含義</th></tr><tr><td>\J &quot;\0&quot; + &quot;abc&quot;</td><td>串連符合到的字串和 「abc」</td></tr><tr><td>\J &quot;\0&quot;.substr( 0, 5 );</td><td>返回符合字串的前 5 個字元</td></tr><tr><td>\J \0 * 100;</td><td>將符合到的數字乘以100</td></tr><tr><td>\J parseFloat( \0 ).toFixed(2);</td><td>將符合到的數字保留兩位小數</td></tr><tr><td>\J cell( -1 )</td><td>返回符合儲存格左側相鄰儲存格的文字</td></tr><tr><td>\J parseFloat( cell( -1 ) ) <br>+ parseFloat( cell( -2 ) ) </td><td>返回左側兩個相鄰儲存格的總和</td></tr></tbody></table>

### 

#### \[JavaScript\]

```
str =cell( iColumn [, yLine [, flags ] ] );
```

### 參數

_iColumn_

指定要檢索的文字的列的索引，以從目前的位置出發的相對位置表示，除非在 _flags_ 中指定了 8。

_yLine_

指定要檢索的文字的行號，以從目前的位置出發的相對位置表示，除非在 _flags_ 中指定了 8。 如果省略，則指定 0。

_flags_

指定以下值的組合。0，1 和 2 不能一起使用。如果省略，則指定 1。

|     |     |
| --- | --- |
| 0 | 返回的文字可以不包括包圍的雙引號或分隔符。 |
| 1 | 返回的文字可以包括包圍的雙引號但不包括分隔符。 |
| 2 | 返回的文字可以包括包圍的雙引號和分隔符。 |
| 8 | _iColumn_ 和 _yLine_ 參數以 1 為基礎的絕對值表示。 |

## 註意

EmEditor 中沒有目前的 JavaScript/ECMAScript 中的許多新方法。取代運算式使用 Chakra（相當於 Microsoft Edge Legacy），並且最多支持到 ECMAScript 5.1，因此不支援 ECMAScript 5.1 之後引入的新方法。

## 請同樣參考

- [規則運算式語法](search_regexp_syntax)
