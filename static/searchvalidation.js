function validateForm(event) {
  event.preventDefault(); //prevent form auto submission before validation
 
  // __________form data ___________

  const search = document.getElementById("search").value;
  
  // ___________error messages __________
  
  const searchError = document.getElementById("search-error");
  
// ______________intialize error messages _______________
  
  searchError.textContent = "";
  
// ______________conditions_________________
  let isValid = true;
  const specialChars = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~\d]/;

  if (search.trim() === "" || specialChars.test(search)) {
      searchError.textContent = "Please enter a valid search text";
      isValid = false;
  }

  if (isValid) {
    document.getElementById("form").submit();  
  }
}

// _______submit button __________
const form = document.getElementById("form");  
form.addEventListener("submit", validateForm);


