(*This is a comment: Hello World Program*)
val test = [1,2,3,4];
print "Hello World, this is my first SML program!!!";

(*function to print out our test*)
fun printList stuff = print(String.concatWith","(map Int.toString stuff)); 
fun printStringList stuff = print(String.concatWith", "stuff);
printList test;
val test = rev test; (* re assinging test to be reversed*)
printList test; (* printint the test list*)
val list = ["ab","cd","ef","gh"];
printStringList list;
print (String.concatWith" " list);

val list = rev list;
print (String.concatWith" " list);

val x = 2;
val y=3;
val z= x+y;
val z = z * 20;


(*this is the class code*)

fun f x = x*2; (*declaring a function named f*)
val absofx = if x < 0 then 0 - x else x;

val x = (~2); (*tilde is the negative sign declaration for a number);