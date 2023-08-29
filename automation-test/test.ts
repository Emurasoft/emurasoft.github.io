import {Builder, logging} from 'selenium-webdriver';
import * as chrome from 'selenium-webdriver/chrome'
import {resolve} from 'path';
import {strict as assert} from 'assert';

async function main() {
    for (const language of ['en', 'ja', 'ko', 'zh-cn', 'zh-tw']) {
        await test(language);
    }
}

async function test(language: string) {
    console.log(`language: ${language}`);

    const options = new chrome.Options();
    options.headless()

    const logPreferences = new logging.Preferences();
    logPreferences.setLevel(logging.Type.BROWSER, logging.Level.WARNING);
    const driver = await new Builder()
        .forBrowser('chrome')
        .setLoggingPrefs(logPreferences)
        .setChromeOptions(options)
        .build();

    const url = new URL('file:///');
    url.pathname = resolve(`../_build/${language}/index.html`);

    await driver.get(url.toString());

    const logEntries = await driver.manage().logs().get(logging.Type.BROWSER);
    assert.equal(logEntries.length, 0);

    await driver.quit();
}

main();