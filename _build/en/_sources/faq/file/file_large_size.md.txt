# Q. What can I do to speed up opening a very large file?

Some configurations could slow down performance. Check the following points:

- Click **[Properties for Current Configuration](../../dlg/properties/index)** under the
**Tools** menu, and then click the
[**General** page](../../dlg/properties/general/index).
If an item other than "No Wrap" is selected in the
**Wrap by** **drop-down**
list box, it might slow down EmEditor since it needs to compute where to wrap lines.
When you open a large file, select "No Wrap", or select the [**No Wrap** \
command](../../cmd/view/wrap_none).