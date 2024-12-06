console.log("")
console.warn("Methods in js")
// 1. print list of methods using---------------------1. foreach  method in js
 
console.warn("forEach is used for performing the task on arrays like to show its list and make some updations and performs some specific tasks on arrays elements")
arrMethods=["forEch","map"]
let methd=(val,indx)=>{
    console.log("methods in js: ",val,"",indx+1);   
}
arrMethods.forEach(methd);

console.log("")
// ------------------------------  -----------------  2. map method (imp)----------------
console.warn("Map method")
console.log("")
console.warn("returns a new array with results of some operations: arr.map(cllbckfn(value,index,array))")
// -------------------------------------------using map to print array

console.log("using map to print array")
console.log("")

let ar=[2,4,6]
let newArr=(val)=>{
    return val*2;
}
let xz=ar.map(newArr)
console.log("after map new array: ",xz)
console.log("inal array before map orig",ar)


// ---------------------------------------------------3. filter method--------------------------------------
console.log("")
console.warn("filter method")
// example 
let numbersArr=[10,11,13,16];

let evenArr=numbersArr.filter((val)=>{
    return val%2===0;
})
console.log(evenArr)

// ---------------------------------------------------4. reduce method

// used to get result in single digit 

let sm=[1,2,3,4]

let sumarr=sm.reduce((val,neval)=>{
    return val+neval;
})
console.log(sumarr)