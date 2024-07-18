document.addEventListener('DOMContentLoaded', function () {
    // Highlight the active navigation link
    highlightActiveLink();

    // Form validation for login and registration forms
    validateForms();
});

function highlightActiveLink() {
    const currentLocation = window.location.href;
    const navLinks = document.querySelectorAll('.nav-list a');
    
    navLinks.forEach(link => {
        if (link.href === currentLocation) {
            link.classList.add('active');
        }
    });
}

function validateForms() {
    const loginForm = document.querySelector('form[action="/login"]');
    const registerForm = document.querySelector('form[action="/register"]');

    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            const email = loginForm.querySelector('#email');
            const password = loginForm.querySelector('#password');

            if (!email.value || !password.value) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            const username = registerForm.querySelector('#username');
            const email = registerForm.querySelector('#email');
            const password = registerForm.querySelector('#password');

            if (!username.value || !email.value || !password.value) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }
}