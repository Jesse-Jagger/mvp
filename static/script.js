document.addEventListener('DOMContentLoaded', function () {
    // Highlight the active navigation link
    highlightActiveLink();

    // Form validation for login and registration forms
    validateForms();

    // Initialize the map
    window.initMap = initializeMap;
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

function initializeMap() {
    // Create the map centered at a specific location
    const map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 51.505, lng: -0.09 },
        zoom: 13
    });

    // Marker data - replace this with actual data as needed
    const markers = [
        { position: { lat: 51.5, lng: -0.09 }, title: 'Marker 1: A pretty CSS3 popup.<br> Easily customizable.' },
        { position: { lat: 51.51, lng: -0.1 }, title: 'Marker 2: Another popup.' },
        { position: { lat: 51.49, lng: -0.08 }, title: 'Marker 3: Yet another popup.' },
    ];

    // Add markers to the map
    markers.forEach(markerData => {
        const marker = new google.maps.Marker({
            position: markerData.position,
            map: map,
            title: markerData.title
        });

        const infoWindow = new google.maps.InfoWindow({
            content: markerData.title
        });

        marker.addListener('click', function () {
            infoWindow.open(map, marker);
        });
    });
}

function initializeMap() {
    const map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 51.505, lng: -0.09 },
        zoom: 13
    });

    fetch('/api/markers')
        .then(response => response.json())
        .then(markers => {
            markers.forEach(markerData => {
                const marker = new google.maps.Marker({
                    position: markerData.position,
                    map: map,
                    title: markerData.title
                });

                const infoWindow = new google.maps.InfoWindow({
                    content: markerData.title
                });

                marker.addListener('click', function () {
                    infoWindow.open(map, marker);
                });
            });
        })
        .catch(error => console.error('Error fetching markers:', error));
}