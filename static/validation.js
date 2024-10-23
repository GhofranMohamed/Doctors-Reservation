//______________**validation**________________
function validateForm(event) {
  event.preventDefault(); //prevent form auto submission before validation
 
  // __________form data ___________

  const phone_number = document.getElementById("phone_number").value;
  
  // ___________error messages __________
  
  const phonenumberError = document.getElementById("phonenumber-error");
  
// ______________intialize error messages _______________
  
  phonenumberError.textContent = "";
  
// ______________conditions_________________
  let isValid = true;

  if (isNaN(phone_number) || phone_number.length < 11) {
    phonenumberError.textContent = "Please enter a valid phone number";
    isValid = false;
  }

  if (isValid) {
    document.getElementById("form").submit();  
  }
}

// _______submit button __________
const form = document.getElementById("form");  
form.addEventListener("submit", validateForm);



