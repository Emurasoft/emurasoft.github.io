# To Use HTMLBar Plug-in

The **HTMLBar** plug-in is installed by default with EmEditor Professional. This plug-in displays a toolbar, filled with buttons, which helps you insert frequently used HTML tags and elements. To use the **HTMLBar** plug-in:

1. Open an HTML file, and click ![](../../images/htmlbar.png) on the **Plug-Ins** bar. Or on the **Tools** menu, point to **Plug-ins**, and then click **HTMLBar**. The
**HTML toolbar** will appear.
2. Click any button of the **HTML** tag or element you would like to insert in the **HTML** document.

## 

### HTMLBar Plug-in Customizable Buttons

In order to customize the toolbar buttons:

1. Right click ![](../../images/htmlbar.png) on the **Plug-in toolbar**, then click **Properties**. The **HTML Bar Properties** box is displayed.
2. Click on the **Customize Buttons** button **.**
The **Customize Buttons** dialog box will appear. The predefined buttons are listed. You can click the **New** button to add a new button, or the **Properties** button to edit the selected button.
When you click the **New** button or the **Properties** button, the **Button Properties** will appear, where you can set the following options:

|     |     |
| --- | --- |
| **Icon** | Selects an icon for the button. |
| **Title** | Specifies a title for the button. The title is also displayed as a tooltip when a mouse hovers over the button. |
| **Insert Tags (Begin and End)** | Specifies begin and end tags to insert for this command. For instance, if you want the button to underline text, enter "\<u\>" in the Begin text box and "\<\/u\>" in the End text box. You can use special macros and insert them easily by clicking the ">" arrow and choosing one of the items in the list. For instance, \\{Path} inserts the file path of the current document, \\{PickFullPath} allows you to select a document in an Open dialog box, and \\{PickColor} allow you to select a color in the Color dialog box. |
| **Special Commands (Table, Font, Unindent, Heading, Form, Customize)** | These commands do specific tasks and are not customizable in details.<br>**Table**: displays the Insert Table dialog box where you can specify the rows and columns of the table, and inserts the table in the HTML document.<br>**Font**: displays the Font dialog box where you can select a font, and insert the font tag.<br>**Unindent**: removes indent for the selected lines.<br>**Heading**: creates a button with the arrow. If you press this button, a context menu appears with items from H1 to H6. Selecting one of these items inserts the corresponding tag (\<h1\> to \<h6\>).<br>**Form**: creates a button with the arrow. If you press this button, a context menu appears with form and form element items.<br>**Customize**: displays the Customize Buttons dialog box. |
| **Replace using Regular Expressions** | Replaces strings in the document or the selection using regular expressions. |
| **Separator** | Inserts a separator between buttons. |
| **Shortcut** | Specifies a shortcut key for this button. |
| **Remove** | Removes the previously defined shortcut key for this button. |

## Tips

By default, the **HTMLBar** plug-in doesn't appear automatically when an **HTML** file is opened. You can change this behavior from the **plug-in Properties**, which can be accessed by right-clicking the **plug-in button** on the **Plug-ins** bar, and selecting the
**Properties**.
