// let h = document.getElementsByClassName("head");


let para=document.getElementById("h1")
para.style.backgroundColor="yellow";
para.style.textAlign="center";

// --------------------------------------class and tagname not working

// using queryselector using tag:

let clr=document.querySelector("p")
clr.style.textAlign="center"
clr.style.backgroundColor="red"
clr.innerText="Queryselector using tagname"


// using queryselector using class:

let mains=document.querySelector(".main")
mains.style.textAlign="center"
mains.style.backgroundColor="green"
mains.innerText="Queryselector using class"


// using queryselector using id:
let sec=document.querySelector("#sec");
sec.style.textAlign="center"
sec.style.color="white"
sec.style.backgroundColor="blue"
sec.innerText="Queryselector using id"

