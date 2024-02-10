function openMenu() {
    let toggleBtn = document.querySelector('.toggle_btn');
    let dropdownMenu = document.querySelector('.dropdown_menu');
    let menuText = document.querySelector('.menu_text');
    function openDropdown() {
        dropdownMenu.classList.toggle('open');
        const menuIsOpen = dropdownMenu.classList.contains('open');
        menuText.innerHTML = menuIsOpen ? 'Close menu <i class="fa-solid fa-xmark"></i>' : 'Open menu <i class="fa-solid fa-bars"></i>';
        toggleBtn.style.marginBottom = menuIsOpen ? '2em' : '0';
    }
    toggleBtn.addEventListener('click', openDropdown);
}

addEventListener('load', openMenu);

function openProfile() {
    const profilePage = document.getElementById('profile').getAttribute('data-url');
    window.location.href = profilePage;
}

function openTask (event) {
    const taskPage = event.currentTarget.getAttribute('data-url-task');
    window.location.href = taskPage;
}