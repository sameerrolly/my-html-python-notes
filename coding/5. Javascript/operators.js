console.log("Operators in js")
console.log("")

// conditional operator
const xn="login"
if (xn==="login"){
    console.log("you're logged in ")
}
else{
    console.log("invalid user")
}

// same thing using ternary operator
// Ternary operators : use for single line code insted of using if else

// syntax: condition ? "if true this works " : "if flase this works"; 
 console.warn("TERNARY OPERATOR'S SYNTAX : CONDITION ? 'IF TRUE THIS WORKS' : 'IF FALSE THIS WORKS' ;" )
 xn ==='login' ? console.log("valid condition works "):console.log("invalid condition works");

//---------------------------------------------------  comparison operator

console.log(4==4)
console.log(4!=4)
console.log(4===4)
console.log(4!==4)
console.log(4<=4)
console.log("diff btw == and ===")
console.log("4==='4' is:",4==="4")
console.log("4==4 is : ",4=="4")
console.log("diff btw == and === is : if both data types and values are same in === then true , else false and on other hand in this == if value is same but data types are not then also be true")
console.log("This process is known as COERCION")

