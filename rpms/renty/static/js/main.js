(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top');
        } else {
            $('.nav-bar').removeClass('sticky-top');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });
    
})(jQuery);

// form.js //
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".containerform");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

// login.js //
let loginname; // Declare loginname outside the function
let signin = document.querySelector("#signin");

// add Event
// signin.addEventListener("submit", function (event) {
//     event.preventDefault();
//     loginname = login(); // Assign the value returned by the login function to loginname
//     let userinfo = JSON.parse(localStorage.getItem(loginname));
//     if (loginname) {
//         // Redirect to welcome.html with the username as a query parameter
//         setTimeout(() => {
//             location.href = 'welcome.html?username=' + encodeURIComponent(userinfo.flname);
//         }, 2000);
//     }
// });

function login() {
    let emailInput = document.querySelector("#emailname");
    let passInput = document.querySelector("#passname");

    let loginname = emailInput.value.trim().toLowerCase();
    let loginpass = passInput.value;

    if (loginname === "" && loginpass === "") {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Please fill input fields'
        });
        return null; // Return null when the fields are not filled
    } else {
        // let userinfo = JSON.parse(localStorage.getItem(loginname));
        // if (userinfo !== null) {
            if (loginname == userinfo['emailname'] && loginpass == userinfo['passwordname']) {
                Swal.fire({
                    icon: 'success',
                    title: 'Good Job',
                    text: 'login sucessfullly',

                })
                return loginname;   
            }
            else {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Password does not match',

                })

            }
            return null;
        // }
        // else {
        //     Swal.fire({
        //         icon: 'error',
        //         title: 'Oops...',
        //         text: 'Account does not exist',

        //     })
        //     return null;
        // }
    }
}

// signup.js //
// let formfield = document.querySelector("#signup")

//add Event to the form field
// formfield.addEventListener("submit", function (event) {
//     event.preventDefault();
//     signup();
// })
let fullname = document.querySelector("#fname")
let mailname = document.querySelector("#ename")
let pass = document.querySelector("#pass")
let cpass = document.querySelector("#confirmpass")

function signup() {
    let fullnameValue = fullname.value.trim()
    let mailnameValue = mailname.value.trim().toLowerCase()
    let passValue = pass.value.trim()
    let cpassValue = cpass.value.trim()
    let letters = /^[a-zA-Z\s']+$/;
    let passmatch = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    let mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

    let userdetail = {
        "flname": fullnameValue,
        "emailname": mailnameValue,
        "passwordname": passValue,
        "confirmpassword": cpassValue
    }
    // get the mail value 
    // const userinfo = JSON.parse(localStorage.getItem(mailnameValue));
    // if (userinfo !== null) {
    //     Swal.fire({
    //         icon: 'error',
    //         title: 'Oops...',
    //         text: 'Account already exist'

    //     })
    // }
    // else {
        // condition 
        if (fullnameValue == "" && mailnameValue == "" && passValue == "" && cpassValue == "") {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Please fill input fields'

            })
            return false
        }
        else {
            
            if (!fullnameValue.match(letters) || fullnameValue.length < 3 ){

                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Username should be letters and min 3 characters'

                })
                return false
                
            }
            if (!mailnameValue.match(mailformat)) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Email is not valid',

                })
                return false
            }
            if (!passValue.match(passmatch)) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Your password needs to be between 8 and 15 characters long and contain one uppercase letter, one symbol, and a number.',

                })
                return false
            }
            if (passValue !== cpassValue) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Password does not match',

                })
                return false
            }
            // else {

            //     setTimeout(() => {
            //         Swal.fire({
            //             icon: 'success',
            //             title: 'Good Job',
            //             text: 'Sign up sucessfullly',

            //         })
            //     }, 2000)
                return true

                
            // }
        }
        //set value in local storage
        // localStorage.setItem(mailnameValue, JSON.stringify(userdetail));
    // }

}

// password eye icon
let passf = document.querySelectorAll(".pass1")
let btn = document.querySelectorAll("span i");
for (let i = 0; i < passf.length; i++) {
    btn[i].onclick = function () {
        if (passf[i].type == "password") {
            passf[i].type = "text";
            btn[i].classList.add("hide-btn")
        }
        else {
            passf[i].type = "password";
            btn[i].classList.remove("hide-btn")

        }
    }
}

//focus password eye icon
let passfield = document.querySelectorAll(".passfield")
let show = document.querySelectorAll(".passfield span")
for (let i = 0; i < passfield.length; i++) {
    passfield[i].addEventListener("focusin", function () {
        show[i].style.display = "block";
    })
}









// let profileDropdownList = document.querySelector(".profile-dropdown-list");
// let btn3 = document.querySelector(".profile-dropdown-btn");

// let classList = profileDropdownList.classList;

// const toggle = () => classList.toggle("active");

// window.addEventListener("click", function (e) {
//     if (!btn3.contains(e.target)) classList.remove("active");
// });







