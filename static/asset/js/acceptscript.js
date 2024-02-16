function submitForm() {
    const acceptCheckbox = document.getElementById('acceptCheckbox');

    if (acceptCheckbox.checked) {
        // Perform any additional actions upon acceptance (e.g., form submission)
        alert('Terms accepted! Form submitted.');
    } else {
        alert('Please accept the Terms of Use before submitting.');
    }
}
