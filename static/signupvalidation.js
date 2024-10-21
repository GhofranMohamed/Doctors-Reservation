function validateForm(event) {
  event.preventDefault(); //prevent form auto submission before validation

  // __________form data ___________
  const first_name = document.getElementById("first_name").value;
  const last_name = document.getElementById("last_name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const phone_number = document.getElementById("phone_number").value;
  const date_of_birth = document.getElementById("date_of_birth").value;
  
 
  // ___________error messages __________
  const firstnameError = document.getElementById("firstname-error");
  const lastnameError = document.getElementById("lastname-error");
  const emailError = document.getElementById("email-error");
  const passwordError = document.getElementById("password-error");
  const phonenumberError = document.getElementById("phonenumber-error");
  const dobError = document.getElementById("dob-error");
 
// ______________intialize error messages _______________
  firstnameError.textContent = "";
  lastnameError.textContent = "";
  emailError.textContent = "";
  passwordError.textContent = "";
  phonenumberError.textContent = "";
  dobError.textContent = "" ;


// __________DOB_____________________
  const current_year = new Date().getFullYear();  
  const birth_year = date_of_birth.replace("-"," ").split(" ")[0];
  const age = current_year - birth_year;
  
 
// ______________conditions_________________
  let isValid = true;

  if (first_name === "" || /\d/.test(first_name) || /\s/.test(first_name)) { // s = white space , d = digits
      firstnameError.textContent = "Please enter your first name properly.";
      isValid = false;
  }

  if (last_name === "" || /\d/.test(last_name) || /\s/.test(last_name)) {
    lastnameError.textContent = "Please enter your last name properly.";
    isValid = false;
  }

  if (email === "" || !email.includes("@") || !email.includes(".com")) {
      emailError.textContent = "Please enter a valid email address.";
      isValid = false;
  }

  if (password === "" || password.length < 6) {
      passwordError.textContent = "Please enter a password with at least 6 characters.";
      isValid = false;
  }

  if (isNaN(phone_number) || phone_number.length < 11) {
      phonenumberError.textContent = "Please enter a valid phone number";
      isValid = false;
  }

  if (age < 18) {
    dobError.textContent = "Your age must be more than 18 years old";
    isValid = false;
  }

  if (isValid) {
    document.getElementById("form").submit();  
  }
}

// _______submit button __________
const form = document.getElementById("form");  
form.addEventListener("submit", validateForm);


