const btnLogin = document.querySelector('.btn_login')
const currentUser = localStorage.getItem('currentUser')
const isAuthenticated = currentUser

let token = null

if (isAuthenticated) {
  token = JSON.parse(currentUser).access
}

if (!isAuthenticated) {
  btnLogin.innerHTML = 'Login'
} else {
  btnLogin.innerHTML = 'Logout'
}

const btnUsers = document.querySelector('[name="users"]')
const btnBooks = document.querySelector('[name="books"]')
btnUsers.addEventListener('click', () => {
  window.location.href = '/admin/users'
})

btnBooks.addEventListener('click', () => {
  window.location.href = '/admin/books'
})
