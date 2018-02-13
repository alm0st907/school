(*
Garrett Rudisill
WSU ID 11461816
HW2 for ML
Coded on Ubuntu 17.10/Windows 10 with SMLNJ
*)

(*
TO DO
    Make count in list tail recursive properly
        add the secondary function with an accumulator to do this

    DeepSumOption
        havent done really anything

    problem 4/5
*)

(*higher order functions*)

fun map f [] = []
    | map f (x::rest) = (f x)::(map f rest);

fun foldL f base [] = base
    | foldL f base (x::rest) = f x (foldL f base rest);

fun filter pred [] = []
    | filter pred (x::rest) = if pred x then x::(filter pred rest)
    else (filter pred rest);

fun inList (n,[]) = false
    | inList(n,x::rest) = if n=x then true else inList(n,rest);
   
fun removeDuplicates [] = []
    | removeDuplicates(x::rest) = x::removeDuplicates(filter (fn y => y <>x)rest);


(*
Problem 1
countInList, zipTail, histogram
*)

    (*count in list, pass a list and a variable to be scanned for. Return how many instances exist in the list*)

fun countInList [] n = 0
    | countInList (x::rest) n = if x = n then 1 + countInList (rest) n else 0 + countInList rest n;
    
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

fun histogram list = removeDuplicates( zipTail list (map (countInList list)list));
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
    | deepSum list = foldL (fn x=> fn y=> x+y) 0 (map (foldL (fn a => fn b => a+b) 0) list);
    (*inner fold works like addup from slides and gets mapped to each of the lists, then the outer fold performs the final summing *)

deepSum [[1,2,3],[4,5],[6,7,8,9],[]];
deepSum [[10,10],[10,10,10],[10]];
deepSum [[]];
deepSum [];

    (*deep sum option*)

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

(*
Problem 4  eitherTree/ Either search
*)

datatype either = ImAString of string | ImAnInt of int;


(*
Problem 5 findMin/FindMax/minMaxTree
*)



(*TEST ZONE*)

