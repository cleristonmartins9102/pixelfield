import { SideEffect } from "./side-effect.js"

const allBtnBorrow = document.querySelectorAll('.btn_geen')
const btnLogin = document.querySelector('.btn_login')
const container = document.querySelector('.container')

const currentUser = localStorage.getItem('currentUser')
const isAuthenticated = currentUser
let token = null

const disableBtn = (btn) => {
    btn.classList.remove('btn_geen')
    btn.classList.add('btn_disabled')
}



const sideEffect = new SideEffect()

if (isAuthenticated) {
  token = JSON.parse(currentUser).access
}

if (!isAuthenticated) {
  allBtnBorrow.forEach(btn => {
    disableBtn(btn)
  })
} else {
  btnLogin.innerHTML = 'Logout'
}

btnLogin.addEventListener('click', (e) => 
  {
  if (btnLogin.innerHTML.toLowerCase().trim() === 'login') {
    window.location.href = '/login'
  } else {
    localStorage.removeItem('currentUser')
    window.location.href = '/books/'
  }
})

allBtnBorrow.forEach(btn => {
  btn.addEventListener('click', function () {
    const book = this.getAttribute('data-book-id')
     axios
      .request({ method: 'POST', url: '/api/loan/', data: { book }, headers: { 'content-type': 'application/json', Authorization: `Bearer ${token}`}})
      .then(response => {
        if (response.status === 201) {
          sideEffect.blackScreenOn()
          sideEffect.dialog('Borrow Success!')
          disableBtn(this)
        }
      })
      .catch(error => {
        console.log(error)
      }) 
  })
})

