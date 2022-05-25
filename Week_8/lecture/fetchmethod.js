// fetch("https://api.github.com/users/techllen")
//     .then(response => response.json() )
//     .then(coderData => console.log(coderData) )
//     .catch(err => console.log(err) )

import fetch from "./node_modules/node-fetch";

async function getCoderData() {
        // The await keyword lets js know that it needs to wait until it gets a response back to continue.
        var response = await fetch("https://api.github.com/users/techllen");
        // We then need to convert the data into JSON format.
        var coderData = await response.json();
        return coderData;
    }
        
    console.log(getCoderData());
    