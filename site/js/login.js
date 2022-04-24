document.documentElement.classList.remove("no-js");

if (document.cookie.indexOf("CrewCentreSession=Valid") == -1) {
  location.href = "/site/login.html";
}

var auth2;

gapi.load("auth2", function(){
    auth2 = gapi.auth2.init({
        client_id: "400237668286-4l755cng626bfg4pp3qcf3d2hh0ffg36.apps.googleusercontent.com"
    });
    auth2.attachClickHandler("signin-button", {}, onSuccess, onFailure);

    auth2.isSignedIn.listen(signinChanged);
    auth2.currentUser.listen(userChanged); // This is what you use to listen for user changes
});  

var signinChanged = function (val) {
    console.log("Signin state changed to ", val);
};

var onSuccess = function(user) {
    console.log("Signed in as " + user.getBasicProfile().getName());

    // redirect to login page if not signed in
    var sessionTimeout = 1; //hours
    var loginDuration = new Date();
    loginDuration.setTime(loginDuration.getTime()+(sessionTimeout*60*60*1000));
    document.cookie = "CrewCentreSession=Valid; "+loginDuration.toGMTString()+"; path=/site/";
    
    if (user.getBasicProfile().getName() == "FRHS SNHS") {
      location.replace(location.href.split("/login.html")[0] + "/home.html");
    } else {
      console.log("Wrong Google Address for Sign In");
    }

    // var current = location.href;
    // var base = current.split("/login.html")[0];
    // location.replace(base + "/home.html");
    // Redirect somewhere
};

var onFailure = function(error) {
    console.log(error);
};

function signOut() {
    auth2.signOut().then(function () {
        console.log("User signed out.");
    });
}        

var userChanged = function (user) {
    if(user.getId()){
      // Do something here
    }
};