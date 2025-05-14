/*
Logical Operator:-
&& (AND) || (OR) ! (NOT)
&& (minimum two input and only one boolean output)
if all the conditions are true then the output is true otherwise false.
console.log( 10>6 && 10>20 );
console.log( 10>6 && 10>2 );

|| (minimum two input and only one boolean output)
if all the conditions are false then the output is false otherwise true.
console.log( 10>60 || 10>20 );
console.log( 10>60 || 10>2 );
console.log( 10>6  10>2 );

! (only and only one input and only one boolean output)
this not gate is also called INVERTER gate.
if the input is true then the answer is false and vice-versa.
console.log( !(10>6) );


# Ternary Operator
variable_name = condition ? true : false ;
Example:-
var z = 10>7 ? "Hello" : "Bye" ;
Example:-
var per = 82;
var passFail = per>=33 ? "Pass" : "Fail" ;
console.log( passFail );
*/

/*
WAP to calculate Gross salary of an employee where HRA is 20% and DA is
30% of his basic salary.
HINT:- Gross_Salary = Basic_Salary + HRA + DA

bs = 15000;
hra = bs*0.20;
da = bs*0.30;
gs = bs+hra+da;
console.log("Gross Salary : "+gs);


WAP to calculate gross salary of an emloyee where HRA and DA is 
20 and 30% if the basic salary is above 20000 other 30 and 40%.

bs = 10000;
hra = bs>=20000 ? bs*0.20 : bs*0.30;
da = bs>=20000 ? bs*0.30 : bs*0.40;
gs = bs+hra+da;
console.log("Gross Salary : "+gs);

WAP to swap two numbers.

var a = 7;
var b = 5;
var c = a;
a = b;
b = c;
console.log("A : "+a);
console.log("B : "+b);

WAP to swap two numbers without using third variable.

var a = 7;
var b = 5;
a = a*b; //35
b = a/b; //7
a = a/b; //5
console.log("A : "+a);
console.log("B : "+b);

*/