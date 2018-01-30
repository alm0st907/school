(*
Garrett Rudisill
WSU ID 11461816
HW 1 for CptS 355
*)


(*
TODO
NUMBERS2SUM

*)

(*inList code*)
fun inList (ck,vallist) =
    if vallist = [] then false
    else if ck = List.hd vallist then true
    else inList(ck,List.tl vallist);

(*remove duplicates*)
fun removeDuplicates [] = []
    | removeDuplicates(x::xs) = x::removeDuplicates(List.filter (fn y => y <>x)xs);

(*list intersection problem*)
fun intersection(L1, L2) =
    let
      fun help(L1, [], result) = result 
        | help([], L2, result) = result 
        | help(cur :: rest, L2, result) =
            if inList(cur, L2)
            andalso inList(cur, result) = false
              then help(rest, L2, cur :: result)
              else help(rest, L2, result)
    in
      help(L1, L2, [])
    end;

(*Range problem*)
fun range (x:int) (y:int) (z:int) =
    if y>0 andalso ((x+y)>=z) then x::[]
    else if y<0 andalso ((x+y)<=z) then x::[]
    else (x::range (x+y) y z);

(*replace problem*)
fun replace i v [] = []
    | replace 0 v (x::xs) = v::xs
    | replace i v (x::xs) = if i < 0 then [] else x::replace (i-1) v xs;


(*NUMBERS TO SUM*)

(*group left/right problems*)

fun groupNleft N L =
    let
      fun transfer i [] [] = [[]] 
        | transfer i (dCur :: dRest) [] = [[]] 
        | transfer i [] (dCur :: dRest) = dCur :: dRest
        | transfer i (sCur :: sRest) (dCur :: dRest) = 
            if i > 0
              then transfer (i - 1) sRest ((sCur :: dCur) :: dRest)
              else transfer N (sCur :: sRest) ([] :: dCur :: dRest)
    in
      if N > 0
        then transfer N (List.rev(L)) [[]]
        else [[]]
    end;

fun groupNright N L =
    let
      fun transfer i [] [] = [[]] 
        | transfer i (dCur :: dRest) [] = [[]] 
        | transfer i [] (dCur :: dRest) = List.rev (dCur) :: dRest
        | transfer i (sCur :: sRest) (dCur :: dRest) = 
            if i > 0
              then transfer (i - 1) sRest ((sCur :: dCur) :: dRest)
              else transfer N (sCur :: sRest) ([] :: List.rev(dCur) :: dRest)
    in
      if N > 0
        then List.rev (transfer N L [[]])
        else [[]]
    end;
  