# Q. How can I round numbers in a column to 2 decimal places?

Select a whole column where you want to round numbers. SelectReplace on theSearch menu (or press CTRL + H) to bring up theReplace dialog box. Click theNumber Range radio button. Clear theIntegers Only option, leaveMinimum andMaximum fields empty, and clickOK if theEnter Number Range dialog box appears. Make sure "\[ , \]" is set in theFind field. In theReplace with field, enter " `\J parseFloat( \0 ).toFixed(2)`". Make sure "In the Selections Only" option is enabled, and click the "Replace All" button.
