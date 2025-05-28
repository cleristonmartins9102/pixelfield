import { SideEffect } from "./side-effect.js"
const allCheck = document.querySelectorAll('[name="checkBook"]')
const btnLogin = document.querySelector('.btn_login')
let deletList = []
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

const sideEffect = new SideEffect()

document.addEventListener('keyup', (k) => {
  if (k.key === 'Escape') {
    sideEffect.blackScreenOff()
  }
})

btnLogin.addEventListener('click', (e) => 
  {
  if (btnLogin.innerHTML.toLowerCase().trim() === 'login') {
    window.location.href = '/login'
  } else {
    localStorage.removeItem('currentUser')
    window.location.href = '/books/'
  }
})

allCheck.forEach(el => {
  el.addEventListener('click', function (e) {
    const book_id = this.getAttribute('data-book-id')
    if (e.target.checked) {
      deletList.push(book_id)
    } else {
      deletList = deletList.filter(id => id !== book_id)
    }
  })
})

const btnDelete = document.querySelector('[name="btn_delete"]')
btnDelete.addEventListener('click', () => {
  let success = false
  for (const book of deletList) {
    axios
      .request({ method: 'DELETE', url: `/api/books/${book}/`, headers: { 'content-type': 'application/json', Authorization: `Bearer ${token}` } })
      .then(response => {
        if (response.status === 204) {
          console.log('hrre')
          success = true
        }
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
  }
  if (success) {
    window.location.href = '/admin'
  }
})

const btnAdd = document.querySelector('[name="btn_add"]')
btnAdd.addEventListener('click', () => {
  const headerTitle = document.createElement('p')
  headerTitle.innerText = 'Add Book'
  const title = document.createElement('input')
  title.placeholder = 'title'
  const author = document.createElement('input')
  author.placeholder = 'author'
  const isbn = document.createElement('input')
  isbn.placeholder = 'isbn'
  const page = document.createElement('input')
  page.placeholder = 'page'
  const wrap = document.createElement('div')
  wrap.style.width = '100%'
  const allInput = [title, author, isbn, page]
  for (const input of allInput) {
    input.style.width = '100%'
    input.style.width = '260px';
    input.style.borderRadius = '4px';
    input.style.padding = '6px';
    input.style.border = '1px solid rgb(0, 128, 0)';
    input.style.color = '#333';
    input.style.outline = 'none';
  }
  wrap.append(headerTitle, title, author, isbn, page)
  wrap.style.display = 'flex'
  wrap.style.flexDirection = 'column'
  wrap.style.gap = '10px'
  wrap.style.padding = '10px 0 10px 0'


  sideEffect.blackScreenOn()
  sideEffect.dialog('', wrap, { 
    fn: () => {
       const form = allInput.reduce((prev, curr) => ({...prev, [curr.getAttribute('placeholder')]: curr.value }), {})
       const { isbn, page, ...rest } = form
       axios
        .request({ method: 'POST', url: `/api/books/`, data: { ...rest, ISBN: isbn, page_count: page }, headers: { 'content-type': 'application/json', Authorization: `Bearer ${token}` } })
        .then(response => {
          if (response.status === 201) {
            window.location.href = '/admin/books'
          }
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    }, 
    label: 'Create' }
  )
})

const btnUsers = document.querySelector('[name="users"]')
console.log(btnUsers)
