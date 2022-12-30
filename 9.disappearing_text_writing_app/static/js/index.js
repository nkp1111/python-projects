const text = document.querySelector("textarea")
const body = document.querySelector("body")
let currentSeconds
let colors = ["#1A120B", "3C2A21", "#E1D7C6", "#ECE8DD", "#F8F4EA"]
let count = 0

text.addEventListener("input", (e) => {
  currentSeconds = new Date().getSeconds()
  count = 0
  text.style.color = "#000"
})

const checkStop = () => {
  const latestSeconds = new Date().getSeconds()

  if (count == 5) {
    clearInterval(interval)
    currentSeconds = null
    text.value = ""
    text.style.color = "#000"
    count = 0
    interval = setInterval(checkStop, 1000)
  }
  if (Math.abs(latestSeconds - currentSeconds) > 5) {
    text.style.color = colors[count]
    count += 1
  }
}

let interval = setInterval(checkStop, 1000)
