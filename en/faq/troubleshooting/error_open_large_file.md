# Q. An Error message similar to "The paging file is too small for this operation to complete" appears when I try opening a very large file. How can I fix this error?

You will need to increase the physical or virtual memory to open a very large file. We recommend increasing the physical memory (RAM) in your PC first. If the error still persists or if you are unable to increase the physical memory, we recommend increasing the virtual memory. To increase the virtual memory, please follow the steps below:

1. PressWin(⊞)+R keys to bring up theRun dialog box, and enterSystemPropertiesPerformance.exe to display thePerformance Options dialog box.
2. Select theAdvanced tab of thePerformance Options dialog box.
3. Click theChange button in theVirtual memory box.
4. Clear theAutomatically manage paging file size for all drives check box.
5. Select theCustom size, and enter recommended numbers toInitial size (MB) andMaximum size (MB) boxes. We recommend entering a same large number to bothInitial size (MB) andMaximum size (MB) boxes. For example, enter 80000 to both boxes.
6. Click OK and restart Windows.
7. Try opening the large file with EmEditor again. If the error persists, please repeat the above steps to increase the virtual memory size until the error disappears.

## References
