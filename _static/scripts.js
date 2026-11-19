const THEME_STORAGE_KEY = 'piccoloThemeMode'

document.addEventListener("DOMContentLoaded", () => {
    const initialMode = initTheme();
    initThemeToggle(initialMode);

    injectSidebarNav();

    // Scroll sidebar to current page
    // Last item in array is current item
    const itemElements = document.querySelectorAll("li.current");
    if (itemElements.length > 0) {
        // Scroll to first child in item
        let focusElement = itemElements[itemElements.length - 1];
        if (focusElement.firstChild) {
            focusElement = focusElement.firstChild;
        }

        focusElement.scrollIntoView({block: "center"});
    }

    // Hide empty table header
    for (const element of document.querySelectorAll("th.head")) {
        if (element.innerText === "") {
            element.style.display = "none";
        }
    }

    // External links
    for (const element of document.getElementsByTagName("a")) {
        const href = element.getAttribute('href');
        if (href && href.startsWith("https://")) {
            element.setAttribute("target", "_blank");
        }
    }

    // The search page has no search box.
    const searchbox = document.getElementById('searchbox');
    if (searchbox) {
        searchbox.style.display = "block";
    }

    // Language dropdown
    const dropdown = document.getElementById('languageDropdown-title');
    if (dropdown) {
        dropdown.addEventListener('click', function(event) {
            event.preventDefault();
            document.getElementById('languageDropdown').classList.toggle('active');
        });
    }


    if (document.getElementById('languageDropdown-en')) {
        const languages = ['en', 'ja', 'ko', 'zh-cn', 'zh-tw'];

        for (const language of languages) {
            document.getElementById('languageDropdown-' + language).addEventListener('click', function(event) {
                event.preventDefault();
                changeLanguage(language);
            });
        }
    }
});

// Apply the saved theme (or the system preference). Runs before any
// page-specific setup so a missing element cannot leave the page unthemed.
function initTheme() {
    let initialMode = localStorage.getItem(THEME_STORAGE_KEY)

    if (initialMode) {
        // Make sure the value in local storage is valid
        if (['light', 'dark', 'darkest'].indexOf(initialMode) === -1) {
            initialMode = 'light'
            localStorage.setItem(THEME_STORAGE_KEY, initialMode)
        }
    } else {
        // Check if the client prefers dark mode
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            initialMode = 'dark'
        } else {
            initialMode = 'light'
        }
        localStorage.setItem(THEME_STORAGE_KEY, initialMode)
    }

    document.documentElement.dataset.mode = initialMode
    return initialMode
}

// Mount the theme toggle button, which is hidden when Help is opened from local files.
function initThemeToggle(initialMode) {
    const button = PetiteVue.createApp({
        'mode': initialMode,
        handleClick() {
            let currentMode = this.mode

            if (currentMode === 'light') {
                this.mode = 'dark'
            } else if (currentMode === 'dark') {
                this.mode = 'darkest'
            } else if (currentMode === 'darkest') {
                this.mode = 'light'
            }

            document.documentElement.dataset.mode = this.mode
            localStorage.setItem(THEME_STORAGE_KEY, this.mode)

            console.log(this.mode)
        }
    })

    const isLocal = window.location.protocol === "file:";
    if (!isLocal) {
        button.mount('#mode_toggle')
    }
}

// Insert the current section's sidebar branch from the shared nav.js data.
// build_sidebar_nav.py removes that branch from every page and stores it in
// _static/nav.js, keyed by the section's index page.
function injectSidebarNav() {
    const nav = window.SIDEBAR_NAV;
    if (!nav || typeof getPageName !== 'function') {
        return;
    }

    const sidebar = document.querySelector('.sphinxsidebarwrapper');
    if (!sidebar) {
        return;
    }

    const currentItem = sidebar.querySelector('li.toctree-l1.current');
    if (!currentItem) {
        return;
    }

    const currentLink = currentItem.querySelector('a');
    if (!currentLink) {
        return;
    }

    const pagePath = getPageName() + '.html';
    const sectionKey = rootRelative(currentLink.getAttribute('href'), pagePath);
    if (!sectionKey) {
        return;
    }

    let fragment = null;
    if (nav.pages && nav.pages[pagePath]) {
        fragment = nav.pages[pagePath];
    } else if (nav.sections && nav.sections[sectionKey]) {
        fragment = nav.sections[sectionKey];
    }
    if (!fragment) {
        return;
    }

    const template = document.createElement('template');
    template.innerHTML = fragment;
    markCurrentEntries(template.content, pagePath);

    // A page cached from before the sidebar split still carries its own list.
    const existing = currentItem.querySelector(':scope > ul');
    if (existing) {
        existing.remove();
    }

    const root = document.documentElement.dataset.content_root;
    currentItem.insertAdjacentHTML('beforeend', template.innerHTML.replaceAll('{{ROOT}}', root));
}

// Restore the "current" markers that build_sidebar_nav.py removed from the
// fragment: the entry for this page, and its ancestor index entries.
function markCurrentEntries(container, pagePath) {
    const marker = '{{ROOT}}';

    for (const link of container.querySelectorAll('a')) {
        const href = link.getAttribute('href');
        if (!href || !href.startsWith(marker)) {
            continue;
        }

        const resolved = href.slice(marker.length);
        const hashIndex = resolved.indexOf('#');
        const target = hashIndex < 0 ? resolved : resolved.slice(0, hashIndex);
        const fragment = hashIndex < 0 ? '' : resolved.slice(hashIndex);
        const item = link.closest('li');
        const isPage = target === pagePath;
        const isIndex = target === 'index.html' || target.endsWith('/index.html');
        const isAncestor = isIndex && target !== 'index.html'
            && pagePath.startsWith(target.slice(0, -'index.html'.length));

        if (isPage) {
            link.classList.add('current');
            // Sphinx links the current entry to the page itself with "#".
            link.setAttribute('href', '#' + fragment.slice(1));
        }
        if ((isPage || isAncestor) && item) {
            item.classList.add('current');
        }
    }

    // Sphinx marks a list current when it has a current direct child.
    for (const list of container.querySelectorAll('ul')) {
        if (list.querySelector(':scope > li.current')) {
            list.classList.add('current');
        }
    }
}

// Normalize a sidebar href to a path relative to the build root, the same way
// build_sidebar_nav.py does. Returns null for hrefs outside the build.
function rootRelative(href, pagePath) {
    if (!href) {
        return null;
    }
    if (href.startsWith('#')) {
        return pagePath + href.slice(1);
    }
    if (href.startsWith('/') || href.includes(':')) {
        return null;
    }

    const base = pagePath.slice(0, pagePath.lastIndexOf('/') + 1);
    const normalized = [];
    for (const part of (base + href).split('/')) {
        if (part === '' || part === '.') {
            continue;
        }
        if (part === '..') {
            normalized.pop();
        } else {
            normalized.push(part);
        }
    }

    return normalized.join('/');
}

function changeLanguage(lang) {
    const newPath = 'https://help.emeditor.com/' + lang + '/' + getPageName() + '.html';
    window.location.href = newPath;
}

// Closes language dropdown
window.addEventListener('click', function(event) {
    const dropdown = document.getElementById('languageDropdown');
    if (dropdown && !dropdown.contains(event.target)) {
        dropdown.classList.remove('active');
    }
});