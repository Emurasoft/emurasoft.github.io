# Active String page

The **Active String** page allows you to specify a behavior for each event.

### Type list box

Displays the list of items that can be customized as **Active String**. The items include URLs, email addresses, IPv4 and IPv6 addresses, strings enclosed by quotation marks, HTML Character Reference, Universal Character Names/Percent-encoding, Hexadecimal colors, RGB colors, Markers, and Search string. However, each Active String can be enabled or disabled per configuration in the [**Link** page](../../properties/link/index) of configuration properties.

### Event list box

Displays the list of events that can be selected as triggers at which an action starts running automatically.

### Action drop-down list box

Specifies an action when the specified event for the specified type is triggered.

### Select String before Action check box

If this is checked, the active string will be selected before running the specified action. Some actions might require this check box set. If **None** was selected for the **Action** drop-down list box, the active string will be simply selected without any actions.

### Command text box

When **Run Program** is selected for the **Action** drop-down list box, you can specify the name of a program, folder, document, or Internet resources to open. You can use the **>** button to select predefined macros, for instance, _$(Path)_, or the **...** button to select a file from the computer.

### Macro Path box

When **Run Macro** is selected for the **Action** drop-down list box, you can specify the macro file to run. You can use the **>** button to select predefined macros, for instance, _$(Path)_, or the **...** button to select a file from the computer.

### Tool drop-down list box

When **External Tool** is selected for the **Action** drop-down list box, you can specify the external tool to run. External Tools can be defined in the [**Customize Tools** dialog box](../../tools/index).

### Command drop-down list box

When **EmEditor Command** is selected for the **Action** drop-down list box, you can choose the command to execute from this drop-down list box. Some commands need the active string selected before execute, and in that case, the **Select String before Action** check box should be set.

### Reset button

Resets to default settings.

