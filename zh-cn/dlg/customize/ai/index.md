# “AI”页面

**AI** 页面让您能自定义与人工智能相关的设置。

## “启用 AI”复选框

在 EmEditor 中可以用 [**OpenAI**](https://openai.com/) 来辅助写作。要启用此功能，您必须在每个配置属性的 [**常规**](../../properties/general/index) 页面中勾选 **AI 辅助写作** 复选框。该功能需要 [**OpenAI API 密钥**](https://platform.openai.com/api-keys) 才能使用。

## “使用 'OPENAI_API_KEY' 环境变量”复选框

如果选中此选项，将使用 “OPENAI_API_KEY” 环境变量保存 OpenAI API 密钥。这是 OpenAI 推荐的存储方式，并与其他应用程序共享。如果未勾选此选项，则将保存 API 密钥以仅供 EmEditor 使用。

## “OpenAI API 密钥”文本框

指定 OpenAI API 密钥。您可以单击此文本框右侧的 **o-o** 来切换字符的显示/隐藏。在您修改此文本框并单击对话框中的 **确定** 按钮之后，EmEditor 将执行与 OpenAI API 的连接测试，以检查输入的 API 密钥是否有效。

## “首选模型”下拉列表框

指定您要使用的模型的名称。您可以从列表中选择已定义的模型名称，也可以直接输入未定义的模型名称。根据所使用的模型，AI 的响应可能有所不同，OpenAI 的使用费也可能有所不同。如果您指定未定义的模型名称并单击 **确定** 按钮，EmEditor 将执行与 OpenAI API 的连接测试以检查输入的模型名称是否有效。

## 「重置」按钮

重置为默认设定。

