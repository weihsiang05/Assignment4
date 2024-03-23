console.log('Hello world!')

const helloWorldBox = document.getElementById('hello-world')

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