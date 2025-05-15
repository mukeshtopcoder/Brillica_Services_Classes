/*
Control Statements:-
if , if_else , Nested if_else , complex condition
Looping:- for , while , do_while

IF 
Syntax:-
if ( condition ){
    statements;
}

if (10>7){
    console.log("Hello"); 
}
if (10>70){
    console.log("Hello"); 
}

IF_ELSE
if (condition){
    true_Statements
}else{
    false_Statements
}
if(10>70){
    console.log("HELLO");
}else{
    console.log("BYE");
}

// WAP to check an entered number is even / odd.
var num = 97;
if (num%2 == 0){
    console.log("Even");
}else{
    console.log("Odd");
}
   
// WAP to find greater value between two.
var a = 10;
var b = 20;
if (a>b){
    console.log(a);
}else{
    console.log(b);
} 


Nested_IF_ELSE
if (condition){
    if(condition){
        true
    }else{
        false    
    }
}else{
    if(condition){
        true
    }else{
        false
    }
}



// WAP to check an entered number is positive, negative or zero.
// num>0  -> positive , num<0 -> negative , num==0 -> zero
var num = 0;
if (num>0){
    console.log("Positive");
}else{
    if(num<0){
        console.log("Negative");
    }else{
        console.log("Zero");
    }
}



// WAP to check an entered charcter is vowel or consonants.
// Vowel:- a,e,i,o,u
var ch = 'z';
if(ch=='a')
    console.log("Vowel");
else
    if(ch=='e')
        console.log("Vowel");
    else
        if(ch=='i')
            console.log("Vowel");
        else
            if(ch=='o')
                console.log("Vowel")
            else
                if(ch=='u')
                    console.log("Vowel")
                else
                    console.log("Consonant");



Complex_Condition  -> Using Logical Operator
if(condition and condition or condition){
    true
}else{
    false
}
*/

// WAP to check an entered character is vowel or consonant.
var ch = 'i';
if ( ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' ){
    console.log("Vowel");
}else{
    console.log("Consonant");
}
