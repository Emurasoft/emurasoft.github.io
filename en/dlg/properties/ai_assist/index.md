# AI Assist page

The **AI Assist** page allows you to set properties related to AI assisted writing.

## Enable AI assisted writing check box

If this is checked, EmEditor will enable AI assisted writing. 

## Show suggestion only on Ctrl+Space check box

If this is checked, EmEditor will only show suggestions when you press the shortcut key, Ctrl+Space, which helps reduce the frequency of OpenAI API calls.

## Confidence level slider

Use this slider to adjust the confidence level in AI decisions. For instance, if you set the confidence to 40%, the AI will show suggestions only when it predicts the next text with at least 40% confidence. To minimize suggestions from less certain predictions, you can set a higher confidence, like 80%, ensuring that suggestions are shown only when predictions are more reliable, thus reducing the number of OpenAI API calls.

## Input length slider

Use this slider to adjust the input length. Using longer input text for predictions increases accuracy but also raises the OpenAI API usage fee.

## Output length slider

Use this slider to adjust the output length. Longer output text results in more words being suggested.

## Reset button

Resets to default settings. The [**Reset** dialog box](../reset/index) will be displayed and will allow you to copy from another configuration.

