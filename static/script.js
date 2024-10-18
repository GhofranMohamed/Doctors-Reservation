const home_link = document.getElementById("home_link");

const user_name = localStorage.getItem("name");


let baseurl = home_link.getAttribute("href")
home_link.setAttribute("href" , baseurl + "?user_name=" + encodeURIComponent(user_name));







