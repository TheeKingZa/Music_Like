// alert_timer.js

// Wait for the document to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
    // Get the alert container
    var alertContainer = document.getElementById('alert-container');
    // Remove the alert message after 4 seconds
    setTimeout(function () {
        alertContainer.remove();
    }, 4000); // 4 seconds in milliseconds
});
