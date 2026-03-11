document.addEventListener("click", function (event) {

    const dropdowns = document.querySelectorAll(".dropdown");

    dropdowns.forEach(dropdown => {

        const button = dropdown.querySelector(".dropdown-button");

        if (button.contains(event.target)) {
            dropdown.classList.toggle("open");
        } else {
            dropdown.classList.remove("open");
        }
    });
});