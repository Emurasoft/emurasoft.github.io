# CETLFrame Member Variables

These member variables inside CETLFrame provide EmEditor with information about the plug-in, such as the name and icon of this plug-in. They must all be defined in order for the plug-in to compile. Variables names start with \_ID require the ID name for the resource.

|     |     |
| --- | --- |
|Identifier |Description |
| \_IDS\_NAME | Displayed as the Name inside the Customize Plug-ins window. |
| \_IDS\_MENU | Displayed in the Tools > Plug-ins menu. |
| \_IDS\_STATUS | Displayed in the tooltip in the Plug-ins toolbar and the status bar. |
| \_IDS\_VER | Displayed as the Version inside the Customize Plug-ins window. |
| \_USE\_LOC\_DLL | The value of 1 specifies that separate DLL(s) containing resources for the Multilingual User Interface are to be used. Otherwise, this value is 0. These DLLs are to be placed in the mui subfolder of the plug-in.. |
| \_IDB\_BITMAP | 16 bit color, 16x16 px. Bitmap image to use as the default icon for all toolbar color palettes and sizes. If EmEditor does not load the icon, try exporting it in Paint. The following icon images are used for optimal display with different toolbar settings. |
| \_IDB\_16C\_24 | 16 bit color, 24x24 px. |
| \_IDB\_TRUE\_16\_DEFAULT | True color (24 or 32 bit), 16x16 px. |
| \_IDB\_TRUE\_16\_HOT | True color, 16x16 px. This image is displayed when cursor is hovered over icon. |
| \_IDB\_TRUE\_16\_BW | True color, 16x16 px, black and white. Displayed when the plug-in is disabled. |
| \_IDB\_TRUE\_24\_DEFAULT | True color, 24x24 px. |
| \_IDB\_TRUE\_24\_HOT | True color, 24x24 px. This image is displayed when cursor is hovered over icon. |
| \_IDB\_TRUE\_24\_BW | True color, 24x24 px, black and white. |
| \_MASK\_TRUE\_COLOR | The color that becomes transparent in the true color icon. Use RGB(r,g,b) to set this value. |
| \_ALLOW\_OPEN\_SAME\_GROUP | TRUE if the plug-in allows EmEditor to open a new file in the same group. |
| \_ALLOW\_MULTIPLE\_INSTANCES | TRUE if the plug-in supports multiple instances. If the plug-in should be allowed to run in more than one frame simultaneously, this message should return TRUE. Note that global <br> variables will be shared when multiple instances are running. |
| \_MAX\_EE\_VERSION | The newest version number of supported EmEditor \* 1000. |
| \_MIN\_EE\_VERSION | The oldest version number of supported EmEditor \* 1000. |
| \_SUPPORT\_EE\_PRO | TRUE if EmEditor Professional is supported. |
| \_SUPPORT\_EE\_STD | TRUE if EmEditor Standard is supported. |

