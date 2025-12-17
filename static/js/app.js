// static/js/app.js
// Common JavaScript functions

// Example: Handle logout
function logout() {
    fetch('/logout', { method: 'POST' })
        .then(() => window.location.href = '/login');
}

// Add event listeners if needed
document.addEventListener('DOMContentLoaded', () => {
    // Any init code
});