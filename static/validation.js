function validateForm(event) {
  event.preventDefault();

  // __________form data ___________
  const first_name = document.getElementById("first_name").value;
  const last_name = document.getElementById("last_name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const phone_number = document.getElementById("phone_number").value;
  
 
  // ___________error messages __________
  const firstnameError = document.getElementById("firstname-error");
  const lastnameError = document.getElementById("lastname-error");
  const emailError = document.getElementById("email-error");
  const passwordError = document.getElementById("password-error");
  const phonenumberError = document.getElementById("phonenumber-error");
 
// ______________define error messages _______________
  firstnameError.textContent = "";
  lastnameError.textContent = "";
  emailError.textContent = "";
  passwordError.textContent = "";
  phonenumberError.textContent = "";
 
// ______________conditions_________________
  let isValid = true;

  if (first_name === "" || /\d/.test(first_name)) {
      firstnameError.textContent = "Please enter your name properly.";
      isValid = false;
  }

  if (last_name === "" || /\d/.test(last_name)) {
    lastnameError.textContent = "Please enter your name properly.";
    isValid = false;
  }

  if (email === "" || !email.includes("@")) {
      emailError.textContent = "Please enter a valid email address.";
      isValid = false;
  }

  if (password === "" || password.length < 6) {
      passwordError.textContent = "Please enter a password with at least 6 characters.";
      isValid = false;
  }

  if (isNaN(phone_number)) {
      phonenumberError.textContent = "Please enter a valid phone number";
      isValid = false;
  }

  if (isValid) {
    document.getElementById("form").submit();  // Assuming your form has an id="myForm"
  }
}

// _______submit button __________
const form = document.getElementById("form");  // Ensure your form has an id
form.addEventListener("submit", validateForm);

console.log(document.getElementById("first_name"));

console.log("hi") ;
