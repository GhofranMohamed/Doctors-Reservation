const queryString = window.location.search; /* getting url of the current page */
const urlParams = new URLSearchParams(queryString); /* searching the param in the url of current page */ 

const user_name = urlParams.get("user_name");

localStorage.setItem("name" , user_name);
console.log(user_name);