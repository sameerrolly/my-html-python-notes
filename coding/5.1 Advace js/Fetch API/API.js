console.warn("API : application programming interface");
console.error("Fetch API :  fetch(url,[options])");
console.log("");

const URL = "https://cat-fact.herokuapp.com/facts";

const facts = async () => {
    console.log("fetching data using async-await")
  let response = await fetch(URL);
  console.log(response.status);
  console.log(response);
let data=await response.json();
console.log(data)
};
