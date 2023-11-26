<p align="center">
  <a href="">
    <img src="https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png" height="96">
    <h3 align="center">Next.js FastAPI OpenAI GPT-4 Vision API</h3>
  </a>
</p>

> Based off of [digitros' started code](https://github.com/digitros/nextjs-fastapi)

### **Bring your own OpenAI API key** 🔐
Get your own key [here](https://platform.openai.com)

### **Sample request** 📨
```sh
curl -X 'POST' \
  '/api/vision?question=<your-question-text>' \
  -H 'accept: application/json' \
  -H 'api-key: <your-openai-api-key>' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@<image.type>;type=image/<type>'
```
***I'd recommend visiting `/api/docs` and use the Swagger UI***