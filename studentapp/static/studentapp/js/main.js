document.addEventListener("DOMContentLoaded", function () {

    const toast = document.getElementById("toast");

    function showToast(message) {
        toast.innerText = message;
        toast.style.display = "block";

        // hide after 2 seconds
        setTimeout(() => {
            toast.style.display = "none";
        }, 2000);
    }

    // 📱 PHONE VALIDATION
    const phoneInput = document.querySelector("input[name='phone']");

    if (phoneInput) {
        phoneInput.addEventListener("input", function () {
            const value = phoneInput.value;

            if (!/^\d*$/.test(value)) {
                showToast("Only numbers allowed in phone");
            }

            if (value.length > 0 && value.length !== 10) {
                showToast("Phone must be exactly 10 digits");
            }
        });
    }

    // 📧 EMAIL VALIDATION
    const emailInput = document.querySelector("input[name='email']");

    if (emailInput) {
        emailInput.addEventListener("input", function () {
            const value = emailInput.value;

            if (value.length > 0 && !(value.includes("@") && value.includes("."))) {
                showToast("Invalid email format");
            }
        });
    }

});