
//                                           1. TAKE INPUTS FROM USERS AS STRING:

console.warn("1.taking inputs from user as string and integer")
/*
let x=prompt("enter your name!")
alert("your name is : " +  x)
console.log("name is : "+ x)
*/
console.log("")

//                                           2. TAKE INPUT FROM USER AS INTEGER
console.warn("2.taking input as int using parseInt")
/*
let int=parseInt(prompt("enter your age "))
alert("your age:"+int)
console.log("Your age is: " + int)
*/
console.log("")

//                                           3. OBJECTS IN JS
console.warn("3.OBJECTS IN JS")


let studentData={
    Name: "sameer",
    class: "mca"
}
console.log("object in js: ", studentData)
console.log("accessing value(objectName.key): " , studentData.Name)
console.log("")

//                                           4. VARIABLES
console.warn("4.VARIABLES IN JS")


var a=10;
const b=20;
var c=30;
console.log("sum of all varibles:",a+b+c)
console.log("")

//                                            5.OUTPUT IN HTML PAGE

console.warn("4 WAYS TO PRINT IN HTML PAGE")
console.log("1.innerhtml/innetText")
console.log("2.document.write()")
console.log("3.window.alert()")
console.log("4.console.log()")

// 1. DOCUMENT.WRITE()

// var a =document.write("print output using document.write()")
console.error("1.document.write() prints output on html page")

// 2.WINDOW.ALERT()

var a=window.alert("WINDOW.ALERT USED ")
console.error("2.window.alert() show a pop-up on html page")

// 3.iNNERHTML

var a=document.getElementById("para").innerHTML="3.INNERHTML IS USED TO PRINT THIS PARAGRAPH"
console.error(a)

// 4. Console.log

console.error("4.console.log")

// ----------------------------------------------------------------------------------------------------------------------

//                                                      6.Ternary operator

console.log("")
console.warn("TERNARY OPERATOR")
console.log("ternary operator is a shortcut of if-else statement")

let age=18;
let result=   age>=18?"adult":"minor";
console.log("Result is : ",result)
console.error("if-else using ternary operator")

// ---------------------------------------------------------------------------------------------------------------------

//                                                        7. FUNCTIONS

