//https://www.youtube.com/watch?v=tc8DU14qX6I
console.log('About to get Mars Rover pics')
const url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY"

fetch(url)
  .then(res => res.json())
  .then(res => {
    document.getElementById('marsH1').textContent = res.photos[0].camera.full_name
    document.getElementById('mars').src=res.photos[0].img_src
  })
  .catch(error =>{
    console.error(error)
  })
