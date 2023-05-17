// make time duration of the alert message 
let timeoutDuration = 3000;

let messageAlerts = document.querySelectorAll('.alert');
messageAlerts.forEach(function (alert) {
    setTimeout(function () {
        alert.remove();
    }, timeoutDuration)
})