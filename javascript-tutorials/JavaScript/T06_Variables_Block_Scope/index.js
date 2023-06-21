{
    // block scope
    {
        // nested block scope
    }
}

function doSomething(){
    var test1 = 8
}

for(var i = 1; i <= 10; i++){
    //block scope
}

console.log(i) // can still access i use let instead

//console.log(test1) // throws error out of scope 