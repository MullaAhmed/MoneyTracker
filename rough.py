
var myHeaders = new Headers();
myHeaders.append("Authorization", "token 5d8b521d669124004d30326ba265befc651d78d3");

var formdata = new FormData();

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/groups/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));