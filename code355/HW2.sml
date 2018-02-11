(*
Garrett Rudisill
WSU ID 11461816
HW2 for ML
Coded on Ubuntu 17.10/Windows 10 with SMLNJ
*)

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
      fun accum aList bList rest = ()

    in
        zipTail aList bList
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