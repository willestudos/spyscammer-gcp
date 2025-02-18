document.addEventListener("DOMContentLoaded", function() {
    var alertDiv = document.getElementById("alertMessage");
        if (alertDiv) {
            setTimeout(function() {
                alertDiv.style.display = "none";
            }, 3000); // 2000 milissegundos = 2 segundos
        }
});

