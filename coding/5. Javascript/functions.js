console.log("")
console.warn("functions in js")
console.log("intro to functions")
// 1. fn programs
function login(username,password){

    console.log("logged in by",username + password)
}
login("sameer",123);

// 2. arrays  in functions

function arr21(arr1,arr2,arr3){
 arrays=[arr1,arr2,arr3]
 return arrays;

}

let val=arr21(10,12,14);
let val2=arr21(10,"hello","sam");
let val3=arr21(101,112,114);
console.log("array value of 1st:",val)
console.log(val2)
console.log(val)

// arrow functions: modern js
// 1.
let log=(fname,lname)=>{
    return fname+""+lname;
}
console.log(log("sam","rolly"))
console.log(log(1,"rolly"))
console.log(log("abc","rolly"))

// 2. sum of 2 numbers 
let valsum=(x,y,z)=>{
    // console.log(x+y+z);
    return x+y+z
}
let xy=valsum(10,20,30)
console.log(xy)


// many ways to declare or call a function



// methods in js  :  forEach 
// used in arrays and call bcakfunction 
// function can be passed and retured in js from anywhwere

// 1. callback function  : one function used as a parameter in another function
let fn=()=>{
    console.log("foreach function  : function passing ")
}
fn();
 
function newfn(fn){
    console.log("using fn in another fn as a parameter/argument:")
}
newfn();

console.warn("callback function : is a fn which is used as argument and parameter")
console.log("")

// ------------------------------------forEach---------------
// syntax: array.forEach(element => {
    
// });

// 1.forEach example:
console.warn("example of forEch method ")
let arr0=[1,2,3,4]

arr0.forEach(function newArr(val0){
    console.log(val0);
})
console.warn("In forEach method mainly arrow function is used , NOTE : ALWAYS REMEMBER TO ADD ARROW FUNCTION IN METHOD USING ARRAYS  ")

let arr01=[10,20,30,40]
arr01.forEach((vl)=>{
    console.log(vl)
}) ;

