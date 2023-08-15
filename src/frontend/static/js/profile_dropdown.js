document.addEventListener('DOMContentLoaded', function () {
    const dropdownButton = document.querySelector('.relative.inline-block button');
    const dropdownMenu = document.querySelector('.absolute.right-0');

    dropdownButton.addEventListener('click', function () {
        dropdownMenu.classList.toggle('hidden');
    });
});