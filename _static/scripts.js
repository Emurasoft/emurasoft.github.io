document.addEventListener("DOMContentLoaded", () => {
    // Replace <pro /> and <profree /> tags
    const proTitle = `
                {% if language == "en" %}
                    EmEditor Professional only
                {% elif language == "ja" %}
                    EmEditor Professional のみ
                {% elif language == "ko" %}
                {% elif language == "zh-CN" %}
                    仅限 EmEditor 专业版
                {% elif language == "zh-TW" %}
                    僅限 EmEditor 專業版
                {% endif %}
            `;
    const proFreeTitle = `
                {% if language == "en" %}
                    EmEditor Professional and EmEditor Free
                {% elif language == "ja" %}
                    EmEditor Professional と EmEditor Free
                {% elif language == "ko" %}
                {% elif language == "zh-CN" %}
                    仅限 EmEditor 专业版
                {% elif language == "zh-TW" %}
                    EmEditor 專業版和 EmEditor 免費版
                {% endif %}
            `;

    for (const element of document.querySelectorAll("pro")) {
        element.textContent = "[P]";
        element.setAttribute("title", proTitle.trim());
        element.style.verticalAlign = "super";
        element.style.fontSize = "smaller";
        element.style.cursor = "help";
    }

    for (const element of document.querySelectorAll("profree")) {
        element.textContent = "[PF]";
        element.setAttribute("title", proFreeTitle.trim());
        element.style.verticalAlign = "super";
        element.style.fontSize = "smaller";
        element.style.cursor = "help";
    }

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
    for (const element of document.querySelectorAll("a.external")) {
        element.setAttribute("target", "_blank");
    }

    document.getElementById('searchbox').style.display = "block";
});

function changeLanguage(lang) {
    const currentLevel = ('{{ pagename }}'.match(/\//g)||[]).length + 1;
    const newPath = '../'.repeat(currentLevel) + lang + '/{{ pagename }}.html';
    window.location.href = newPath;
}

function toggleLanguageDropdown() {
    const dropdown = document.querySelector('.languageDropdown');
    dropdown.classList.toggle('active');
}

// Closes language dropdown
window.addEventListener('click', function(event) {
    const dropdown = document.querySelector('.languageDropdown');
    if (!dropdown.contains(event.target)) {
        dropdown.classList.remove('active');
    }
});

// Theming
(function() {
    const LOCAL_STORAGE_KEY = 'piccoloThemeMode'

    var initialMode = localStorage.getItem(LOCAL_STORAGE_KEY)

    if (initialMode) {
        // Make sure the value in local storage is valid
        if (['light', 'dark', 'darkest'].indexOf(initialMode) == -1) {
            initialMode = 'light'
            localStorage.setItem(LOCAL_STORAGE_KEY, initialMode)
        }
    } else {
        // Check if the client prefers dark mode
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            initialMode = 'dark'
        } else {
            initialMode = 'light'
        }
        localStorage.setItem(LOCAL_STORAGE_KEY, initialMode)
    }

    document.documentElement.dataset.mode = initialMode

    const button = PetiteVue.createApp({
        'mode': initialMode,
        handleClick() {
            let currentMode = this.mode

            if (currentMode == 'light') {
                this.mode = 'dark'
            } else if (currentMode == 'dark') {
                this.mode = 'darkest'
            } else if (currentMode == 'darkest') {
                this.mode = 'light'
            }

            document.documentElement.dataset.mode = this.mode
            localStorage.setItem(LOCAL_STORAGE_KEY, this.mode)

            console.log(this.mode)
        }
    })

    const enableButton = window.location.protocol !== "file:";

    if (enableButton) {
        button.mount('#mode_toggle')
    }
})();
