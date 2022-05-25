// fetch("https://api.github.com/users/techllen")
//     .then(response => response.json() )
//     .then(coderData => console.log(coderData) )
//     .catch(err => console.log(err) )

// import fetch from "./node_modules/node-fetch";

// async function getCoderData() {
//         // The await keyword lets js know that it needs to wait until it gets a response back to continue.
//         var response = await fetch("https://api.github.com/users/techllen");
//         // We then need to convert the data into JSON format.
//         var coderData = await response.json();
//         return coderData;
//     }
        
//     console.log(getCoderData());
    

var data = {
    "orders": [
      {
        "orderno": 784692,
        "date": "June 30, 2088 1:54:23 AM",
        "trackingno": "TN000391",
        "customer": {
          "custid": 11045,
          "fname": "Sue",
          "lname": "Hatfield",
          "address": "1409 Silver Street",
          "city": "Ashland",
          "state": "NE",
          "zip": 68003
        }
      },
      {
        "orderno": 784693,
        "date": "March 3, 2088 8:18:14 PM",
        "trackingno": "TN000468",
        "customer": {
          "custid": 11045,
          "fname": "Sue",
          "lname": "Hatfield",
          "address": "1409 Silver Street",
          "city": "Ashland",
          "state": "NE",
          "zip": 68003
        }
      }
    ]
  }

// KNOWING DATA TYPE
console.log(typeof(data));
// 'object'
console.log(Array.isArray(data));
// false
console.log(Array.isArray(data.orders));
// true
  
// ACCESSING DATA
// square brackets
console.log(data["orders"][1]["date"])
// dot notation
console.log(data.orders[1].date)

  