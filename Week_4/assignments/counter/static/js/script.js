console.log('connected to js')

// getting paragraph length and the first letter of the paragraph
var paragraphLength = document.getElementsByTagName('p')[0].innerHTML.length
var paragraphFirstLetter = document.getElementsByTagName('p')[0].innerHTML.slice(0,1)

// checking if the first number in a paragraph is 1
if (paragraphLength == '7'){
    if (paragraphFirstLetter == '1'){
        document.getElementsByTagName('p')[0].innerHTML = '1 time'
    }
}
// for debugging
console.log(paragraphFirstLetter)
console.log(paragraphLength)
