// console.warn("1.Asynchronous Programming")
// console.error("setTimeout function")
// console.error("setTimeout function's Syntax : \n setTimeout(function-name,seconds)")

// // 1. setTimeout using function: 
// function hello(a){
// console.log("print using setTimeout with 1000= 1 second")
// }
// /*
// setTimeout(hello)
// console.log("")
// console.log("1 second = 1000ms, ")
// */
// console.log("")
// // 2. using setTimeout inside arrow function

// /*
// setTimeout(()=>{
//     console.log("Using setTimeout inside a arrow function, \n syntax : setTimeout(arrow function,seconds)")
// },2000);
// */
// console.log("")
// console.warn("2.Callbacks")
// console.error("Callbacks are: Passing function as argument inside a function")
// console.warn("Syntax: function fName(()=>{....})")

// function hello1(){
//     console.log("3. callbacks: this is a call back function using setTimeout and hello1 function is used as a parameter inside a function, So setTimeout function is also known as callback funtion")
// }
// setTimeout(hello1,1000)

// //    -------------------------- callback hell-------------------------
// console.log("")
// console.warn("3.callback hell")
// console.error("callback hell : calling function(value,()=>{.....repeat})")

// function Getdatas (data,getData){
//     setTimeout(() => {
//         console.log("data",data);
//         if(getData){
//             getData();

//         }
//     }, 1000);
// }

// Getdatas(1,()=>{
//     Getdatas(2,()=>{
//         Getdatas(3,()=>{
//             Getdatas(4);
//         });

//     });
// })

 
// //          ----------------------    Promises       --------------------
 
// console.log("")
// console.warn("4.Promises")
// console.error("new Promises((resolve,reject)=>{.... resolve( 'this is resolve message')}) ")
// console.log("promises types : .then()  and   .catch()")
// // Promise.then((res)=>{})
// // Promise.catch((err)=>{})

//                                             PROMISE CHAin

// function asynFunc(){
//     return new Promise((resolve,reject)=>{
// setTimeout(()=>{
//     console.log("some data....")
//     resolve("success")
// },2000);
//     })
// }
// console.log("fetching some data....")

// let p1=asynFunc();
// p1.then((res)=>{
//     console.log(res)
// })




// async await

console.log("")
console.warn("Async await")
console.error("Async await are keywords used with functions and returns a promise. we can make any normal function as async await")
console.log("Syntax : async function fName(){...}")

async function hello(){
    console.log("hello")
}

console.log("")
console.warn(" await")
console.error(" await will always be used inside async function.mainly used for execution od code result one after one.")
console.log("")
console.log("async await example:")


// async await :

// function getData(id){
//     return new Promise((resolve,reject)=>{
//         setTimeout(() => {
//             console.log("data",id);
//             resolve("promise resolved .")
//         }, 2000);
//     })
// }
// async function getAllData(){
//     console.log("getting data using await and async one by one")
//     console.log("")
//     console.log("getting data 1...")
//     await getData(1);
//     console.log("getting data 2...")
//     await getData(2);
//     console.log("getting data 3...")
//     await getData(3);
//     console.log("getting data 4...")
//     await getData(4);
//     console.log("getting data 5...")
//     await getData(5);
// }

console.warn("async-await overcome the complexity of promise-chain and callback hell")
console.warn("NOTES : ")

// -----------------------------------IIFE (immidiate invoked function expression)
console.warn("syntax of IIFE")
console.error("IIFE function is made just using brackets (function(){..}) and called using(); \n i'e (funtion)();")
console.log("1.simple function : (function(){...})();  \n 2.arrow function : (()=>{..})();  \n 3.async func : (async function fName(){...})();"  )

console.log("")
console.warn("IIFE (immidiate invoked function expression)")
console.error("IIFE used to overcome the problem of calling the async function. \n its a function immidiately called as it is defines")

console.log("")
console.warn("callback and promises are called by default (We don't need to call them after function,these are called automatically and returs the results) \nBut async function has to be called so to overcome the calling problem of async-await we uses the term IIFE")

function getData(id){
    return new Promise((resolve,reject)=>{
        setTimeout(() => {
            console.log("data",id);
            resolve("promise resolved .")
        }, 2000);
    })
}

(async function getAllData(){
    console.log("getting data using await and async one by one")
    console.log("")
    console.log("getting data 1...")
    await getData(1);
    console.log("getting data 2...")
    await getData(2);
    console.log("getting data 3...")
    await getData(3);
    console.log("getting data 4...")
    await getData(4);
    console.log("getting data 5...")
    await getData(5);
})();