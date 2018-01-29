(*
Garrett Rudisill
WSU ID 11461816
HW 1 for CptS 355
*)

(*TODO*)
(*
NUM2SUM
REPLACE
*)

(*inList problem*)
val list = [1,2,3,4,5,6];
val strings = ["a","b","c"];
val list_length = List.length list;
val problemData = (1,list);

fun inList (ck,vallist) =
    if vallist = [] then false
    else if ck = List.hd vallist then true
    else inList(ck,List.tl vallist);
    
inList(7,list);
inList(6,list);
inList("a",strings);
inList("d",strings);
inList("A",[]);

(*remove duplicates problem*)

val rmd = [1,2,3,3,4];
(*val test = comp::temp; (*concat value to beginning of list)*)*)
(*val test = test @ [comp]; (*concat list to to end*)*)

(*somewhat helpful code, just need to clean*)
fun delete(x,[]) = []
    | delete(x,y::l) = if x=y then delete(x,l) else y::delete(x,l);

fun remove_dup [] = []
    | remove_dup (x::l) = x::remove_dup(delete(x,l)); 

fun remdup [] = []
    | remdup (l as x::xs) = 
        let fun delete (x,[]) = []
            | delete (x, l as y::ys) = if x = y 
                then delete(x,ys) else y::delete(x,ys)
        in
            x::remdup(delete(x,xs))
        end;
    
fun alt_remdup [] = []
    | alt_remdup(x::xs) = x::alt_remdup(List.filter (fn y => y <>x)xs);

remove_dup(rmd);

(*list intersect problem*)
val inter_list = [1,2,3,4,5,7,8,9,10];
val inter_list_2 = [3,4,5,22,2];


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


intersection(inter_list, inter_list_2);


(* range problem*)

fun range (x:int) (y:int) (z:int) =
    if y>0 andalso ((x+y)>=z) then x::[]
    else if y<0 andalso ((x+y)<=z) then x::[]
    else (x::range (x+y) y z);

range 0 5 31;
range ~1 5 30;
range 0 1 30;
range 5 ~1 ~1;
range 5 ~2 ~1;

(*numbers to sum*)

(*replace*)


(*groupNleft group Nright stuff*)
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

val grouptest = groupNleft 2 [1,2,3,4,5];

fun groupNright N L =
    let
      fun transfer i [] [] = [[]] 
        | transfer i (dCur :: dRest) [] = [[]] 
        | transfer i [] (dCur :: dRest) = List.rev (dCur) :: dRest
        | transfer i (sCur :: sRest) (dCur :: dRest) = 
            if i > 0
              then transfer (i - 1) sRest 
                            ((sCur :: dCur) :: dRest)
              else transfer N (sCur :: sRest) 
                            ([] :: List.rev(dCur) :: dRest)
    in
      if N > 0
        then List.rev (transfer N L [[]])
        else [[]]
    end;

groupNright 2 [1,2,3,4,5];
