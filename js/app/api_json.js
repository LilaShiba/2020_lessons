//https://www.youtube.com/watch?v=tc8DU14qX6I
console.log('About to get ISS info')
// leaflet

// make map
const mymap = L.map('issMap').setView([51.505, -0.09], 2);
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
// make tiles
const tileUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
const tiles = L.tileLayer(tileUrl, { attribution });
tiles.addTo(mymap);
// custom icon
const myIcon = L.icon({
    iconUrl: 'shiber.jpeg',
    iconSize: [50, 32],
    iconAnchor: [25, 16]
});
const marker = L.marker([0, 0], {icon: myIcon}).addTo(mymap);

// api call function
async function catchMars(){
  //api call
  const url = "https://api.wheretheiss.at/v1/satellites/25544"
  const res = await fetch(url);
  const data = await res.json()
  // lat = data.latitude
  // lon = data.longitude
  // same as above
  const {latitude, longitude} = await data
  document.getElementById('issH1').textContent = "Where is the "+ data.name + ' Right Now?'
  document.getElementById('issP1').textContent = "latitude: " + latitude.toFixed(2)
  document.getElementById('issP2').textContent = "longitude: " + longitude.toFixed(2)
  //marker update
  console.log(latitude, longitude)
  marker.setLatLng([latitude, longitude])
  mymap.setView([latitude, longitude], 4)
  //myIcon.setLatLng([latitude, longitude])
}

catchMars();
setInterval(catchMars, 2000)
