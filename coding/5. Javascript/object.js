//----------------------------------------- Objects -------------------------------------
/*
syntax :
  variable variable.name ={key:'values', key='string', key = 123}
  */

const obj = {
  Name: "sameer",
  class: "mca",
  rollno: 123,
};
console.log(obj);
console.log(obj.class);

//   ------------------------------------Variables----------------------------------------

// 3 variable : let const var
// ---------------------------------------------------------let variable

let Name = "ROLLY";
console.log(" using let variable: ", Name);

let classes;
classes = "bca";
console.log(classes);
// NOTE : can't redeclared

// ---------------------------------------------------------const variable----------------
const abc = "sameer";
console.log("using const variable:", abc);
// NOTE : can't update value after declaring

const abcd = 123;
console.log("using const variable:", abcd);

// ----------------------------------------------------------var variable---------------------
var x = 10;
console.log("value of x using 'var' variable:", x);

var x = "updated variable value with same name ";
console.log("value of x after update :", x);
console.log(
  "NOTE: values of variable var can be updatable, on other hand values of const,let can't"
);

// Block scope

console.info(
  "Block Scope : is that where a value is initailized under a block and cant be able to print outside of block, Note: const and let variable are block scope"
);
console.warn("var is not a block scope");

// example :
var b = "before function";

function blocked() {
  let a = 10;
  const xyz = "block scope example";
  var b = "not a block scope";
  console.log("value of const variable ", xyz);
  console.log("value of let variable ", a);
  console.log("value of var variable ", b);
}
blocked();

console.log("declared outside as well as inside of block", b);
console.warn(
  "note: ik variable var x unction to pehle bnaya te ik function vich , jdo conslore kraage pehle function vla print hou fr bahar vla"
);

// practice-------
// ----------1.-var variable : jedi value baad ch declare hoi , ohi print hou 

var az = 10;
{
  var az = "sam";
  console.log(az);
}
console.log(az);
// -----------2. let variable  : update kr skde te saria values show hon gia 
let ax = 20;
{
  let ax = "rolly";
  console.log(ax);
}
console.log(ax);
// -----------3. const variable : update v ni te redeclared v ni hou 

// const ac=30
// {
//     ac="mca"
//   console.log(ac);

// }
// console.log(ac);


// ------------------------------------hoisting-----------------------------

/*Intro : Hoisting is that where you can console or print first and then declare value  
*/
console.log("hoisting using var variable shows undefined output:",hoi)
var hoi="10"

/* Hoisting using let and const variable shows error 
console.log(nm)
const nm=301
let nm=102
*/