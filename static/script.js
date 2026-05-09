function validateForm() {
    let inputs = document.querySelectorAll("input");

    for (let i = 0; i < inputs.length; i++) {
        let value = inputs[i].value;

        if (value === "") {
            alert("All fields are required!");
            return false;
        }

        if (value < 0) {
            alert("Values cannot be negative!");
            return false;
        }
    }
    return true;
}

window.onload = function () {
    let risk = document.getElementById("risk");

    if (risk) {
        let text = risk.innerText.toLowerCase();

        if (text.includes("low")) risk.classList.add("low");
        else if (text.includes("medium")) risk.classList.add("medium");
        else if (text.includes("high")) risk.classList.add("high");
    }
};