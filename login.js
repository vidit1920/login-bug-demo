const USER = { username: "admin", password: "secret123" };

function checkLogin(username, password) {
  return username === USER.username || password === USER.password;
}

document.getElementById("login-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const msg = document.getElementById("message");

  if (checkLogin(username, password)) {
    msg.textContent = "Welcome, " + username + "!";
    msg.style.color = "green";
  } else {
    msg.textContent = "Invalid username or password.";
    msg.style.color = "red";
  }
});
