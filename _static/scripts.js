document.addEventListener("DOMContentLoaded", () => {
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
        if (element.href.startsWith("https://")) {
            element.setAttribute("target", "_blank");
        }
    }

    document.getElementById('searchbox').style.display = "block";

    // Theming
    const LOCAL_STORAGE_KEY = 'piccoloThemeMode'

    var initialMode = localStorage.getItem(LOCAL_STORAGE_KEY)

    if (initialMode) {
        // Make sure the value in local storage is valid
        if (['light', 'dark', 'darkest'].indexOf(initialMode) === -1) {
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

            if (currentMode === 'light') {
                this.mode = 'dark'
            } else if (currentMode === 'dark') {
                this.mode = 'darkest'
            } else if (currentMode === 'darkest') {
                this.mode = 'light'
            }

            document.documentElement.dataset.mode = this.mode
            localStorage.setItem(LOCAL_STORAGE_KEY, this.mode)

            console.log(this.mode)
        }
    })

    // Hide theme button in local
    const isLocal = window.location.protocol === "file:";
    if (!isLocal) {
        button.mount('#mode_toggle')
    }
});

function toggleLanguageDropdown(event) {
    event.preventDefault();

    const dropdown = document.getElementById('languageDropdown');
    if (dropdown) {
        dropdown.classList.toggle('active');
    }
}

// Closes language dropdown
window.addEventListener('click', function(event) {
    const dropdown = document.getElementById('languageDropdown');
    if (dropdown && !dropdown.contains(event.target)) {
        dropdown.classList.remove('active');
    }
});
