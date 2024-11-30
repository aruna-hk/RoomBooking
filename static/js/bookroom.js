async function book() {
  document.querySelector("article > button").addEventListener('click', async (event) => {
    let url = "http://localhost:8000/book/"
    const data = {"room": `${event.target.id}`}
    const headers = {"Content-Type": "Application/json"}
    const response = await fetch(url, { method: "POST", body: JSON.stringify(data), headers:headers})
    const text = await response.text()
    console.log(text)
  })
}
