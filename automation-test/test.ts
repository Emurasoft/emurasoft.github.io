import {Builder, logging} from 'selenium-webdriver';
import {resolve} from 'path';
import {strict as assert} from 'assert';

async function main() {
    const logPreferences = new logging.Preferences();
    logPreferences.setLevel(logging.Type.BROWSER, logging.Level.WARNING);
    const driver = await new Builder()
        .forBrowser('chrome')
        .setLoggingPrefs(logPreferences)
        .build();

    const url = new URL('file:///');
    url.pathname = resolve('../_build/en/index.html');

    await driver.get(url.toString());

    const logEntries = await driver.manage().logs().get(logging.Type.BROWSER);
    assert.equal(logEntries.length, 0);

    await driver.quit();
}

main();