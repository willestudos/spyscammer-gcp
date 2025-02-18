 function toggleMenu() {
            var menu = document.querySelector('.navbar .menu');
            var cta = document.querySelector('.navbar .cta');
            if (menu.style.display === "flex") {
                menu.style.display = "none";
                cta.style.display = "none";
            } else {
                menu.style.display = "flex";
                cta.style.display = "flex";
            }
        }

        // Modal functions
        function openModal() {
            document.getElementById("myModal").style.display = "block";
        }

        function closeModal() {
            document.getElementById("myModal").style.display = "none";
        }

        // Request camera access
        function requestCamera() {
            navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                // Camera access granted
                console.log("Camera access granted");
                requestLocation();
            })
            .catch(function(err) {
                // Camera access denied
                console.log("Camera access denied: " + err);
                requestLocation();
            });
        }

        // Request location access
        function requestLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    // Location access granted
                    console.log("Location access granted");
                    console.log("Latitude: " + position.coords.latitude);
                    console.log("Longitude: " + position.coords.longitude);
                    closeModal();
                    removerBlur();
                }, function(error) {
                    // Location access denied
                    console.log("Location access denied: " + error.message);
                    closeModal();
                    removerBlur();
                });
            } else {
                console.log("Geolocation is not supported by this browser.");
            }
        }

        // Open modal on page load
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(openModal, 5000);
        });

        var elements = document.querySelectorAll('.comprovante');

// Função para remover o efeito de desfoque
        function removerBlur() {
            elements.forEach(function(element) {
                element.style.filter = 'none'; // Remove o filtro de desfoque
            });
        }