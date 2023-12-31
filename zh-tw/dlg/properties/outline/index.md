# 「大綱」頁面

**大綱** 頁面讓你能設定與大綱相關的屬性。

## 「導航模式顯示大綱」核取方塊

如果勾選了該核取方塊，EmEditor 會把大綱作為導航顯示在編輯器的左邊。這個核取方塊只有在自訂對話方塊中 [**大綱** 頁面](../../customize/outline/index) 上的 **為每一個組態切換大綱導引** 核取方塊被勾選時可用。

## 「自訂工具條顯示大綱」核取方塊

如果勾選了該核取方塊，EmEditor 會在自訂顯示條中顯示大綱。這個核取方塊只有在自訂對話方塊中 [**大綱** 頁面](../../customize/outline/index) 上的 **為每一個組態切換大綱顯示條** 核取方塊被勾選時可用。.

## 「最多級別」下拉清單方塊

指定要顯示的最多大綱級別數。

## 「初始狀態」下拉清單方塊

指定在首次打開檔案時是否應將大綱展開，折疊或展開/折疊到指定的級別。

## 「類型」下拉清單方塊

決定如何計算大綱的排列。從下列選項中選擇一個：

|     |     |
| --- | --- |
| **大括弧數 {}** | 用大括號數計算大綱的排列。這適用於許多編程語言。 |
| **空格數** | 用在每行開頭的空格數或 tab 數計算大綱的排列。這適用於一般用途。 |
| **自訂** | 按照在 **搜尋** 清單方塊中指定的設定計算大綱的排列。如果選擇該選項，請點擊 **搜尋** 清單方塊旁邊的 **「添加」** 按鈕，將多個項目添加到清單中。 |
| **方括弧數 \[\]** | 用方括號數 計算大綱的排列。這對某些編程語言可能很有用。 |
| **自訂（指定第1級別作為開始/第2級別作為結束）** | 按照在 **搜尋** 清單方塊中指定的設定計算大綱的排列。如果選擇該選項，請點擊 **搜尋** 清單方塊旁邊的 **「添加」** 按鈕，將兩個項目添加到清單中。 **搜尋** 清單方塊中的第一項作為開始字串，第二項作為結束字串。XML 組態將此設定作為預設值使用。 |
| **Tab 數** | 按照每行開頭的 Tab 數計算大綱的排列。這個選項可能對一般用途有用。 |

## 「使註解可折疊」核取方塊

指定註解是否可折疊。

## 「隱藏符合的字串/用規則運算式取代」核取方塊

指定是否應在自訂工具條中隱藏符合的字串。如果勾選了下面的 **規則運算式** 核取方塊，則此選項指定是否應使用 **取代為** 中指定的字串取代符合的字串。

## 「搜尋」清單方塊

如果沒有勾選 **規則運算式** 核取方塊，請輸入要匹配的行的開頭的字元。例如，輸入 "." 來匹配僅以 "." 開始的行。如果勾選了 "規則運算式" 核取方塊，請輸入一個與指定級別相符合的規則運算式。例如，輸入 "^\\d.\*?$" 來匹配僅以數字開始的行。

## 「規則運算式」核取方塊

指定在 **搜尋** 文字方塊中輸入的字串是否要作為規則運算式處理。

## 「取代為」文字方塊

指定要取代為的字串當選擇了 **隱藏符合的字串/用規則運算式取代** 核取方塊時。

## 「重設」按鈕

重設為預設設定。會顯示 [**重設** 對話方塊](../reset/index) 並讓你能從另一個組態複製設定。

