// make date time picker to start at 10am to 6pm 
$(document).ready(function () {
    $('.timepicker').timepicker({
        timeFormat: 'HH:mm',
        interval: 60,
        minTime: '10:00',
        maxTime: '18:00',
        defaultTime: '10:00',
        startTime: '10:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});
