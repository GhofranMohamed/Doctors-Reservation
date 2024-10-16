/*____________getting elememnts from html _____________*/

const signin = document.getElementById("signin"); 
const signup = document.getElementById("signup") ;
const inform = document.getElementById("signinform");
const upform = document.getElementById("signupform");
const content = document.getElementById("content") ;

/*__________functions_______*/
function singinform() { 
  inform.style.display = inform.style.display === 'none' ? 'block' : 'none';
  content.style.display = content.style.display === 'none' ? 'block' : 'none';
}

function signupform() {
  upform.style.display = upform.style.display === 'none' ? 'block' : 'none';
  content.style.display = content.style.display === 'none' ? 'block' : 'none';
}


/*_________event listners_________*/
signin.addEventListener("click", singinform);
signup.addEventListener("click" , signupform);

