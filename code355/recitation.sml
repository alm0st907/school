fun numTosum (num:int) list = 
    if (List.null list) = true then []
    else List.hd list::[];

numTosum 1 [2];

(*)
fun replace index replace list =
    if index <> 0 then (List.hd list)::replace (index-1) replace list
    else if index = 0 then replace:: *)
    

fun change(i,v,[]) = []
    | change(0, v, x::xs) =  v :: xs
    | change(i, v, x::xs) =  if i < 0 then []
                            else  x :: change((i-1), v, xs);
