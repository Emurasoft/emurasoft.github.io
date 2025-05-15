# To use Chat with AI

## How to install
Chat with AI is included in the **ChatAI** plug-in. You can download the plug-in from [emeditor.com](https://www.emeditor.com/download-chatai/). We recommend using the installer for easy installation. If you have a portable version of EmEditor, download the zip archive and unzip the `ChatAI.dll` file to the `PlugIns` folder of your EmEditor folder. Go to [**Customize Plug-ins**](../../cmd/tools/customize_plug_ins) and **Add** the `ChatAI.dll` file.

## Setup
1. After **ChatAI** is installed, open EmEditor and open **Tools > Customize... > AI Options**.
2. Log into OpenAI, and go to the [API keys page](https://platform.openai.com/settings/organization/api-keys).
3. Click on **Create a new secret key**. Optionally add a name, and select any project.
4. Select **All** permissions, or select **Restricted** and add the required permission below. The required resources may change in the future as new features are added.
- **Model capabilities**: **Write**
- All other resources: **None**
5. Copy the API key to the **OpenAI API key** field in **AI Options**. Click **OK**.

## Access Chat with AI
Go to **AI > Chat with AI**.

## Chat panel
- There is an input box at the bottom of the chat, in which you can type your questions or prompts. Press enter or click **↑** to send the prompt.
- Your prompt message will show on the right side of the panel. OpenAI's response message will momentarily appear below your prompt. You can add new prompts, and OpenAI will use previous prompts and responses as context for new responses.
- Hover over any prompt and response message to see buttons:
  - **Copy to clipboard**: Copies the prompt or response text to clipboard
  - **Edit message**: Edit your prompt or the response. This allows you to modify the conversation to better suit your topic.
  - **Regenerate response**: Asks OpenAI to try generating the response again, so that the output is slightly different.
- You can right click on any message to open a context menu with these options.
  - **Copy**: Copies to clipboard
  - **Copy to Editor**: Copies the text to the editor, at the caret position.
  - **Copy to New Document**: Opens a new document and copies the text to the editor.
- OpenAI may response with a code block that contains programming code. On the top right of a code block, you can click on **…** to open the menu containing options to copy the code block text.

## Sidebar
- Each chat conversation is listed in the sidebar. Click on **+ New chat** to create a new chat that contains a different conversation. Responses in a chat will use the context of other messages in that chat conversation only.
- Click on *…* on any entry in the list for these options:
  - **Delete Chat**: Deletes all messages in the chat conversation.
  - **Copy to New Document**: Copies all messages in the conversation to a new document.
- Click on **⚙️** (Open menu) for app options.
  - **Debug Log Options**: The debug log helps diagnose technical issues with the app.
  - **Keyboard Shortcuts**: Contains Keyboard shortcuts for Chat with AI
- You can hide the sidebar with the **Close sidebar** button.