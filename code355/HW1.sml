(*
Garrett Rudisill
WSU ID 11461816
HW 1 for CptS 355
*)


(*
TODO
comments, testing
*)

(*inList code*)
(*This function takes in a tuple with a comparing value, and a list to find it in*)
(*the type is ''a * ''a list because it is templated for any comparable type, with a list of comparable types*)
fun inList (ck,vallist) =
    if vallist = [] then false
    else if ck = List.hd vallist then true
    else inList(ck,List.tl vallist);

(*remove duplicates*)
(*using built in filter function, to filter for checking if a item is in the list. We only add to the list if not*)
fun removeDuplicates [] = []
    | removeDuplicates(x::rest) = x::removeDuplicates(List.filter (fn y => y <>x)rest);

(* listIntersect problem*)
(* this function will return a list of common items between the two inputs
By using inList we test for the element being in both input lists, and not in the output already, we then add it to the output list
*)
fun listIntersect(L1, L2) =
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
(*recursively adding to the list based on condition
x is start point, y is the increment, and z is the condition x must be less than.
we add x to the output, then continually add x+y while x+y<z, or >z if a negative being added and we decrement
*)
fun range (x:int) (y:int) (z:int) =
    if y>0 andalso ((x+y)>=z) then x::[]
    else if y<0 andalso ((x+y)<=z) then x::[]
    else (x::range (x+y) y z);

(*NUMBERS TO desSum*)
fun numbersToSum desSum L = 
    let
    	fun num2sumHelp(desSum, [], curSum, newList) = newList
	| num2sumHelp(desSum, x::rest, curSum, newList) = 
		(if curSum+x >= desSum then newList    (* checking if the current sum is < desired sum *)
		else num2sumHelp(desSum, rest, curSum+x, rev(x::rev(newList))))
    in
	num2sumHelp(desSum, L, 0, [])        (* 0 works only for positive numbers *)
    end;

(*replace problem*)
(*we iterate through the list until i=0, while i>0, append what is in the original list, but when i=0, append the value v to replace it, then we continue to append the rest of the original list*)
fun replace i v [] = []
    | replace 0 v (x::rest) = v::rest
    | replace i v (x::rest) = if i < 0 then [] else x::replace (i-1) v rest;

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
  