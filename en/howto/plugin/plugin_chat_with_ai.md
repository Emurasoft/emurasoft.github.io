# To use Chat with AI plug-in

## Installation
**Chat with AI** is available as the **ChatAI** plug-in. You can download it from [ChatAI plug-in downloads](https://www.emeditor.com/download-chatai/). The **ChatAI** plug-in is not available for the Store App.

### Desktop
1. If you use the **Desktop Installer** version of EmEditor, click **Installer** to download the installer version
2. Run the downloaded installer.
3. Open EmEditor and go to **Customize** > **AI Options**. Check **Enable AI**.

### Portable
1. If you use the **Portable** version of EmEditor, click **Zip archive** to download the zip file.
2. Unzip the `ChatAI.dll` file to the `PlugIns` folder in your EmEditor folder.
3. Navigate to [**Customize Plug-ins**](../../cmd/tools/customize_plug_ins) in EmEditor and **Add** the `ChatAI.dll` file.
4. Open EmEditor and go to **Customize** > **AI Options**. Check **Enable AI**.

## API Key
To start using Chat with AI, create and copy an API key from one of these AI providers.

### Deepseek
1. Log into your Deepseek account and visit the [API keys page](https://platform.deepseek.com/api_keys).
2. Click **Create new API key**. Add a name for the key.
3. Copy the API key.

### Google
1. Log into your Google AI Studio account and visit the [API keys page](https://aistudio.google.com/u/1/apikey).
2. Click **+ Create API Key**.
3. If prompted, select an existing Google Cloud project to create the API key.
4. Copy the API key.

### OpenAI
1. Log into your OpenAI account and visit the [API keys page](https://platform.openai.com/api-keys).
2. Click **Create a new secret key**. Optionally, add a name and select any project.
3. Select **All** permissions, or select **Restricted** and add the required permissions below. The required resources may change in the future as new features are added:
   - **Model capabilities**: **Write**
   - **Responses API**: **Write**
   - All other resources: **None**
4. Copy the generated API key.

## Setup
1. After **ChatAI** is installed, the **AI** menu should appear in the main menu. Open the **AI** menu and select **Chat with AI**.
2. In the **Chat with AI** app, click the ⚙️ button in the sidebar and select **Settings**.
3. Select the **Provider** of your choice.
4. Paste your API key into the **API key** field.

## Chat panel
- Type your question or prompt in the input box at the bottom and press Enter or click **&#8593;** to send.
- Your message appears on the right; the AI’s response will appear just below it shortly. Prompts and responses remain in the conversation for context-aware replies.
- Hover over any message to see buttons for:
  - **Copy to clipboard**: Copies the message to clipboard
  - **Copy to New Document**: Opens a new document and inserts the text.
  - **Edit message**: Make revisions to the message.
  - **Regenerate response**: Requests a new reply based on the same prompt. Useful if you would like a different phrasing.
- Click the **⋯** button or right-click on any message for additional options:
  - **Copy to Editor**: Inserts the text at the cursor position in the editor.
  - **Message Info**: Displays details about this message.
- Code blocks contain programming code. In a code block, you can click on **⋯** for options to copy the code.

## Chat input
* Enter your prompts in the input box at the bottom of the chat panel.
* Click **+ File** to upload a file.
  * This feature is available only when using OpenAI. Only files with [supported extensions](https://platform.openai.com/docs/guides/tools-file-search#supported-files) can be uploaded.
  * When a supported file is opened in the editor, its document name appears in the file selection dropdown.
  * You can also click **Browse** to select a supported file using the file browser dialog.
  * When a file is uploaded, Chat with AI creates both a file and a vector store resources in OpenAI. The file can then be referenced during chat conversations.
  * Uploaded files are listed in the input area. Click a file to remove it, or right-click for additional options.
  * Referencing uploaded files typically consumes fewer tokens than copying and pasting the file contents directly into the chat.
  * For details on file search costs, see [OpenAI pricing](https://platform.openai.com/docs/pricing#built-in-tools).
* Enable **Tools** to use the tool-calling feature. These EmEditor tools can used by the AI to read or modify your document.
  * Tools are available only for OpenAI and DeepSeek.
  * Hover over **Tools** and select **Settings** to view and configure the available tools.

## Sidebar
- Conversations are listed in the sidebar. Click on **+ New chat** to create a new chat that contains a different conversation. Responses in a chat will use the context of messages in that chat conversation only.
- Click on **&#8230;** on any entry for these options:
  - **Delete Chat**: Clears all messages in that chat.
  - **Copy to New Document**: Copies all messages in the conversation to a new document.
- You can hide the sidebar with the **Close sidebar** button.

## Search

* Click the 🔍 button in the sidebar to search for chat messages.
* Enter a keyword in the search box to display matching messages.
* In the results list, select a message to jump directly to its location in the chat panel.

## Settings
- You can change AI connection and user interface settings by clicking the ⚙️ button in the sidebar and selecting **Settings**.
- **AI Connection**
  - Configure how the app connects to an AI service.
  - You can select the following providers: Deepseek, LM Studio/OpenAI compatible, OpenAI
  - Clicking on **Test Connection** checks that the settings are correct for the provider by sending a small AI request.
- **AI Parameters**
  - Adjust parameters for AI generation.
  - Chat completion and reasoning models are supported.
  - Read the providers' documentation for more details about each setting.
    - [Deepseek](https://api-docs.deepseek.com/api/create-chat-completion)
    - [Google](https://ai.google.dev/api/generate-content)
    - [OpenAI](https://platform.openai.com/docs/api-reference/chat/create)
- **Tool Calling**
  - These EmEditor tools can be made accessible to the AI to read or modify your document.
  - Using tools will incur additional token costs.
  - Tool calling can be enabled from the chat input by clicking on the **Tools** button.
- **Files**
  - These options for the OpenAI file search feature control the expiration of files and vector stores.
- **User Interface**
  - These settings customize the Chat with AI interface.
- **Debug Log Options**
  - The debug log helps diagnose technical issues with the app.
- **Update**
  - Allows you to manually update the app.
- **Reset Settings**
  - Deletes all chats or reset all settings to default.

## Uploaded files
* To view uploaded files and vector stores, click the ⚙️ button in the sidebar and select **Uploaded Files**.
* The dialog displays all files and vector stores associated with your OpenAI account or organization. For each vector store, the associated chat and current status are also shown.
  * Expired vector stores do not incur storage costs.
* You can select and delete files or vector stores from your account or organization.

## LM Studio setup instructions
The LM Studio integration requires initial setup. Follow these steps to set up LM Studio.

1. Download and install LM studio from [lmstudio.ai](https://lmstudio.ai/).
2. In LM Studio, go to the **Discover** tab to download a model.
    - `mistralai/mistral-7b-instruct-v0.3` is a good model to try, as it can run on most computers.
    - Attempting to load a model unsupported by your system may result in an error.
3. At the top of the LM Studio window, load the model that you downloaded.
4. Go to the **Developer** tab. Click on the switch on the top left to start the server. It should now say "Status: Running".
5. Open the **Settings** next to the switch. **Enable CORS**.
6. Open **Chat with AI** and open **Settings**.
7. In the **AI Connection** page, set the **Provider** to "LM Studio/OpenAI compatible". Leave the **API key** field empty.
8. Go to the **AI Parameters** page. Under **Model**, select the model you downloaded. 
   - If it is not listed, verify that CORS is enabled in LM Studio. You can manually enter the model name by selecting "Other".
9. Go back to **AI Connection**, and click **Test Connection** to ensure that it can connect to LM Studio.

- Each time you restart your computer, the LM Studio service starts automatically. However, you’ll need to manually load a model before you can use it in Chat with AI.