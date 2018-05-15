# Javascript Undefined Behavior

```
<button id="btn-0">Button 1!</button>
<button id="btn-1">Button 2!</button>
<button id="btn-2">Button 3!</button>

<script type="text/javascript">
  var prizes = ['A Unicorn!', 'A Hug!', 'Fresh Laundry!'];
  for (var btnNum = 0; btnNum < prizes.length; btnNum++) {
      // for each of our buttons, when the user clicks it...
      document.getElementById('btn-' + btnNum).onclick = function() {
          // tell her what she's won!
          alert(prizes[btnNum]);
      };
  }
</script>
```

The above javascript contains some undefined behaviour, namely, prizes[btnNum] is always undefined.

## Problem:

The anonymous function we're assigning to the buttons' onclicks has access to variables in the scope outside of it (closure). In this case, it has access to btnNum.

* A closure is a function that accesses a variable "outside" itself
* One useful thing to do with a closure is to create something like an "instance variable" that can change over time and can affect the behavior of a function.
```
// function for getting the id of a dom element,
// giving it a new, unique id if it doesn't have an id yet
var getUniqueId = (function(){
    var nextGeneratedId = 0;
    return function(element) {
        if (!element.id) {
            element.id = 'generated-uid-' + nextGeneratedId;
            nextGeneratedId++;
        }
        return element.id;
    };
})();
```

**When a function accesses a variable outside its scope, it accesses that variable, not a frozen copy.** So when the value held by the variable changes, the function gets that new value. By the time the user starts pressing buttons, our loop will have already completed and btnNum will be 3, so this is what each of our anonymous functions will get for btnNum!

## The Solution

We can solve this by wrapping our anonymous function in another anonymous function that takes btnNum as an argument. Like so:

```
<button id="btn-0">Button 1!</button>
<button id="btn-1">Button 2!</button>
<button id="btn-2">Button 3!</button>

<script type="text/javascript">
    var prizes = ['A Unicorn!', 'A Hug!', 'Fresh Laundry!'];
    for (var btnNum = 0; btnNum < prizes.length; btnNum++) {
        // for each of our buttons, when the user clicks it...
        document.getElementById('btn-' + btnNum).onclick = function(frozenBtnNum){
            return function() {
                // tell her what she's won!
                alert(prizes[frozenBtnNum]);
            };
        }(btnNum);  // LOOK! We're passing btnNum to our anonymous function here!
    }
</script>
```

This "freezes" the value of btnNum.

So when we pass btnNum to the outer anonymous function as its one argument, we create a new number inside the outer anonymous function called frozenBtnNum that has the value that btnNum had at that moment (0, 1, or 2).

Our inner anonymous function is still a closure because it still reaches outside its scope, but now it closes over this new number called frozenBtnNum, whose value will not change as we iterate through our for loop.

#### Primitives vs. Objects

btnNum is a number, which is a primitive type in JavaScript. Primitives are "simple" data types (string, number, boolean, null, and undefined in JavaScript). Everything else is an object in JavaScript (functions, arrays, Date() values, etc).

#### Arguments Passed by Value vs. Arguments Passed by Reference

One important property of primitives in JS is that when they are passed as arguments to a function, they are copied ("passed by value"). So for example:

```
var threatLevel = 1;

function inspireFear(threatLevel){
    threatLevel += 100;
}

inspireFear(threatLevel);
console.log(threatLevel);  // 1
```

In contrast, when a function takes an object, it actually takes a reference to that very object. So changes you make to the object in the function persist after the function is done running. This is sometimes called a side effect.

```
var scaryThings = ['spiders', 'Cruella de Vil'];

function inspireFear(scaryThings){
    scaryThings.push('why am i doing this to myself');
}

inspireFear(scaryThings);
console.log(scaryThings);
// ['spiders', 'Cruella de Vil', 'why am i doing this to myself']
```
