console.warn("OBJETCS")
//                                  1. Creating an object
let obj={
    Name:"sameer",
    class:"MCA",
    AGE:24
}
console.log(obj)
console.error("declaring function inside objects")
// -----------------------------------------------------------------------------------------
// 2.                               2.declaring function in objects with two ways

const data={
    dataFn (){
        console.log("tax 10%")  /*1st way (mainly used)*/
},
};

const SAM={
    salary: 60000
};
const SAM2={
    salary:7011001,
    dataFn (){
        console.log("tax 20%")  /*1st way (mainly used)*/
},
};
const SAM3={
    salary:800000
}
SAM.__proto__=data;
SAM2.__proto__=data;
SAM3.__proto__=data;
console.error("Note: We can assign functions in every obj like in SAM2 same function name i.e dataFn (also used inside data object) is used with different value and the function output will be its own value of an object")


//                                          3.CLASSES

console.log("")
console.warn("CLASSES")

// syntax: class className{...} let objName= new className();
// --------------------------------------------------------------------------
class stuData{
     fail(){
        console.log("failed")
     }
     pass(){
        console.log("passed")
     }
}
let stuObj=new stuData();
console.log(stuObj)
console.log(stuObj.pass())
console.log(stuObj.fail())
// -----------------------------------------------------------------------------
// 1. class with defining variable with (this.) this method
class stuData1{
    fail(){
       console.log("failed")
    }
    pass(){
       console.log("passed")
    }
    variableNew(test){
        this.testName=test;
    }

}
let objStu= new stuData1();
objStu.variableNew("test areas")
// ----------------------------------------------------------------------------------


//                                                  3.CONSTRUCTOR

class relation{
    constructor(relate,age){
        console.log("this is constructor")
        this.relate=relate;
        this.age=age
    }
    father(){
        console.log("father")
    }
    mother(){
        console.log("mother")
    }
}
let Father= new relation("father","60");
console.log(Father)
console.log(Father.mother())
let Mother= new relation();
console.log(Mother.father())
// ------------------------------------------------------
//                                                    4.INHERITANCE
console.log("")
console.warn("Inheritance")
console.log("Syntax : \n class Parentclass{......} \n class childClass extends Parentclass{.......} ")
/*
class Parentclass{
   
}
class childClass extends Parentclass{

}
*/

// 1. example of inheritance

class Gparent{
    hello(){
        console.log("hello")
    }
}
class Parent extends Gparent{
    by(){
        console.log("by")
    }
    no(){
        console.log("noops")
    }
}
class Gchild extends Parent{
    by(){
        console.log("by 2")
    }
}
let childClass=new Parent();
let gchildobj=new Gchild();

//                                   SUPER KEYWORD

console.log("")
console.warn("SUPER KEYWORD : used to call constructor of parent class to access its properties and methods")
console.log("SYNTAX : \n super(argument) \n super.parentMethod(argument)")