# 所需的成员变量

有几个变量必须在 CETLFrame 中定义才能编译。以 \_ID 开头的变量需要该资源的 ID。

|     |     |
| --- | --- |
| **标识名** | **说明** |
| \_IDS\_NAME | 在“自定义插件”窗口中显示为“名称”。 |
| \_IDS\_MENU | 显示在工具 \> 插件菜单中。 |
| \_IDS\_STATUS | 显示在插件工具栏的工具提示中。 |
| \_IDS\_VER | 在“自定义插件”窗口中显示为“版本”。 |
| \_USE\_LOC\_DLL | 值为 1 指定要使用包含多语言用户界面资源的独立 DLL。 否则，该值为 0。这些 DLL 将被放置在 EmEditor > mui 中。 |
| \_IDB\_BITMAP | 位图图像用作所有工具栏调色板和大小的默认图标。 如果 EmEditor 未加载图标，请尝试将其导出到 Paint 中。 以下图标图像用于使用不同的工具栏设置时进行最佳显示。 |
| \_IDB\_16C\_24 | 16 色，24x24 px。 |
| \_IDB\_TRUE\_16\_DEFAULT | 真色彩 (24 或 32 位)，16x16 px。 |
| \_IDB\_TRUE\_16\_HOT | 真色彩，16x16 px。光标悬停在图标上时显示此图像。 |
| \_IDB\_TRUE\_16\_BW | 真色彩，16x16 px，黑白。当插件停用时显示。 |
| \_IDB\_TRUE\_24\_DEFAULT | 真色彩，24x24 px。 |
| \_IDB\_TRUE\_24\_HOT | 真色彩，24x24 px。光标悬停在图标上时显示此图像。 |
| \_IDB\_TRUE\_24\_BW | 真色彩，24x24 px，黑白。 |
| \_MASK\_TRUE\_COLOR | 在真色彩图标中变透明的颜色。用 RGB(r,g,b) 设置值。 |
| \_ALLOW\_OPEN\_SAME\_GROUP | 允许在插件执行期间在同一个窗口群组中打开文件。 |
| \_ALLOW\_MULTIPLE\_INSTANCES | 如果插件支持多个实例，则为 TRUE。 如果允许插件同时在多个帧中运行，则此消息应该返回 TRUE。 请注意，全局变量将在多个实例运行时共享。 |
| \_MAX\_EE\_VERSION | 不使用。 |
| \_MIN\_EE\_VERSION | 不使用。 |
| \_SUPPORT\_EE\_PRO | 不使用。 |
| \_SUPPORT\_EE\_STD | 不使用。 |

