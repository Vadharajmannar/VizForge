document.addEventListener('DOMContentLoaded', function() {
    // Get the "Get Started" button element
    var getStartedBtn = document.getElementById('getStartedBtn');

    // Add a click event listener to the button
    getStartedBtn.addEventListener('click', function(event) {
        // Prevent the default action (e.g., following the link)
        event.preventDefault();

        // Replace this line with the action you want to perform when the button is clicked
        alert('Button clicked!'); // Example action: show an alert
    });
});
