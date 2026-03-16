const setTheme = (theme) => {
    document.documentElement.setAttribute("data-theme", theme)
    localStorage.setItem("theme", theme)
}

const loadTheme = () => {

    const savedTheme = localStorage.getItem("theme")

    if (savedTheme) {
        document.documentElement.dataset.theme = savedTheme
    } else {
        document.documentElement.dataset.theme = "night"
    }

}

loadTheme()