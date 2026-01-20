from pyscript import display, document # type: ignore

def sign_up(e):
    document.getElementById('output').innerHTML = ' '
    
    regitration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value