################################################################
 In Python, parameters are passed to a function using a mechanism called call-by-object 
 or pass-by-assignment. This means Python passes a reference to the actual object.
 How the object behaves inside the function depends entirely on whether it is mutable 
 (modifiable) or immutable (unchangeable).

 *** Core Parameter Passing Types***
 Positional Arguments:
 Arguments are assigned to parameters based on the order they are passed.
 program:

 Keyword Arguments
 Arguments are explicitly matched using the parameter names, ignoring the position
 program:

 Default Parameters
 You can assign default values to parameters, making them optional during the function call. 
 Optional parameters must always come after required parameters.
 program:

 ***Arbitrary Arguments (Variable Length)
 *args (Positional)
 Accepts an arbitrary number of positional arguments, which are packed into a tuple inside
 the function.

 **kwargs (Keyword)Accepts an arbitrary number of keyword arguments, which are packed into a
  dictionary.

  Mutability vs. Immutability (The Rule)
  Because Python passes references to objects, modifications inside a function depend on 
  the data type.

  Object Type:
  Immutable

  Examples:
  int, float, string, tuple

  Inside the Function:
  Modifying the value creates a new object; the original outside the function remains 
  unchanged.
  

  
  Object Type:
  Mutable
  
  Examples:
  list, dict, set

  Inside the Function:
  Modifying the object directly alters the original outside the function.
################################################################
