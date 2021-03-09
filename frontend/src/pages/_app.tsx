import { useState, useEffect } from "react"
import type { AppProps } from "next/app"
import { Provider } from "react-redux"

import "~/styles/globals/index.scss"
import { store } from "~/store"
import { autoLogin } from "~/utils/auth"

const MyApp: React.VFC<AppProps> = ({ Component, pageProps }: AppProps) => {
  const [token, setToken] = useState<string | undefined>(undefined)

  useEffect(() => {
    if (typeof window !== "undefined") {
      autoLogin((receivedToken) => setToken(receivedToken))
    }
  }, [])

  return (
    <Provider store={store}>
      <div id="auth">
        <p>
          {typeof token !== "undefined"
            ? "ログイン済み"
            : "ログインしてください"}
        </p>
        <p>トークン: {token}</p>
      </div>
      <Component {...pageProps} />
    </Provider>
  )
}

export default MyApp
