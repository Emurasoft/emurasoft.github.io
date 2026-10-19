# 将 EmEditor 用作 Claude Code 的编辑器

在 Claude Code 的[交互模式](https://code.claude.com/docs/en/interactive-mode)下按 Ctrl+G 时，会打开记事本，以便编辑提示文本。按照以下步骤，可以将按 Ctrl+G 时打开的编辑器更改为 EmEditor。

1. 退出 Claude Code。
2. 确认 EmEditor 位于 `PATH` 中。如果使用桌面安装程序安装，通常已经设置好了。如果使用便携版，请按如下方式设置 `PATH`：
   1. 打开 Windows“开始”菜单，搜索 **环境变量**，然后选择 **编辑账户的环境变量**。
   2. 在 **系统属性** 中，单击 **环境变量** 按钮。
   3. 在 **用户变量** 部分中，选择 **Path** 项，然后单击 **编辑**。
   4. 单击 **新建**，然后粘贴 EmEditor 安装文件夹的路径。
   5. 在每个打开的窗口中单击 **确定** 以保存。
   6. 关闭并重新打开终端，使新的 `PATH` 生效。
3. 在 EmEditor 中打开文件 `%USERPROFILE%\.claude\settings.json`。
4. 在 `env` 部分中添加 `VISUAL` 变量：

```json
{
  "env": {
    "VISUAL": "emeditor /sp"
  }
}
```

   - 如果已存在 `"env"` 部分，请在其中添加 `"VISUAL": "emeditor /sp"` 这一行，并确保前一行以逗号结尾。
   - 如果没有 `"env"` 部分，请添加上面显示的整个块。如果文件中已有其他设置，请将 `"env"` 与它们并列添加，并用逗号分隔。
   - 保存文件。
5. 运行 Claude Code。按 Ctrl+G 时，应会打开 EmEditor。在打开的文档中输入文本，然后关闭 EmEditor。输入的文本将显示在 Claude Code 的输入框中。

## 疑难解答

- **在 Claude Code 中按 Ctrl+G 时，EmEditor 没有打开。** 打开终端并运行 `emeditor`。如果 EmEditor 启动，则 `PATH` 设置正确。如果 EmEditor 没有启动，请参见步骤 2。
- **`PATH` 正确，但按 Ctrl+G 时 EmEditor 没有打开。** 将 `VISUAL` 的值更改为 `emeditor.exe` 的完整路径。在 JSON 中，反斜杠必须写成两个以进行转义。例如：

```json
{
  "env": {
    "VISUAL": "C:\\path_to\\EmEditor\\EmEditor.exe /sp"
  }
}
```
