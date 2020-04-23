
const express = require('express');
const app = express();
// dotenv
require('dotenv')
const api_key = process.env.MARS_API_KEY
console.log(api_key)
// use fetch
// npm i node-fetch --save
const fetch = require("node-fetch");
app.listen(4000, ()=> console.log('Running on 4000'));
app.use(express.static('public'));

app.get('/mars/:sol/:camera', async (req, res) =>{
  console.log(req.params)
  const sol = req.params.sol
  const camera = req.params.camera

  const url = `https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=${sol}&camera=${camera}&api_key=B0HKkbxQ9ovFxTXg5TcwKMU2PsFwScu12gYqeR8T`
  const resp = await fetch(url);
  const data = await resp.json()
  res.json(data)
})
