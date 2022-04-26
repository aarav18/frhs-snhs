function signOut() {

  console.log("Signing Out!");

  document.cookie = document.cookie.replace("CrewCentreSession=Valid", "");
  window.location.href = "https://aarav18-snhs.netlify.app/login.html";
}