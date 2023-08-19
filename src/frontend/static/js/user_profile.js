document.getElementById('saveButton').addEventListener('click', function () {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    const message = `Saved!<br><br>`;

    Swal.fire({
        title: 'You\'ve Successfully Updated Your User Profile!',
        html: message,
        icon: 'success',
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'OK'
    });
});