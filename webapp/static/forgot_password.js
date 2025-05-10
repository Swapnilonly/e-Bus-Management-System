document.getElementById("forgotPasswordForm").addEventListener("submit", function(event) {
  event.preventDefault();
  const emailInput = document.getElementById("emailInput");
  const feedbackMessage = document.getElementById("feedbackMessage");

  // Basic email validation
  if (!emailInput.value || !/\S+@\S+\.\S+/.test(emailInput.value)) {
      feedbackMessage.textContent = "Please enter a valid email address.";
      feedbackMessage.style.color = "red";
      return;
  }

  // Show loading state
  feedbackMessage.textContent = "Sending reset link...";
  feedbackMessage.style.color = "#333";
  emailInput.disabled = true;
  this.querySelector("button").disabled = true;

  // Simulate sending email (mockup)
  setTimeout(() => {
      feedbackMessage.textContent = "Reset link sent! Please check your email.";
      feedbackMessage.style.color = "green";
      emailInput.disabled = false;
      this.querySelector("button").disabled = false;
      this.reset();
  }, 2000);
});
