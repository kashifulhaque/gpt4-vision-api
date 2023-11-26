<p align="center">
  <a href="https://gpt4-vision-api.vercel.app">
    <img src="https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png" height="96">
    <h3 align="center">Next.js FastAPI OpenAI GPT-4 Vision API</h3>
  </a>
</p>

> Based off of [digitros' started code](https://github.com/digitros/nextjs-fastapi)

### **Bring your own OpenAI API key** 🔐
Get your own key [here](https://platform.openai.com)

### **Sample request** 📨
`curl` 👇️
```sh
curl  -X POST \
  'https://gpt4-vision-api.vercel.app/api/vision?question=What%20is%20the%20colour%20of%20the%20cat' \
  --header 'api-key: sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
  --form 'image=@/home/user/Pictures/cat.png'
```
`python requests` 👇️
```py
import requests

reqUrl = "https://gpt4-vision-api.vercel.app/api/vision?question=What%20is%20the%20colour%20of%20the%20cat"

post_files = { "image": open("/home/user/Pictures/cat.png", "rb") }
headersList = { "api-key": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" }

payload = ""

response = requests.request("POST", reqUrl, data=payload, files=post_files, headers=headersList)

print(response.text)
```
`node.js fetch` 👇️
```js
const fs = require('fs');
const FormData = require('form-data');
const fetch = require('node-fetch');
const formData = new FormData();

formData.append('image', fs.createReadStream('/home/user/Pictures/cat.png'));

let url = 'https://gpt4-vision-api.vercel.app/api/vision?question=What%20is%20the%20colour%20of%20the%20cat%3F';

let options = {
  method: 'POST',
  headers: {
    'api-key': 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'content-type': 'multipart/form-data; boundary=---011000010111000001101001'
  }
};

options.body = formData;

fetch(url, options)
  .then(res => res.json())
  .then(json => console.log(json))
  .catch(err => console.error('error:' + err));
```
`node.js axios` 👇️
```js
var axios = require("axios").default;

var options = {
  method: 'POST',
  url: 'https://gpt4-vision-api.vercel.app/api/vision',
  params: {question: 'What is the colour of the cat?'},
  headers: {
    'api-key': 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'content-type': 'multipart/form-data; boundary=---011000010111000001101001'
  },
  data: '-----011000010111000001101001\r\nContent-Disposition: form-data; name="image"; filename="cat.png"\r\nContent-Type: image/png\r\n\r\n\r\n-----011000010111000001101001--\r\n'
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```