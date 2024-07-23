let username = document.getElementById('uname');
let password = document.getElementById('password');


function validate() {
    if(username.value.trim()===""){
         alert("Please enter username")
         username.focus()
         return false;
    }else if(password.value.trim()===""){
        alert("Please enter password")
        password.focus()
        return false;
    }if(password.value.length <8){
        alert("Please enter a valid password (minimum password length = 8)")
        password.focus()
        return false;
    }else{
        return true
    }
}

document.querySelector("#submit")
.addEventListener("click",(event)=>{
    event.preventDefault();
    validate();
});