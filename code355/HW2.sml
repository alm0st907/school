(*
Garrett Rudisill
WSU ID 11461816
HW2 for ML
Coded on Ubuntu 17.10/Windows 10 with SMLNJ
*)

(*higher order functions*)
fun zip nil l = nil
    | zip l nil = nil
    | zip (a::la) (b::lb) = (a,b)::(zip la lb) ;

zip [1,2,3] ["one", "two"];

fun tail_zip l1 l2 =
    let
        fun zip' (a::list1) (b::list2) list = zip' list1 list2 ((a,b)::list) (*accumulating function for tail recursion*)
            | zip' [] [] list = rev list (* reversing the list on a null l1/l2 matching case*)
    in
        zip' l1 l2 []
    end;

fun unzip l = 
  case l
    of nil => (nil, nil)
     | (a,b)::tl => 
        let val (l1, l2) = unzip tl
        in (a::l1, b::l2) end;

fun map f [] = []
    | map f (x::rest) = (f x)::(map f rest);

fun fold f base [] = base
    | fold f base (x::rest) = f x (fold f base rest);

fun filter pred [] = []
    | filter pred (x::rest) = if pred x then x::(filter pred rest) else (filter pred rest);
   

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

fun zipTail aList bList =
    let
    fun myzip  nil l = nil
        |   myzip  l   nil  = nil
        |   myzip (a::la) (b::lb)  = (a,b)::(myzip la lb) 
        
    in
        zipTail [] []
    end;




    (*Histogram*)

(*
Problem 2 sum and deepSumOpion
*)

(*
Problem 3  eitherTree/ Either search
*)

(*
Problem 4 zip
*)

(*
Problem 5 findMin/FindMax/minMaxTree
*)



(*TEST ZONE*)