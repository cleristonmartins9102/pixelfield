const btn_sign = document.querySelector('#btn_sign')
const error_element = document.querySelector('#error')
btn_sign.addEventListener('click', (e) => {
  e.preventDefault()
  const form = { 
    username: document.querySelector('#username').value,
    password: document.querySelector('#password').value
  }
  axios
      .request({ method: 'POST', url: '/api/login/', data: form }, { Headers: { 'content-type': 'application/json'}})
    .then(response => {
      error_element.innerHTML = null
      localStorage.setItem('currentUser', JSON.stringify(response.data))
      if (response.data.role === 'admin') {
        window.location.href = '/admin/'
      } else {
        window.location.href = document.referrer ?? '/books/'
      }
    })
    .catch(error => {
      console.log(error)
      error_element.innerHTML = error.response.data.detail
    }) 
})

