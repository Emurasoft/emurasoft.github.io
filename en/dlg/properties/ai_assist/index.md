# AI Assist page

The **AI Assist** page allows you to set properties related to AI assisted writing.

## Enable AI-assisted writing checkbox

If this is checked, EmEditor will enable AI assisted writing. 

## Show suggestions only on Ctrl+Space checkbox

If this is checked, EmEditor will only show suggestions when you press the shortcut key, Ctrl+Space, which helps reduce the frequency of AI calls.

## Show suggestions only when confident checkbox

If you do not want to receive AI suggestions too frequently, you can check this option to show suggestions only when the AI is confident. When this is checked, you can use the **Confidence level** slider below it to set the minimum confidence level required to display a suggestion. Because judging confidence is difficult for AI, and some AI models may not interpret it correctly, we recommend turning this off if you do not need it.

## Set the temperature checkbox

In AI, **temperature** is a parameter that controls the "randomness (creativity)" used when the LLM chooses the next word while generating text. The lower the temperature, the lower the randomness, and the more deterministic the suggestions you receive. The higher the temperature, the higher the randomness, and the more creative the suggestions you receive. When the **Set the temperature** option is off, the model's default temperature is always used. When it is on, a temperature of 0.0 is used initially so that you receive deterministic suggestions; however, when you press Ctrl + Space to request a different suggestion, the temperature is raised to produce more creative suggestions. Many recent reasoning models do not accept a temperature parameter, in which case this option is ignored. If an error appears on the status bar because the temperature cannot be set for a particular model, please turn this option off. For AI-assisted writing, we recommend specifying a lightweight model that returns responses quickly, rather than a reasoning model.

## Don't show suggestions after any of the following checkbox

If you check this and enter characters that indicate the end of a sentence in the field below—for example, ".。"—suggestions will no longer appear after symbols such as "." or "。". This lets you tailor the feature for easy use according to the type of text you are editing.

## Confidence level slider

Use this slider to adjust the confidence level in AI decisions. For instance, if you set the confidence to 40%, the AI will show suggestions only when it predicts the next text with at least 40% confidence. To minimize suggestions from less certain predictions, you can set a higher confidence, like 80%, ensuring that suggestions are shown only when predictions are more reliable, thus reducing the number of OpenAI API calls.

## Input length slider

Use this slider to adjust the input length. Using longer input text for predictions increases accuracy but also raises the OpenAI API usage fee.

## Output length slider

Use this slider to adjust the output length. Longer output text results in more words being suggested.

## Delay time slider

AI suggestions appear automatically after the specified amount of time has elapsed once typing stops and the editor becomes idle. You can adjust this delay time in milliseconds using the slider.

## Additional instructions text box

Here, you can add instructions such as what kind of suggestions you want to receive, which language to use, and the desired tone. For example, when writing code in JavaScript, you can specify "Use JavaScript," and if you want to use polite language, you can specify "Write in a polite style." However, depending on the AI model, these additional instructions may not always be fully understood or produce an appropriate response, and entering too many instructions may slow down the response.

## Reset button

Resets to default settings. The [**Reset** dialog box](../reset/index) will be displayed and will allow you to copy from another configuration.

## Notes

This page is available only when the **ChatAI** plugin is installed and enabled.
