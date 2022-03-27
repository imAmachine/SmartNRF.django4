window.addEventListener('resize', function() {
    mobileLayout()
});

let mobileLayout = () => {
    if (window.innerWidth <= 767) {
        document.getElementsByClassName('burger')[0].classList.add('burger-active')
        document.getElementsByClassName('form-select')[0].classList.remove('hidden')
    }
    else {
        document.getElementsByClassName('burger')[0].classList.remove('burger-active')
        document.getElementsByClassName('form-select')[0].classList.add('hidden')
        document.getElementsByClassName('list-group')[0].classList.add('hidden')
    }
}
    
let openMobileMenu = () => {
    document.getElementsByClassName('list-group')[0].classList.toggle('hidden')
}