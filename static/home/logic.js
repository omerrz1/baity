const menu = document.getElementsByClassName('menu')[0]
const buttons = document.getElementsByClassName('buttons')[0]
menu.addEventListener('click',(c)=>{
    buttons.classList.toggle('active')
    menu.classList.toggle('active')
    })