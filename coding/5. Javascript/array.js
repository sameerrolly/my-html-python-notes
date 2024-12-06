console.log("")
console.warn("Array in js")

const arrray1=["hello",12,"new"]
arrray1[1]="changed"
console.log(arrray1)

// syntax :
const arr = [10,12,16,20]
console.log("elements of array: ",arr)

console.log("")
console.warn("Methods of Array in js")
// Methods in arrays :
// 1. Push : add element in last
console.log("1. push Method")

const arr1=["sam",21,"mca"]
console.log("before push method",arr1)
arr1.push("Rolly")
console.log("using push method",arr1)

console.log("")
// 2. pop : remove element from last 
console.log("1. pop Method")

const arr2=["sam",21,"mca"]
console.log("before pop method",arr2)
arr2.pop("")
console.log("using pop method",arr2)

// 3. shift : remove element from 1st position in array 
console.log("")
console.log("1. shift Method")

const arr3=[10,20,30]
arr3.shift()
console.log(arr3)


// 4. Unshift : remove element from 1st position in array 
console.log("")
console.log("1. Unshift Method")

const arr4=[10,20,30]
arr4.unshift(40)
console.log(arr4)
console.log("lenghth of array is : ",arr4.length)
console.log("")

// 5. tostring: convert array elements into string
console.warn("convert into string")

let food=["apple","banana","orange"]
console.log(food)
let temp=(food.toString())
console.log(temp)

// 6. concat() : add multiple arrays and gives a result 
let marvel =["thor","ironman","spiderman"]
let dc=["aquaman","wonderwoman","batman"]
console.log("concat of arrays :",marvel.concat(dc));

// 7. slice() : slice(strt,end)
let ab=[1,2,36,4,6]
console.log("slice method:",ab.slice(2,4))

// 8. SPLICE METHOD : variablename.splice(index,no.of element to be replace,element to placed)

let newsplice=["zero","one","two","three"]
console.log(newsplice.splice(1,2,2,"hello"));
console.log(newsplice)

// 9.map (important)
const fname=[
    {
        fname1:"sam",
        lname:"rolly"

    },{
        fname1:"sunny",
        lname:"sharma"

    },{
        fname1:"sahil",
        lname:"kumar"

    }
];
const users=fname.map((fn)=>{
return{
    fullname:fn.fname1+ fn.lname
}
}

)
console.log(users)

// 10. 