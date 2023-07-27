# Q. How can I open Excel files with EmEditor?

Excel files are binary files, and you can't open Excel files directly with EmEditor. However, there are several ways to achieve this task.

1. Open an Excel file with Excel, and save it as a text file (Tab delimited or Comma delimited). Then open the text file with EmEditor.
2. Use an Excel add-in, [CSV Import+Export](https://appsource.microsoft.com/en-us/product/office/wa200000025) to export an Excel file as a CSV file, and then open the CSV file with EmEditor.
3. Open an Excel file with Excel, press CTRL + A, and CTRL + C to select and copy all data to the Clipboard. Launch EmEditor, select the Tab-separated mode from theCSV toolbar, and press CTRL + V to paste.
