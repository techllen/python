console.log("connected to JS");

//load report
function alertWeatherReport(element){
    alert("Loading weather report...");
    document.querySelector(".city").innerHTML=element.innerHTML;
}

//remove cookie policy
function removeCookiePolicy(){
    document.querySelector(".cookie-policy").remove();
}

//temperature conversion
function celsiusToFahrenheit(){
    var lowsC = document.querySelectorAll(".low");
    var highsC = document.querySelectorAll(".high");
    var lowsF = [];
    var highsF = [];
//the length of lows and high is the same so the same number of 
//iterations can be used
    for (var i = 0; i < lowsC.length; i++) {
        var lowf = Math.floor(((9/5)*parseInt(lowsC[i].innerHTML)) + 32); 
        lowsF.push(lowf);

        var highf = Math.floor(((9/5)*parseInt(highsC[i].innerHTML)) + 32); 
        highsF.push(highf);
//putting back the values
        (lowsC[i]).innerHTML = `${lowsF[i]}&deg;`;
        (highsC[i]).innerHTML = `${highsF[i]}&deg;`;
    }
}
// this function make async call to the api to get the current weather
async function getCurrentWeather(element){
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    // var response = await fetch("http://api.openweathermap.org/data/3.0/forecast/daily?id=524901&APPID=52ec07192d14ae6c4d0605f05fec6566");
    // var response = await fetch("http://api.openweathermap.org/data/2.5/weather?q=Berlin&APPID=52ec07192d14ae6c4d0605f05fec6566");
    var cityName = element.innerHTML
    var response = await fetch(`http://api.openweathermap.org/data/2.5/weather?q=${cityName}&APPID=52ec07192d14ae6c4d0605f05fec6566`);
    // We then need to convert the data into JSON format.
    var weatherData = await response.json();
    console.log(weatherData)
    return weatherData;
}

// console.log(getCurrentWeather())