# Q. An Error message similar to "The paging file is too small for this operation to complete" appears when I try opening a very large file. How can I fix this error?

You will need to increase the physical or virtual memory to open a very large file. We recommend increasing the physical memory (RAM) in your PC first. If the error still persists or if you are unable to increase the physical memory, we recommend increasing the virtual memory. To increase the virtual memory, please follow the steps below:

1. Press **Win**(⊞)+ **R** keys to bring up the **Run** dialog box, and enter **SystemPropertiesPerformance.exe** to display the **Performance Options** dialog box.
2. Select the **Advanced** page of the **Performance Options** dialog box.
3. Click the **Change** button in the **Virtual memory** box.
4. Clear the **Automatically manage paging file size for all drives** check box.
5. Select the **Custom size**, and enter recommended numbers to **Initial size (MB)** and **Maximum size (MB)** boxes. We recommend entering a same large number to both **Initial size (MB)** and **Maximum size (MB)** boxes. For example, enter 80000 to both boxes.
6. Click OK and restart Windows.
7. Try opening the large file with EmEditor again. If the error persists, please repeat the above steps to increase the virtual memory size until the error disappears.

## References
