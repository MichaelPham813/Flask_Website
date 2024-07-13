/* Add library of: bvambient.js */ 

// This is for the background particle setting
document.addEventListener("DOMContentLoaded", function() {
    var demo1 = new BVAmbient({
        selector: "#ambient",
        fps: 60,
        max_transition_speed: 12000,
        min_transition_speed: 8000,
        particle_number: 75,
        particle_maxwidth: 60,
        particle_minwidth: 10,
        particle_radius: 50,
        particle_opacity: true,
        particle_colision_change: true,
        particle_background: "#58c70c",
        particle_image: {
        image: false,
        src: ""
        },
        responsive: [
        {
        breakpoint: 768,
        settings: 
        {
            particle_number: "70"
        }
        },
        {
        breakpoint: 480,
        settings: 
        {
            particle_number: "10"
        }
        }
        ]
    });
});

function getlocation()
{
    navigator.geolocation.getCurrentPosition(showlocation);
}
let obj = []
function showlocation(position)
{
    let lat = position.coords.latitude;
    let lon = position.coords.longitude;
    const dict_value = {lat,lon};
    const string = JSON.stringify(dict_value);
    var a= document.createElement("h3"); 
    var b= document.createElement("p");
    var c = document.querySelector("#div_container");
    var c1 = c.querySelector("#div_container_2");
    var c2 = c1.querySelector("#map_container");
    a.appendChild(document.createTextNode("Your location"));
    b.appendChild(document.createTextNode(`https://maps.google.com/maps?q=${lat},${lon}&hl=en&z=5&amp`))
    c2.append(a);
    c2.append(b);
    console.log(string);
    $.ajax(
        {
        url:"/user_loc",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(string),  
    });
    
}

getlocation()