console.log('Hello world!')

const helloWorldBox = document.getElementById('hello-world')
const postBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')

// helloWorldBox.innerHTML = 'hello <b>world</b>'

$.ajax({
  type: 'GET',
  url: '/hello-world/',
  success: function (response) {
    // it will print the {'text': 'hello world'} which be difinded in the views.py
    console.log('success', response.text)
    helloWorldBox.textContent = response.text
  },
  error: function (error) {
    console.log('error', error)
  }
})

$.ajax({
  type: 'GET',
  url: '/data/',
  success: function (response) {
    console.log(response)
    const data = response.data
    setTimeout(() => {
      // .not-visible has been defined in the style.css
      spinnerBox.classList.add("not-visible")
      data.forEach(el => {
        postBox.innerHTML += `
          <div class="card mb-2">
            <div class="card-body">
              <h5 class="card-title">${el.title}</h5>
              <p class="card-text">${el.body}</p>
            </div>
            <div class="card-footer">
                <div class="row">
                  <div class="col-1">
                    <a href="#" class="btn btn-primary">Details</a>
                  </div>
                  <div class="col-1">
                    <a href="#" class="btn btn-primary">Like</a>
                  </div>
                </div>
              </div>
          </div>
        `
      })
    }, 1000)
  },
  error: function (error) {
    console.log(error)
  }
})