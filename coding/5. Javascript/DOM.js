console.log(document.body.childNodes[1])
document.body.style.background="grey"

let heading=document.getElementById("heading");
console.log(heading)

// // note if want to make any changes first use document.queryselector property .
// let h1=document.querySelector("div")
// h1.style.backgroundColor="red"
// h1.style.color="yellow"

let neewbtn=document.createElement("button")
neewbtn.innerText="submit button"
console.log(neewbtn)

let div=document.querySelector("main")
div.append(neewbtn);
// div.after(neewbtn);
// div.before(neewbtn);

// div.remove(); 