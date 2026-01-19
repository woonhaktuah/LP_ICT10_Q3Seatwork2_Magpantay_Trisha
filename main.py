from js import document
from pyodide.ffi import create_proxy

def assign_team(event=None):
    reg = document.querySelector('input[name="reg"]:checked')
    med = document.querySelector('input[name="med"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value.lower()
    output = document.getElementById("output")

    if reg is None or med is None:
        output.innerHTML = "Please answer all questions."
        return
        
    if reg.value == "yes" and med.value == "yes":

        if section == "ruby":
            team = "Yellow Tigers 🐯"
        elif section == "sapphire":
            team = "Green Hornets 🐝"
        elif section == "emerald":
            team = "Red Bulldogs 🐶"
        else:
            team = "Blue Bears 🐻"

        output.innerHTML = (
            "Congratulations for completing your registration! <br>"
            f"You are part of {team}"
        )   

    else:
        output.innerHTML = (
            "Registration incomplete."
            "<br>"
            "Kindly register online or secure medical clearance from the clinic."
        )

button = document.getElementById("signup")
button.addEventListener("click", create_proxy(assign_team))