(*
Garrett Rudisill
WSU ID 11461816
HW2 for ML
Coded on Ubuntu 17.10/Windows 10 with SMLNJ
*)

(*
TO DO
    problem 5
*)

(*higher order functions*)

fun map f [] = []
    | map f (x::rest) = (f x)::(map f rest);

fun foldL f base [] = base
    | foldL f base (x::rest) = f x (foldL f base rest);

fun filter pred [] = []
    | filter pred (x::rest) = if pred x then x::(filter pred rest)
    else (filter pred rest);

(*
Problem 1
countInList, zipTail, histogram
*)

    (*count in list, pass a list and a variable to be scanned for. Return how many instances exist in the list*)

fun countInList list cVal =
  let
    fun accumulator [] count = count
        | accumulator (s::list) count =
            if s = cVal
            then accumulator list (count + 1)
            else accumulator list count
  in
      accumulator list 0
  end;

countInList ["3","5","5","-","4","5","1"] "5";
countInList [true, false, false, false, true, true, true] true;
countInList [] "n";
countInList [1, 2, 3, 5, 5, 4] 5;
countInList ["3","5","5","-","4","5","1"] "5";
countInList [] "5";
countInList [true, false, false, false, true, true, true] true;

    (*zipTail - *)

fun zipTail l1 l2 =
    let
        fun sub_zip (a::list1) (b::list2) list = sub_zip list1 list2 ((a,b)::list) (*accumulating function for tail recursion*)
            | sub_zip list1 [] list = (List.rev list)
            | sub_zip [] list2 list = (List.rev list)           
         (* reversing the list on a null l1/l2 matching case*)

    in
        sub_zip l1 l2 []
    end;

zipTail [1,2,3] ["one", "two"];
zipTail [1] [1,2,3,4];
zipTail [] [1,2,3,4];


    (*Histogram*)

fun histogram list = 
    let
        fun removeDuplicates [] = []
            | removeDuplicates(x::rest) = x::removeDuplicates(filter (fn y => y <>x)rest);
    in
        removeDuplicates( zipTail list (map (countInList list)list))
    end;

histogram [1,3,2,2,3,0,3];
histogram [[1,2],[3],[],[3],[1,2]];
histogram [];
histogram [true, false, false, false, true, true, true];
(*
ziptail returns list of tuples, joins first element of each list
remove duplicates returns a list without duplicates
map applies a function to each element of the list and returns said list
*)

(*
val list = [1,1,2,2,3,4,5,5];

val maptest=map (countInList list) list;
val mapzip = zipTail list maptest; *)

(*removeDuplicates (zipTail L (map (countInList L) L))*)

    
        


(*
Problem 2 deepSum and deepSumOpion
*)

    (*deep sum*)
fun deepSum [] = 0 (*base case of empty list*)
    | deepSum list = foldL (fn a=> fn b=> a+b) 0 (map (foldL (fn c => fn d => c+d) 0) list);
    (*inner fold works like addup from slides and gets mapped to each of the lists, then the outer fold performs the final summing *)

deepSum [[1,2,3],[4,5],[6,7,8,9],[]];
deepSum [[10,10],[10,10,10],[10]];
deepSum [[]];
deepSum [];



    (*deep sum option*)
    (*
    this closely replicates the logic of the above solution
    the difference isusing pattern matching to handle the option type before applying our folds to the list/sublist
    *)
fun deepSumOption L =
    let
        fun opAdd (NONE) (NONE) = NONE
            | opAdd (SOME(x)) (NONE) = SOME(x)
            | opAdd (NONE) (SOME(y)) = SOME(y)
            | opAdd (SOME(x)) (SOME(y)) = SOME(x+y)
    in
	    foldL opAdd NONE (map (foldL opAdd NONE) L)
    end;

val test = (deepSumOption [[SOME(1),SOME(2),SOME(3)],[SOME(4),SOME(5)],[SOME(6),NONE],[],[NONE]]);

(*Problem 3 unzip*)

(*
pass in a zipped list
the function will return  a list, with the two unziped lists inside
use map to split the values and make our two sublists for the final answer
    a is the element from the first list, and the first map rips the first element from all the zipped elements
    b is the element from the second position, and ripped from all sublists in the zip
*)
fun unzip list = 
    if null list <> true then [map (fn (a,_) => a) list, map (fn (_,b) => b) list]
    else (nil);

val string_test = zipTail ["1","2","3"] ["one", "two"];
val unzip_test =zipTail [1] [1,2,3,4];
(*val mixed_test = ziptail ["1","2","3"] [1,2,3,4];*)
unzip unzip_test;
unzip string_test;
unzip [];

(*
Problem 4  eitherTree/ Either search
*)

datatype either = ImAString of string | ImAnInt of int;
datatype eitherTree = eLEAF of either | eINTERIOR of (either * eitherTree * eitherTree);

fun eitherSearch (eLEAF (ImAnInt x)) v = if v = x then true else false
    | eitherSearch (eLEAF (ImAString (x))) v = false
    | eitherSearch (eINTERIOR ((ImAString (x)), t1, t2)) v = (eitherSearch (t1) v) orelse (eitherSearch (t2) v)
    | eitherSearch (eINTERIOR ((ImAnInt (x)), t1, t2)) v = if v = x then true else (eitherSearch (t1) v) orelse (eitherSearch (t2) v);
    

(*
Problem 5 findMin/FindMax/minMaxTree
*)

datatype 'a Tree = LEAF of 'a | NODE of ('a Tree) * ('a Tree);
datatype 'a myTree = myLEAF of 'a | myNODE of 'a* 'a*('a myTree)*('a myTree);

fun findMin (LEAF x) = x
    | findMin (NODE (x,y)) = if findMin x < findMin y then findMin x else findMin y;

fun findMax (LEAF y) = y
    | findMax (NODE (x,y)) = if findMax y > findMax x then findMax y else findMax x;




(*TEST ZONE*)

fun eitherTest() =
    let
	val testTree = eINTERIOR(ImAString("1"), eINTERIOR(ImAString("2"), eINTERIOR(ImAnInt(4), eLEAF(ImAnInt(8)), eLEAF(ImAString("9"))), eLEAF(ImAnInt(5))), eINTERIOR(ImAnInt(3), eLEAF(ImAnInt(6)), eINTERIOR(ImAString("7"), eLEAF(ImAString("14")), eLEAF(ImAnInt(15))) ))
	val testInt1 = (eitherSearch testTree 8) = true
	val testInt2 = (eitherSearch testTree 7) = false
	val testInt3 = (eitherSearch testTree 10) = false
	val testInt4 = (eitherSearch testTree 9) = false
	val testInt5 = (eitherSearch testTree 5) = true
	val testInt6 = (eitherSearch testTree 4) = true
	val testInt7 = (eitherSearch testTree 3) = true
    in
	print("\n----------------\neitherTest:\n" ^
	      "test1: " ^ Bool.toString(testInt1) ^ "\n" ^
	      "test2: " ^ Bool.toString(testInt2) ^ "\n" ^
	      "test3: " ^ Bool.toString(testInt3) ^ "\n" ^
	      "test4: " ^ Bool.toString(testInt4) ^ "\n" ^
	      "test5: " ^ Bool.toString(testInt5) ^ "\n" ^
	      "test6: " ^ Bool.toString(testInt6) ^ "\n" ^
	      "test7: " ^ Bool.toString(testInt7) ^
	      "\n----------------\n")
    end;
    
val eTest = eitherTest();
