import {Builder, By, logging} from 'selenium-webdriver';
import * as chrome from 'selenium-webdriver/chrome.js'
import {readFile} from 'fs/promises';
import {resolve} from 'path';
import {pathToFileURL} from 'url';
import {strict as assert} from 'assert';

async function main() {
    const driver = await createDriver();
    try {
        for (const language of ['en', 'ja', 'ko', 'zh-cn', 'zh-tw']) {
            await test(driver, language);
        }
    } finally {
        await driver.quit();
    }
}

async function createDriver() {
    const logPreferences = new logging.Preferences();
    logPreferences.setLevel(logging.Type.BROWSER, logging.Level.WARNING);
    return new Builder()
        .forBrowser('chrome')
        .setLoggingPrefs(logPreferences)
        .setChromeOptions(new chrome.Options().addArguments('--headless=new'))
        .build();
}

async function test(driver, language: string) {
    console.log(`language: ${language}`);

    // The generated page keeps the top-level links but not the branch.
    const raw = await readFile(resolve(`../_build/${language}/cmd/index.html`), 'utf8');
    // The minifier omits optional </li> end tags, so stop at the next item or list end.
    const currentItem = raw.match(/<li class="toctree-l1 current">(?:(?!<li\b|<\/ul>)[\s\S])*/);
    assert.ok(currentItem, 'the sidebar should have a current section');
    assert.ok(!currentItem[0].includes('<ul'), 'the branch should not be in the page');
    assert.ok(raw.includes('/_static/nav.js'), 'the page should load nav.js');

    await load(driver, language, 'index.html');
    await load(driver, language, 'cmd/index.html');

    // Top-level links stay in the page; the current section's branch is injected.
    const topLevelItems = await driver.findElements(By.css('.sphinxsidebar > .sphinxsidebarwrapper > ul > li'));
    assert.ok(topLevelItems.length > 1, 'the sidebar should keep its top-level links');

    const branchLists = await driver.findElements(By.css('.sphinxsidebar li.toctree-l1.current > ul'));
    assert.equal(branchLists.length, 1, 'the current section should have exactly one branch list');

    const branchLinks = await driver.findElements(By.css('.sphinxsidebar li.toctree-l1.current > ul > li > a'));
    assert.ok(branchLinks.length > 0, 'the injected branch should contain links');

    // The section index is not one of its own children, so no list is current.
    const sectionLists = await driver.findElements(By.css('.sphinxsidebar li.toctree-l1.current > ul.current'));
    assert.equal(sectionLists.length, 0, 'the section index should not mark the branch list current');

    // A category index page is the current page itself.
    const categoryUrl = await branchLinks[0].getAttribute('href');
    await navigate(driver, categoryUrl);

    const currentLinks = await driver.findElements(By.css('.sphinxsidebar li.toctree-l2.current > a.current'));
    assert.equal(currentLinks.length, 1, 'the category index should be highlighted');
    assert.equal(await currentLinks[0].getDomAttribute('href'), '#',
        'the current entry should link to the page itself');
    const categoryLists = await driver.findElements(By.css('.sphinxsidebar li.toctree-l1.current > ul.current'));
    assert.equal(categoryLists.length, 1, 'the branch list should be current on a child page');
    await assertRootMarkerResolved(driver);

    // A page inside the category marks its ancestor category, not itself.
    const contentLinks = await driver.findElements(By.css('.document .body table a'));
    assert.ok(contentLinks.length > 0, 'the category index should list pages');
    await navigate(driver, await contentLinks[0].getAttribute('href'));

    const ancestorItems = await driver.findElements(By.css('.sphinxsidebar li.toctree-l2.current'));
    assert.equal(ancestorItems.length, 1, 'the ancestor category should be marked');
    const ancestorLinks = await ancestorItems[0].findElements(By.css(':scope > a.current'));
    assert.equal(ancestorLinks.length, 0, 'the ancestor category link should not be marked');
    const ancestorAnchor = await ancestorItems[0].findElement(By.css(':scope > a'));
    assert.equal(await ancestorAnchor.getAttribute('href'), categoryUrl,
        'the ancestor category should link to the category index');
    await assertRootMarkerResolved(driver);
}

async function assertRootMarkerResolved(driver) {
    const html = await driver.executeScript("return document.querySelector('.sphinxsidebar').innerHTML");
    assert.ok(!html.includes('{{ROOT}}'), 'the root marker should be resolved');
}

async function load(driver, language: string, page: string) {
    await navigate(driver, pathToFileURL(resolve(`../_build/${language}/${page}`)).href);
}

async function navigate(driver, url: string) {
    await driver.get(url);
    const logEntries = await driver.manage().logs().get(logging.Type.BROWSER);
    assert.equal(logEntries.length, 0, JSON.stringify(logEntries));
}

await main();
