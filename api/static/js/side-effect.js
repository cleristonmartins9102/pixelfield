export class SideEffect {
  body
  constructor() {
    this.body = document.querySelector('body')
  }

  blackScreenOn() {
    const bScreen = document.createElement('div')
    bScreen.setAttribute('name', 'bscreen')
    bScreen.style.position = 'absolute'
    bScreen.style.height = '100%'
    bScreen.style.width = '100%'
    bScreen.style.background = 'rgba(0, 0, 0, 0.5)'
    bScreen.style.top = '0'
    this.body.style.position = 'relative'
    this.body.style.heigth = '100%'
    this.body.style.width = '100%'
    this.body.appendChild(bScreen)
  }

  blackScreenOff() {
    const dialogElement = document.querySelector('[dialog-name="borrow"]')
    const screen = document.querySelector('[name="bscreen"]')
    if (dialogElement) {
      dialogElement.remove()
    }
    screen.remove()
  }


  dialog (message, el=null, btnAction = { fn: null, label: null }) {
    const closeAction = () => {
      const dialogElement = document.querySelector('[dialog-name="borrow"]')
      const screen = document.querySelector('[name="bscreen"]')
      dialogElement.remove()
      screen.remove()
    }
    const screen = document.createElement('div')
    const wrapContent = document.createElement('div')
    const buttonClose = document.createElement('button')
    buttonClose.innerText = btnAction.label ?? 'Close'
    buttonClose.classList.add('btn')
    buttonClose.classList.add('btn_geen')
    screen.style.position = 'absolute'
    // screen.style.height = '200px'
    screen.style.width = '300px'
    screen.style.background = '#fff'
    screen.style.top = '50%';
    screen.style.left = '50%';
    screen.style.transform = 'translate(-50%, -50%)';
    screen.style.borderRadius = '4px';
    screen.style.padding = '20px';
    screen.style.display = 'flex';
    screen.style.flexDirection = 'column';
    screen.style.justifyContent = 'space-between';
    wrapContent.style.width = '100%';
    wrapContent.style.height = '100%';
    wrapContent.style.display = 'flex';
    wrapContent.style.alignItems = 'center';
    wrapContent.style.justifyContent = 'center';
    screen.style.boxShadow = 'rgba(0, 0, 0, 0.24) 0px 3px 8px';
    screen.setAttribute('dialog-name', 'borrow')
    const text = document.createElement('p')
    text.style.width = '100%'
    text.style.textAlign = 'center'
    text.style.fontSize = '22px'
    text.textContent = message
    wrapContent.appendChild(el ?? text)
    screen.appendChild(wrapContent)
    screen.appendChild(buttonClose)
    this.body.appendChild(screen)
    buttonClose.onclick = btnAction.fn ?? closeAction
  }
}