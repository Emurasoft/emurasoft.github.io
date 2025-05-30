# 使用提交清單外掛程式

**提交清單**外掛程式預設安裝在 EmEditor Professional 中。此外掛程式會顯示 Git 倉儲的目前的變更和提交的歷史記錄。要使用**提交清單**外掛程式，請點擊**外掛程式**欄上的 ![提交清單](../../images/plugin_commit_list.png) 圖示。或到**工具**功能表上，將滑鼠指向**外掛程式**，然後點擊**提交清單**。

此外掛程式將首先檢查目前的文檔是否在一個 **[Git](https://git-scm.com/)** 倉儲中。如果是，您可以選擇該倉儲並顯示其提交的歷史記錄。您可以點擊**打開...**按鈕來打開不同的倉儲。

## 變更邊欄

該外掛程式將首先檢查目前的文檔是否在 **[Git](https://git-scm.com/)** 倉儲中。 如果是，將打開倉儲並顯示其狀態。您可以單擊側邊欄中的**打開...**按鈕打開不同的倉儲。

目前的變更和暫存的變更顯示在側邊欄中。暫存的變更是添加到索引中的變更。對工作目錄的所有其他變更都顯示在變更樹中。

右鍵單擊側邊欄中的已變更檔案將顯示一個功能表，其中包含針對該已變更檔案的命令。以下是該功能表中的選項。

- **檢視變更**會在編輯器中顯示與之前版本的檔案所做的比較結果，以顯示檔案做了哪些修改。具體來說，所比較的檔案版本是暫存檔案的最後一次提交和索引版本，或未暫存檔案的索引版本和工作樹版本。
- **打開檔案**會打開編輯器中的檔案。
- **暫存**和**取消暫存**相當於 `git add` 和 `git reset` 命令。
- **復原變更**可以應用在未暫存的檔案上。它調用 `git checkout` 以用索引中的內容來覆寫檔案。未追蹤的檔案會被刪除。
- 如果列出了子模塊，**更新子模塊**將調用 [`git submodule update --init`](https://git-scm.com/docs/git-submodule#Documentation/git-submodule.txt-update--init--remote-N--no-fetch--no-recommend-shallow-f--force--checkout--rebase--merge--referenceltrepositorygt--depthltdepthgt--recursive--jobsltngt--no-single-branch--filterltfilterspecgt--ltpathgt82308203) 來將子模塊中的檔案更新到其目前的 `HEAD`。
- **重新整理**將重新整理變更的檔案清單。

提交清單外掛程式會監視檔案系統，如果倉儲目錄中的檔案被外部程式修改，則會重新整理側邊欄。

**提取**按鈕會將變更從遠程倉儲拉取到本地倉儲。 **推送**則將本地變更發送到遠程倉儲。如果目前的分支沒有與上游分支相關聯，則在將變更推送到上游分支之前將建立上游分支。這些命令在完成時會用狀態列發送訊息。

**提取**和**推送**按鈕還能顯示一個數字，以指示上游分支後面或前面的提交數量。「提取 (1)」表示有 1 個提交要提取，「推送 (1)」表示有 1 個提交要推送。功能表中的**自動獲取**選項對於定期更新這些數字非常有用。

您可以點擊 **>** 按鈕來訪問更多指令。

- **重新整理**會重新整理已變更的檔案清單。
- **指令輸出**顯示先前指令的匯出。
- **狀態**指令會列出 `git status` 的匯出。
- **擷取**指令會更新您的遠程跟蹤分支。
- **打開倉儲資料夾**會打開檔案總管中的倉儲資料夾。
- 如果目前的分支有上游分支， **打開倉儲網站**會在 Web 瀏覽器中打開項目的原始檔控制和協作網站，例如 GitHub。
- 如果啟用**自動擷取**，則每 3 分鐘調用一次 `git fetch`。
- **說明**會打開此頁。

您可以使用下拉功能表變更目前的分支。變更分支等同於命令 `git checkout branch`。沖突的變更將阻止您簽出分支。

分支下拉清單下方的編輯控件是您可以編寫提交訊息的地方。單擊**提交暫存**/**提交全部**來提交暫存變更或暫存所有變更並提交。提交將提交給目前的選定的分支。

## 提交清單

點擊**提交清單**按鈕來檢視提交歷史。在提交清單中，可以通過左側的分支清單檢視其他分支的歷史記錄。選擇提交後，右側欄會顯示提交詳細信息和此次提交變更的檔案清單。右鍵單擊清單中的檔案並選擇**與上一個比較**以檢視此次提交對檔案的變更。

在提交清單中，您可以右鍵單擊提交並選擇**複製**以複製提交詳細信息。 **提交時瀏覽檔案**將在提交時顯示樹狀目錄。 **比較提交**將向您展示兩次提交之間的差異。

您可以通過單擊**篩選記錄**來篩選清單。輸入**篩選字串**，選擇**篩選依據**選項，然後點擊**篩選**。提交清單現在僅顯示與篩選符合的提交。 點擊**篩選記錄**按鈕旁邊的 **取消篩選** 按鈕會取消篩選。

左側面板會顯示倉儲中的分支清單。右鍵單擊分支所顯示的內容功能表包含以下與分支相關的指令。

- **檢視分支**：顯示該分支的提交清單。
- **比較分支**：當選擇兩個分支時，您可以比較這些分支之間的檔案。
- **重新整理**：重新整理 CommitList 列顯示的信息。
- **簽出分支**：切換到分支。
- **建立新分支...**：從所選分支建立新分支並簽出新分支。
- **刪除分支**：刪除所選分支。
- **刪除遠程分支**：刪除該分支跟蹤的遠程分支（調用 `git push -v <upstream> --delete <branch>` 指令）。

如果在目前的倉儲中的檔案已在編輯器中打開，則可以使用**檢視目前的檔案的歷史記錄**按鈕。它會列出包括對目前的檔案的變更的所有提交。右鍵單擊一個提交將顯示四個選項。 **顯示提交**會跳轉到主提交清單中的那個提交。 **與上一個比較**將檔案與其之前的修訂版進行比較。 **提交時比較檔案**則將兩次不同提交時的檔案進行比較。 **與工作樹狀上的檔案比較**會比較所選提交的檔案和工作樹狀上的版本。

## 提示

- 按 **F6** 鍵或 **ESC** 鍵可以讓鍵盤焦點返回到編輯器中。
