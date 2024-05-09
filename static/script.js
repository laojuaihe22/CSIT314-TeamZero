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

function userLogin() {
    var email = document.getElementById("email").value;
    var localEmail = localStorage.getItem("email");
    var password = document.getElementById("password").value;
    var localPassword = localStorage.getItem("password");
    var errorDiv = document.getElementById("infoMisMatch");
    
    if (email !== localEmail && password !== localPassword) {
        errorDiv.innerText = "Wrong Password or Email, Please try again!";
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

function showUserAccount() {
    var adminContent = document.getElementById("adminContent");
    var userAccountContent = `
        <div class="user-account-option">
            <div class="user-account-title">
                <u><p>User Account Options:</p></u>
            </div>
            <div class="user-account-buttons">
                <button onclick="location.href='/createUserAccount'">Create User Account</button>
                <button onclick="location.href='adminView.html'">View User Account</button>
                <button onclick="location.href='adminUpdate.html'">Update User Account</button>
                <button onclick="location.href='adminDelete.html'">Delete User Account</button>
                <button onclick="location.href='adminSearch.html'">Search User Account</button>
            </div>
        </div>
    `;

    if (adminContent.innerHTML === userAccountContent) {
        adminContent.innerHTML = `
            <p>ZeroRealEstate</p>
            <p>Admin</p>
        `;
    } else {
        adminContent.innerHTML = userAccountContent;
    }
}

function highlightLink(link) {
    var isSelected = link.classList.contains('selected');

    var links = document.getElementsByClassName('sidenav')[0].getElementsByTagName('a');
    for (var i = 0; i < links.length; i++) {
        links[i].classList.remove('selected');
    }

    if (!isSelected) {
        link.classList.add('selected');
    }
}

//jiro's js!!

//Ally's js!!!
