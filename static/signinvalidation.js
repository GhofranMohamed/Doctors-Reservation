const loginButton = document.getElementById("login");

if (loginButton) {

  loginButton.addEventListener("click" , () => localStorage.removeItem("is_logged_out"))
}

function validateForm(event) {
  event.preventDefault(); //prevent form auto submission before validation

  // __________form data ___________

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  
  // ___________error messages __________
  
  const emailError = document.getElementById("email-error");
  const passwordError = document.getElementById("password-error");
 
 
// ______________intialize error messages _______________
  
  emailError.textContent = "";
  passwordError.textContent = "";
  
 
// ______________conditions_________________
  let isValid = true;

  if (email === "" || !email.includes("@") || !email.includes(".com")) {
      emailError.textContent = "Please enter a valid email address.";
      isValid = false;
  }

  if (password === "" ) {
    passwordError.textContent = "Your password can't be null";
    isValid = false;
  }


  if (isValid) {
    document.getElementById("form").submit();  
  }
}

// _______submit button __________
const form = document.getElementById("form");  
form.addEventListener("submit", validateForm);


