# Q. 如何使用 EmEditor 打开 Excel 文件？

Excel 文件是二进制文件，您不能直接使用 EmEditor 打开 Excel 文件。但是，有几种方法可以完成此任务。

1. 使用 Excel 打开 Excel 文件，并将其另存为文本文件（制表符分隔或逗号分隔）。然后使用 EmEditor 打开文本文件。
2. 使用 Excel 外接程序 [CSV Import+Export](https://appsource.microsoft.com/zh-cn/product/office/wa200000025) 来把 Excel 文件导出为 CSV 文件，然后使用 EmEditor 打开 CSV 文件。
3. 用 Excel 打开一个 Excel 文件，按 CTRL + A，然后按 CTRL + C 选择所有数据并将其复制到剪贴板。启动 EmEditor，从 CSV 工具栏中选择制表符分隔模式，然后按 CTRL + V 进行粘贴。