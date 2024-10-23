//________return isloggedout key and user name from local storage______________
const isLoggedOut = localStorage.getItem("is_logged_out")
const user_name = localStorage.getItem("name");

if (!isLoggedOut) {
//___________display welcome back again if user is still logged in______-
  const home_link = document.getElementById("home_link");
  
  let baseurl = home_link.getAttribute("href")
  home_link.setAttribute("href" , baseurl + "?user_name=" + encodeURIComponent(user_name));
  
} else {
//________redirect to index page if user is logged out __________  
  localStorage.removeItem("is_logged_out") ;
  window.location = "http://"+ window.location.host ;
}

function logout () {
localStorage.removeItem("name");
localStorage.setItem("is_logged_out" , true) ;
}

logoutbutton.addEventListener("click" , logout) ; 












