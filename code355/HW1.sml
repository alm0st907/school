(*This is leftover from hello world, just a reference*)
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
