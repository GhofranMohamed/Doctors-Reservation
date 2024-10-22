//___________**handeling logout**________________
  const isLoggedOut = localStorage.getItem("is_logged_out")
  const userName = localStorage.getItem("name") ;

  if (!isLoggedOut && userName != null) {
  const queryString = window.location.search; /* getting url of the current page */
  const urlParams = new URLSearchParams(queryString); /* searching the param in the url of current page */ 
    
  const user_name = urlParams.get("user_name");
  
  localStorage.setItem("name" , user_name);
  } else {
    localStorage.removeItem("is_logged_out")
    window.location = "http://"+ window.location.host;
  }

function logout () {
  localStorage.removeItem("name");
  localStorage.setItem("is_logged_out" , true) ;
}

logoutbutton.addEventListener("click" , logout) ; 




//_________** search validation ** _____________

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







