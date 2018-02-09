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

fun countInList list n = 
    let
        fun inList (n,[]) = false
            | inList(n,x::rest) = if n=x then true else inList(n,rest)
            
    in
        if list = [] then 0
        else if inList(n,list)=false then 0 + countInList (tl list) n else 1 + countInList (tl list) n
    end

    (*zipTail - *)

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