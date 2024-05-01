function lsRememberMe() {
    var emailInput = document.getElementById("email");
    var rememberMeCheckbox = document.getElementById("rememberUser");
    
    if (rememberMeCheckbox.checked) {
        localStorage.setItem("email", emailInput.value);
        localStorage.setItem("rememberMe", true);
    } else {
        localStorage.removeItem("email");
        localStorage.setItem("rememberMe", false);
    }
}

document.addEventListener("DOMContentLoaded", function() {
    var emailInput = document.getElementById("email");
    var rememberMeCheckbox = document.getElementById("rememberUser");
    
    var storedRememberMe = localStorage.getItem("rememberMe");
    if (storedRememberMe === "true") {
        rememberMeCheckbox.checked = true;
        var storedEmail = localStorage.getItem("email");
        if (storedEmail) {
            emailInput.value = storedEmail;
        }
    }

    rememberMeCheckbox.addEventListener("change", function() {
        if (!this.checked) { 
            emailInput.value = ""; 
        }
        lsRememberMe(); 
    });

    lsRememberMe();
});

function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var toggleIcon = document.getElementById("toggleIcon");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.className = "ri-eye-off-line toggle-password-icon";
    } else {
        passwordInput.type = "password";
        toggleIcon.className = "ri-eye-line toggle-password-icon";
    }
}

function validatePasswords() {
    var password = document.getElementById("npassword").value;
    var password_re = document.getElementById("npassword_re").value;
    var errorDiv = document.getElementById("passwordMismatch");
    if (password !== password_re) {
        errorDiv.innerText = "Both password do not match.";
        errorDiv.classList.add("error");
        errorDiv.classList.remove("success");
        errorDiv.style.display = "block";
        return false;
    } else {
        errorDiv.innerText = "";
        errorDiv.classList.remove("error");
        errorDiv.classList.add("success");
        errorDiv.style.display = "block";
        return true;
    }

}

function validateNewUser() {
    var email = document.getElementById("nemail").value;
    var storedEmail = localStorage.getItem("email");
    var errorDiv = document.getElementById("exsistingEmail");
    
    if (email === storedEmail) {
        errorDiv.innerText = "Email has already been registered. Please sign in instead!";
        errorDiv.classList.add("error");
        errorDiv.classList.remove("success");
        errorDiv.style.display = "block"; 
        return false;
    }else{
        errorDiv.innerText = "";
        errorDiv.classList.remove("error");
        errorDiv.classList.add("success");
        errorDiv.style.display = "block";
        return true;
    }
}
