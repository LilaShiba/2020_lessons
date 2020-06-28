// Index.js body parser

const database = require('./mongoObj');
database.init()
// read forms sent
const bodyParser = require('body-parser');
app.use(bodyParser.json());

// READ: GET Client
// create map and show all markers in db
async function mapInit() {
    // add locate user funcntion geolocation
    const mymap = L.map('map').setView([cordObj.lat, cordObj.lon], 12);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);
    // show all current markers
    const url = '/show';
    const data = await fetch(url);
    const locationData = await data.json();
    // add markers
    for (let idx = 0; idx < locationData.length; idx++) {
      const m = L.marker([parseFloat(locationData[idx].lat), parseFloat(locationData[idx].lon)]).addTo(mymap).bindPopup(locationData[idx].note).openPopup();
      m._icon.id = locationData[idx]._id;
    }
    mymap.setView([cordObj.lat, cordObj.lon])
  }

  // CREATE: POST Client
  async function addData() {
    const note = document.getElementById('note').value;
    cordObj.note = note;
    const options = {
      method: 'POST',
      body: JSON.stringify(cordObj),
      headers: {
                'Content-Type': 'application/json',
              },
        };
    await fetch('/location', options)
    console.log('add data done');
  }

// SERVER
// POST
const {lat, lon, note} = req.body;
console.log(lat, lon, note)
database.userInfo.insertOne({lat, lon, note});
console.log('add info')
res.redirect('/');


// GET
const data = await database.userInfo.find().toArray();
res.json(data);