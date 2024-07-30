const btn = document.getElementById("check")
const val = document.getElementById("val")
const res = document.getElementById("name")
const number = Math.floor(Math.random() * 100) + 1;
console.log(number)
let count = 1

function checkValue() {

    let value = val.value

    if (value == number) {
        res.innerText = `You Won By This ${count} Times`
        // alert("You Won")
    }
    else if (value < number) {
        res.innerText = "Enter A Higher Value"
    }
    else {
        res.innerText = "Enter A lower Value"
    }
    count += 1;

}

btn.addEventListener("click", checkValue)

for (let index = 0; index <= 8  ; index++) {
    document.querySelectorAll(".col")[index].addEventListener("click", handleCLick)

}

let currentPlayer = "X"
let array = Array(9).fill(null)
let box = document.getElementById("box")

function handleCLick(el){
    const id = Number(this.id)
    if (array[id] != null) return console.log("Done Already")
    // console.log(id)
    array[id] = currentPlayer;
    this.innerText = currentPlayer;
    checkWinner();
    currentPlayer = currentPlayer == "X" ? "O" : "X"
    console.log(array)
//  0 1 2
//  3     4 5
//  6      7 8
}

function checkWinner(){
    if(
     (array[0] !== null && array[0] == array[1] && array[1] == array[2]) || 
       (array[4] !== null && array[4] == array[3] && array[3] == array[5]) ||
       (array[6] !== null && array[6] == array[7] && array[7] == array[8]) ||

       (array[3] !== null && array[3] == array[0] && array[0] == array[6]) ||
       (array[1] !== null && array[1] == array[4] && array[4] == array[7]) ||
       (array[5] !== null && array[5] == array[2] && array[2] == array[8]) ||

       (array[8] !== null && array[8] == array[4] && array[4] == array[0]) ||
       (array[2] !== null && array[2] == array[4] && array[4] == array[6]) )
    {   
        // document.write("Winner Is : "+ currentPlayer + " Player")
        box.innerHTML = "<h1> Winner Is : " + currentPlayer + " Player </h1>"
        
    }

    else if(!array.some((e) => e === null)){
        box.innerHTML = "<h1> The Game Is Draw : Press Below To Re-Start </h1>"
    }
}



// const ad = document.querySelector("body").children;

// for(let i=0; i < ad.length; i++){
//     ad.item(i).addEventListener("click",()=> {
//         ad.item(i).remove();
//     })
// }