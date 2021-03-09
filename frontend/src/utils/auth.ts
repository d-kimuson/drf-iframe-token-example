export const appOrigin = "http://127.0.0.1:3000"
export const authOrigin = "http://127.0.0.1:8000"

export const autoLogin = (callback: (token: string) => void): void => {
  const iframe = window.document.createElement("iframe")
  iframe.style.display = "none"

  const receiver = (event: MessageEvent<string>) => {
    if (event.origin !== authOrigin) return

    const token = event.data
    window.document.body.removeChild(iframe)
    window.removeEventListener("message", receiver, false)

    callback(token)
  }

  window.addEventListener("message", receiver, false)
  window.document.body.appendChild(iframe)
  iframe.setAttribute("src", `${authOrigin}/autologin`)
}
