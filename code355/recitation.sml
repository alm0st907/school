fun numTosum (num:int) list = 
    if (List.null list) = true then []
    else List.hd list::[];

numTosum 1 [2];

(*)
fun replace index replace list =
    if index <> 0 then (List.hd list)::replace (index-1) replace list
    else if index = 0 then replace:: *)
    

fun replace i v [] = []
    | replace 0 v (x::xs) = v::xs
    | replace i v (x::xs) = if i < 0 then [] else x::replace (i-1) v xs;


replace ~3 40 [1, 2, 3, 4, 5, 6];
replace 0 "X" ["a", "b", "c", "c", "d"];
replace 4 false [true, false, true, true, true];
