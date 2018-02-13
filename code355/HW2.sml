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
zip[1,2,3] ["one", "two"];

fun map f [] = []
    | map f (x::rest) = (f x)::(map f rest);

fun foldL f base [] = base
    | foldL f base (x::rest) = f x (foldL f base rest);

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

(*
Problem 2 deepSum and deepSumOpion
*)

fun deepSum [] = 0 (*base case of empty list*)
    | deepSum list = foldL (fn x=> fn y=> x+y) 0 (map (foldL (fn a => fn b => a+b) 0) list);
    (*inner fold works like addup from slides and gets mapped to each of the lists, then the outer fold performs the final summing *)

deepSum [[1,2,3],[4,5],[6,7,8,9],[]];
deepSum [[10,10],[10,10,10],[10]];
deepSum [[]];
deepSum [];
(*
Problem 3  eitherTree/ Either search
*)

(*
Problem 4 unzip*)

fun unzip l = 
  case l
    of nil => (nil, nil)
     | (a,b)::tl => 
        let val (l1, l2) = unzip tl
        in (a::l1, b::l2) end;

fun unzip2 [] = ([], [])
  | unzip2 ((x,y)::xys)  =
      let val (xs,ys) = unzip2 xys in (x::xs,y::ys) end;

unzip (zipTail [1,2,3] ["one", "two"]);
unzip2 (zipTail [1,2,3] ["one", "two"]);

(*
Problem 5 findMin/FindMax/minMaxTree
*)



(*TEST ZONE*)