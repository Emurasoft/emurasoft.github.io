# 編輯巨集 (教程)

EmEditor 會自動把最后的巨集作為預設巨集。所有，如果要編輯預設巨集，選擇 [**編輯巨集** 命令](../../cmd/macros/macro_edit) 即可。預設的巨集會在一個新的 EmEditor 視窗中被打開。如果您想要打開非預設的巨集檔案，執行 [**選擇巨集** 命令](../../cmd/macros/macro_select)，然后選擇您想要編輯的巨集。這個動作會把您所選取的巨集設為預設。然后，您便能通過選擇 [**編輯巨集** 命令](../../cmd/macros/macro_edit) 來編輯該巨集。在這個教程中，我們會編輯 tutorial.jsee 或 tutorial.vbee。當打開這兩個檔案中的一個時，會分別出現下列文字:

## 

### \[JavaScript\]

```
document.selection.Text="EmEditor supports macros.";
```

### \[VBScript\]

```
document.selection.Text="EmEditor supports macros."
上面的代碼用[Text 屬性](../selection/selectiontext) 告訴 EmEditor 在目前的游標位置處插入 "EmEditor supports macros." 文字。
```

## 下一主題:
