//https://www.youtube.com/watch?v=tc8DU14qX6I
console.log('About to get Mars Rover pics')

catchMars()

async function catchMars(){


  const url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY"
  const res = await fetch(url);
  const data = await res.json()
  document.getElementById('marsH1').textContent = data.photos[0].camera.full_name
  document.getElementById('mars').src=data.photos[0].img_src

}
