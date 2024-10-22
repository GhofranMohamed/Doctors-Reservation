

const isLoggedOut = localStorage.getItem("is_logged_out")

if (!isLoggedOut ) {
 
  const home_link = document.getElementById("home_link");
  const user_name = localStorage.getItem("name");
  
  let baseurl = home_link.getAttribute("href")
  home_link.setAttribute("href" , baseurl + "?user_name=" + encodeURIComponent(user_name));
  
} else {
  localStorage.removeItem("is_logged_out") ;
  window.location = "http://"+ window.location.host ;
}

function logout () {
localStorage.removeItem("name");
localStorage.setItem("is_logged_out" , true) ;
}

logoutbutton.addEventListener("click" , logout) ; 












