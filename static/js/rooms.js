Section = document.querySelector('section');
async function filter(){
  const selected = document.querySelector("select").value
  console.log(selected)
  const url = new URL(document.baseURI)
  url.searchParams.append("purpose", selected)
  console.log(url)
  const response = await fetch(url)
  const json = await response.json()
  console.log(typeof(json))
  for (room in await json) {
    let article = document.createElement("article")
    article.appendChild(document.createElement("h3"))
    article.firstElementChild.textContent = `Room name: ${json[room].room_name}`
    article.appendChild(document.createElement("p"))
    article.lastElementChild.textContent = `Room capacity: ${json[room].room_capacity}`
    article.appendChild(document.createElement("p"))
    article.lastElementChild.textContent = `Descripton: ${json[room].room_description}`
    article.appendChild(document.createElement('p'))
    article.lastElementChild.textContent = 'payable: True'
    article.appendChild(document.createElement('button'))
    article.lastElementChild.id = json[room].id
    article.lastElementChild.textContent = "Book"
    Section.appendChild(article)
  }
  book()
}

document.querySelector('#select-btn').addEventListener('click', filter)
