
/*Register and Login Form input box animation*/


const wrapper=document.querySelector('.wrapper');
const loginLink=document.querySelector('.login-link');
const registerLink=document.querySelector('.register-link');

registerLink.addEventListener('click',()=>{
    wrapper.classList.add('active');
});
 
loginLink.addEventListener('click',()=>{
    wrapper.classList.remove('active');
});


/* altert for successful registration */

function register(){
    alert("You have registered succesfully.");
    wrapper.classList.remove('active');
}




