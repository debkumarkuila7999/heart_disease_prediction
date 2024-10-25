document.getElementById('predictionForm').addEventListener('submit', function(event) {
    // Get all input elements that are required
    const requiredFields = document.querySelectorAll('input[required], select[required]');
    let formIsValid = true;

    // Check each required field
    requiredFields.forEach(field => {
        if (!field.value) {
            // If field is empty, add invalid class and prevent form submission
            field.classList.add('invalid');
            formIsValid = false;
        } else {
            // If field is filled, remove invalid class
            field.classList.remove('invalid');
        }
    });

    // Show an alert if the form is not valid
    if (!formIsValid) {
        event.preventDefault(); // Prevent form submission
        alert('This field is required. Please fill in all required fields.');
    }
});
