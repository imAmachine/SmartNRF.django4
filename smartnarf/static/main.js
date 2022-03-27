let selectCart = (discipline, teacher) => {
    document.getElementById('idComment').innerHTML = `Домашняя работа ${discipline}`
    document.getElementById('idHomework').innerHTML = `Комментарий ${teacher}`
}

let prevScrollpos = window.pageYOffset;

window.onscroll = function() {
  let currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) document.getElementsByClassName('form-select')[0].classList.remove('form-select-hide')
  else document.getElementsByClassName('form-select')[0].classList.add('form-select-hide')
  prevScrollpos = currentScrollPos;
}