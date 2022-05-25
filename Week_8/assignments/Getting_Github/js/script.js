console.log("connected to js"); 

// this method get user data from the API
async function getUser() {
        // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.github.com/users/techllen");
        // We then need to convert the data into JSON format.
    var coderData = await response.json();
    // selecting a specific element to place the information
    document.querySelector(".intro").innerHTML = `${coderData["name"]} a ${coderData["bio"]} has ${coderData["followers"]} followers on Github`
    // console.log(Object.keys(coderData).length)
    document.getElementById("user-data").style.display = "block"
    displayingKeys(coderData)
    return coderData
    }

// this method create a series of options in a webpage for the user to select
function displayingKeys(coderData){
    // iterating through all the keys
    for(var keyIndex = 0; keyIndex < Object.keys(coderData).length; keyIndex++){
    // setting options
    // console.log(Object.keys(coderData)[keyIndex])
    var option = document.createElement("option")
    option.text = `${Object.keys(coderData)[keyIndex]}`
    option.value = `${Object.keys(coderData)[keyIndex]}`
    // adding options to the page
    document.getElementById("selection").appendChild(option)
    }
    // console.log(document.querySelector("#selection").innerHTML)
}
// this method get user option selection and display it on a webpage
async function getUserSelection(){
    // getting the selected option
    select = document.getElementById('selection')
    var selectedValue = select.options[select.selectedIndex].value;
    // console.log(selectedValue);
    dataValue = await getUser()
    // console.log(dataValue[`${selectedValue}`])
    // displaying the user selection
    document.querySelector(".content").textContent = dataValue[`${selectedValue}`]
}




