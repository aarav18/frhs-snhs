document.documentElement.classList.remove("no-js");

function decodeJwtResponse(token) {
  var base64Url = token.split('.')[1];
  var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));

  return JSON.parse(jsonPayload);
};

function handleCredentialResponse(response) {
  console.log("Encoded JWT ID token: " + response.credential);
  const responsePayload = decodeJwtResponse(response.credential);

  console.log("ID: " + responsePayload.sub);
  console.log('Full Name: ' + responsePayload.name);
  console.log('Given Name: ' + responsePayload.given_name);
  console.log('Family Name: ' + responsePayload.family_name);
  console.log("Image URL: " + responsePayload.picture);
  console.log("Email: " + responsePayload.email);

  // redirect
  var sessionTimeout = 1; //hours
  var loginDuration = new Date();
  loginDuration.setTime(loginDuration.getTime()+(sessionTimeout*60*60*1000));
  document.cookie = "CrewCentreSession=Valid; "+loginDuration.toGMTString()+"; path=/";

  window.location.href = "https://aarav18-snhs.netlify.app/home.html";
}

if (window.location.href == "https://aarav18-snhs.netlify.app/login.html") {
  window.onload = function () {
    google.accounts.id.initialize({
      client_id: "400237668286-4l755cng626bfg4pp3qcf3d2hh0ffg36.apps.googleusercontent.com",
      callback: handleCredentialResponse
    });
    google.accounts.id.renderButton(
      document.getElementById("google-signin"),
      { theme: "outline", 
        size: "large"
      }  // customization attributes
    );
  }
  // google.accounts.id.prompt(); // also display the One Tap dialog
}