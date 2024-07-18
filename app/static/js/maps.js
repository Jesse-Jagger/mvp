let map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 7.9528, lng: -1.0307 },
        zoom: 6
    });

    fetchMarkers();
}

async function fetchMarkers() {
    try {
        const response = await fetch('/api/map/markers');
        const markers = await response.json();

        markers.forEach(marker => {
            if (typeof marker.position.lat === 'number' && typeof marker.position.lng === 'number') {
                const markerElement = new google.maps.marker.AdvancedMarkerElement({
                    position: { lat: marker.position.lat, lng: marker.position.lng },
                    map: map,
                    title: marker.title
                });

                const infoWindow = new google.maps.InfoWindow({
                    content: marker.title
                });

                markerElement.addListener('click', () => {
                    infoWindow.open(map, markerElement);
                });
            } else {
                console.error('Invalid lat/lng values:', marker);
            }
        });
    } catch (error) {
        console.error('Error fetching markers:', error);
    }
}

// Load the Google Maps API asynchronously
function loadGoogleMaps() {
    var script = document.createElement('script');
    script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyD8wpWOJOtJy1KVdiihGcXHlHLVJchcicc&callback=initMap';
    script.defer = true;
    script.async = true;
    document.body.appendChild(script);
}

// Call the function to load the Google Maps API
loadGoogleMaps();

function highlightActiveLink() {
    const currentLocation = window.location.href;
    const navLinks = document.querySelectorAll('.nav-list a');
    
    navLinks.forEach(link => {
        if (link.href === currentLocation) {
            link.classList.add('active');
        }
    });
}