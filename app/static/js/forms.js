document.addEventListener('DOMContentLoaded', () => {
    // Function to validate password match
    function validatePasswordMatch(password, confirmPassword) {
        return password === confirmPassword;
    }

    // Function to show validation error
    function showValidationError(message) {
        alert(message);
    }

    // Function to handle registration form submission
    const registrationForm = document.getElementById('registrationForm');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const username = document.getElementById('username').value;
            const firstName = document.getElementById('first_name').value;
            const otherName = document.getElementById('other_name').value;
            const lastName = document.getElementById('last_name').value;
            const email = document.getElementById('email').value;
            const address = document.getElementById('address').value;
            const phone = document.getElementById('phone_number').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm_password').value;

            if (!validatePasswordMatch(password, confirmPassword)) {
                showValidationError('Passwords do not match');
                return;
            }

            // Add further validations and AJAX call to submit the form data to the server

            console.log('Registration Form Submitted');
        });
    }

    // Function to handle login form submission
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const email = document.getElementById('login_email').value;
            const password = document.getElementById('login_password').value;

            // Add further validations and AJAX call to submit the form data to the server

            console.log('Login Form Submitted');
        });
    }

    // Function to handle update account form submission
    const updateAccountForm = document.getElementById('updateAccountForm');
    if (updateAccountForm) {
        updateAccountForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const username = document.getElementById('update_username').value;
            const firstName = document.getElementById('update_first_name').value;
            const otherName = document.getElementById('update_other_name').value;
            const lastName = document.getElementById('update_last_name').value;
            const phone = document.getElementById('update_phone').value;
            const address = document.getElementById('update_address').value;
            const email = document.getElementById('update_email').value;

            // Add further validations and AJAX call to submit the form data to the server

            console.log('Update Account Form Submitted');
        });
    }
});