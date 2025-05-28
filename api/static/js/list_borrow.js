const currentUser = localStorage.getItem('currentUser')
const isAuthenticated = currentUser
let token = null
if (isAuthenticated) {
  token = JSON.parse(currentUser).access
}

const returnBook = (book_id) => {
  axios
  .request({ method: 'POST', url: '/api/loan/delete_loan/', data: { book_id },  headers: { 'content-type': 'application/json', Authorization: `Bearer ${token}` } })
  .then(response => {
    if (response.status === 204) {
      window.location.href = '/borrow'
    }
  })
  .catch(error => console.log(error))
}
axios
  .request({ method: 'GET', url: '/api/loan/', headers: { 'content-type': 'application/json', Authorization: `Bearer ${token}` } })
  .then(response => {
    if (response.status === 200) {
      const borrows = response.data

      borrows.forEach(book => {
        const row = document.createElement('tr')
        row.setAttribute('data-borrow-id', book.id)
        const btnReturn = document.createElement('div')
        btnReturn.classList.add('btn')
        btnReturn.classList.add('btn_geen')
        btnReturn.innerText = 'Return'
        const title = document.createElement('td')
        title.innerHTML = book.book_detail.title
        const author = document.createElement('td')
        author.innerHTML = book.book_detail.author
        const isbn = document.createElement('td')
        isbn.innerHTML = book.book_detail.ISBN
        const page_count = document.createElement('td')
        page_count.innerHTML = book.book_detail.page_count
        const btnReturnTD = document.createElement('td')
        btnReturnTD.appendChild(btnReturn)
        row.prepend(btnReturnTD)
        row.prepend(title)
        row.prepend(author)
        row.prepend(isbn)
        row.prepend(page_count)
        document.querySelector('.table_row').prepend(row)
        btnReturnTD.onclick = () => returnBook(book.book_detail.id)
      })
    }
  })
  .catch(error => {
    console.log(error)
  }) 