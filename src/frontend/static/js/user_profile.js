document.getElementById('saveButton').addEventListener('click', function () {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    alert(`Saved! \nUsername: ${username} \nEmail: ${email}`);
});