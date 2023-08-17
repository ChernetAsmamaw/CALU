
// Get the form element
const form = document.getElementById('myForm');

// Handle form submission
form.addEventListener('submit', function (event) {
  // Prevent the form from submitting
  event.preventDefault();

  // Validate the form inputs
  if (form.checkValidity()) {
    // If the form is valid, you can proceed with form submission or further processing
    // For example, you can send an AJAX request to your Django backend here
    console.log('Form is valid. Submitting...');
    // Perform your form submission or further processing here
  } else {
    // If the form is invalid, you can display error messages or take appropriate actions
    console.log('Form is invalid. Please fill in all required fields.');
  }
});