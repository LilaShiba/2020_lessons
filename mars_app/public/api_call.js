function marsFind(event){
  event.preventDefault()
  console.log('About to get Mars Rover pics')
  catchMars()

  async function catchMars(){
    const sol = document.getElementById('sol');
    const camera = document.getElementById('camera');
    // calling a route in my server
    // api call
    const url = `mars/${sol.value}/${camera.value}`
    // this url makes the api call
    const res = await fetch(url);
    // it returns the api data
    const data = await res.json()
    // cool dom & parsing
    console.log('Populating data')
    console.log(data)
    document.getElementById('myH1').textContent = data.photos[0].camera.full_name
    document.getElementById('myImg').src=data.photos[0].img_src
  }
}
// callback function
document.querySelector('#find-mars').addEventListener('click', marsFind);
