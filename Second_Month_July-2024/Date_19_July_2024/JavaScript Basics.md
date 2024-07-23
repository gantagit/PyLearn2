
// // // Java Script basics
// // console.log("hello world");

// // // ; in java Script semicolon is optional

// // console.log(2+2)
// // console.log(2-2)
// // console.log(2*2)
// // console.log(2/2)
// // // this is a comment

// // var age = 65;
// // var name = "VJ"
// // var isMarried = true

// // console.log(age, name, isMarried)
// // age +=1
// // console.log(age)

// // // This is Java script
// // var xObject = {}
// // xObject = {
// //   name : "Vijay",
// //   age1 : 65
// // }

// // // The is JSON
// // // {
// // //   "name" : "Vijay",
// // //   "age1" : 65
// // // }

// // // console.log(xObject)
// // console.log(xObject.age1)
// // console.log(xObject.name)
// // // console.log(xObject["name"])
// // // we can also fetch using Square braces but its always best to use dot notation

// // // Python Dict -> JSON -> JS Object -> Hashmap in java, C#, Ruby


// // var a = 10, b = 5 , c =a+b
// // console.log(c)

// // var a = 10
// // if(a>=10){
// //   console.log("a>=10")
// // }
// // else {
// //    console.log("a<10")
// // }

// // for(var i = 1; i<=10; i++){
// //   console.log(i)
// // }

// // functions
// // define
// function greet(){
//   console.log("Hi, How are you")
// }
// // call
// greet()


// function sum(a,b){
//   console.log(a+b)
// }

// sum(2,3)

// function mul(a,b){
//   return a*b
// }

// var result = mul(2,3)
// console.log(result)

// function check(){
//   return true
// }

// var isMarried = check()
// console.log(isMarried)


// // JSON to JS Object 
// var res = '{"name" : "Pramod","age" : 65,"cars" : ["Audi", "BMW", "Ferrari"]}'
// var parseResponseJS = JSON.parse(res);  // JSON.parse() is used to parse json response
// console.log(parseResponseJS.name)

// var response = '{"name":"Vijay", "age":36}'
// var parseResponseJS = JSON.parse(response)
// console.log(parseResponseJS["age"])


// // JSON to JS Object
// var jsResponse = '{"name" : "Vijay","age" : 36,"cars" : ["Audi","BMW", "Ferrari"]}'
// var objectResponseJS = JSON.parse(jsResponse)
// console.log(objectResponseJS.name)
// console.log(objectResponseJS["age"])

// JS object to JSON response
var jsObject = {
  name : "Ganta",
  age : 65
}

var jsResponse = JSON.stringify(jsObject)
console.log(jsResponse)

// we have similar in python, Java and in each language
// In Python ,  Dict -> JSON and JSON to Dict
// In Java , Hashmap \ Class -> JSON and JSON to Hashmap \ class