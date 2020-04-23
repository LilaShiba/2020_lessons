function nearFind(event){
  event.preventDefault()
  console.log('About to get API data')
  findNEA()

  async function findNEA(){
    const start = document.getElementById('start');
    const stop = document.getElementById('stop');

    const url = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+start.value+"&end_date="+stop.value+"&api_key=DEMO_KEY"
    console.log('url:'+url)
    const res = await fetch(url);
    console.log('Got api')
    const data = await res.json()
    console.log('Populating data')
    console.log(data)
    const stop_v = stop.value
    document.getElementById('myH1').textContent = data.element_count+ " Near Earth Objects On " + stop_v
    all_them_neo = data.near_earth_objects[stop_v]


    // https://stackoverflow.com/questions/46141450/create-li-from-loop-through-array-and-display-to-html-as-a-list
    var str = '<p>'
    all_them_neo.forEach(function(v) {
      str += '<br>'+  "Name: " + v.name + " Magnitude: "+ v.absolute_magnitude_h+ " Diameter: " + v.estimated_diameter.miles.estimated_diameter_max + " Miss Distance: "+v.close_approach_data[0].miss_distance.miles
    });

    str += '</p>';
    document.getElementById("all_neos").innerHTML = str;

    // document.getElementById('myImg').src=data.photos[0].img_src
  }
}
// callback function
document.querySelector('#find-nea').addEventListener('click', nearFind);
