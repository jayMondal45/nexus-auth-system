// Get all form sections
const loginSection = document.getElementById('login-section');
const registerSection = document.getElementById('register-section');
const forgotSection = document.getElementById('forgot-section');

// Get all toggle buttons
const showRegister = document.getElementById('show-register');
const showLogin = document.getElementById('show-login');
const showForgot = document.getElementById('show-forgot');
const backToLogin = document.getElementById('back-to-login');

// Get title elements
const formTitle = document.getElementById('form-title');
const formSubtitle = document.getElementById('form-subtitle');

// Get navigation dots
const navDots = document.querySelectorAll('.nav-dot');

// Password toggle functionality
const loginTogglePassword = document.getElementById('login-toggle-password');
const loginPassword = document.getElementById('login-password');

const regTogglePassword = document.getElementById('reg-toggle-password');
const regPassword = document.getElementById('reg-password');

const regConfirmTogglePassword = document.getElementById('reg-confirm-toggle-password');
const regConfirmPassword = document.getElementById('reg-confirm-password');

// Function to show a specific section
function showSection(section) {
    // Hide all sections
    loginSection.classList.remove('active');
    registerSection.classList.remove('active');
    forgotSection.classList.remove('active');

    // Show the requested section
    section.classList.add('active');

    // Update header text
    if (section === loginSection) {
        formTitle.textContent = 'Welcome Back';
        formSubtitle.textContent = 'Sign in to your account to continue';
    } else if (section === registerSection) {
        formTitle.textContent = 'Create Account';
        formSubtitle.textContent = 'Join our community today';
    } else if (section === forgotSection) {
        formTitle.textContent = 'Reset Password';
        formSubtitle.textContent = 'We\'ll help you get back into your account';
    }

    // Update navigation dots
    navDots.forEach(dot => {
        if (dot.getAttribute('data-target') === section.id) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

// Add event listeners
showRegister.addEventListener('click', () => showSection(registerSection));
showLogin.addEventListener('click', () => showSection(loginSection));
showForgot.addEventListener('click', () => showSection(forgotSection));
backToLogin.addEventListener('click', () => showSection(loginSection));

// Navigation dots event listeners
navDots.forEach(dot => {
    dot.addEventListener('click', () => {
        const targetId = dot.getAttribute('data-target');
        const targetSection = document.getElementById(targetId);
        showSection(targetSection);
    });
});

// Password toggle functionality
function togglePasswordVisibility(toggleBtn, passwordField) {
    toggleBtn.addEventListener('click', () => {
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        toggleBtn.classList.toggle('fa-eye');
        toggleBtn.classList.toggle('fa-eye-slash');
    });
}

togglePasswordVisibility(loginTogglePassword, loginPassword);
togglePasswordVisibility(regTogglePassword, regPassword);
togglePasswordVisibility(regConfirmTogglePassword, regConfirmPassword);

// Auto-hide flash messages after 5 seconds
setTimeout(() => {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        message.style.display = 'none';
    });
}, 5000);