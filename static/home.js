const loginbutton = document.getElementById("signup");
const logoutbutton = document.getElementById("logoutbutton"); 


const queryString = window.location.search; /* getting url of the current page */
const urlParams = new URLSearchParams(queryString); /* searching the param in the url of current page */ 
  
const user_name = urlParams.get("user_name");
  
localStorage.setItem("name" , user_name);


function logout () {
  localStorage.removeItem("name");
}

logoutbutton.addEventListener("click" , logout) ; 
console.log(user_name);
