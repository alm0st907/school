(*
Garrett Rudisill
WSU ID 11461816
HW 1 for CptS 355

Ran on ubuntu 17.10 using SMLNJ
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
        rev(help(L1, L2, [])) (*reverse our final results*)
    end;
    

(*Range problem*)
(*recursively adding to the list based on condition
x is start point, y is the increment, and z is the condition x must be less than.
we add x to the output, then continually add x+y while x+y<z, or >z if a negative being added and we decrement
*)
fun range (x:int) (y:int) (z:int) =
    if x = z then []
    else if y<0 andalso (x<=z) then []
    else if y>0 andalso ((x+y)>=z) then x::[]
    else if y<0 andalso ((x+y)<=z) then x::[] 
    else (x::range (x+y) y z);

(*NUMBERS TO desSum*)
(* take in the desired sum and a list of numbers
   returns a list of numbers, such that n elements of the list are < desired sum, but n+1 elements would be the sum *)
fun numbersToSum desSum L = 
    let
      fun addup [] = 0
        | addup (x::rest) = (x + addup rest)
    in   
        if ((addup L) < desSum andalso L <> []) then L (* the list is already the answer*)
        else if (addup L>= desSum) then numbersToSum desSum (rev(tl(rev L))) (*recursively trim our list*)
        else [] (*otherwise return an empty list*)
    end;

(*replace problem*)
(*we iterate through the list until i=0, while i>0, append what is in the original list, but when i=0, append the value v to replace it, then we continue to append the rest of the original list*)
fun replace i v [] = []
    | replace 0 v (x::rest) = v::rest
    | replace i v (x::rest) = if i < 0 then [] else x::replace (i-1) v rest;

(*group left/right problems*)
(* these functions group N elements of L list together, and returns a list of lists*)
(*uses pattern matching to handle the cases of input*)

fun groupNleft N L =
    let
      fun grouping i [] [] = [[]] 
        | grouping i (thiscur :: thisrest) [] = [[]] 
        | grouping i [] (thiscur :: thisrest) = thiscur :: thisrest
        | grouping i (thatcur :: thatrest) (thiscur :: thisrest) = 
            if i > 0
              then grouping (i - 1) thatrest ((thatcur :: thiscur) :: thisrest)
              else grouping N (thatcur :: thatrest) ([] :: thiscur :: thisrest)
    in
      if N > 0
        then grouping N (List.rev(L)) [[]]
        else [[]]
    end;

fun groupNright N L =
    let
      fun grouping i [] [] = [[]] 
        | grouping i (thiscur :: thisrest) [] = [[]] 
        | grouping i [] (thiscur :: thisrest) = List.rev (thiscur) :: thisrest
        | grouping i (thatcur :: thatrest) (thiscur :: thisrest) = 
            if i > 0
              then grouping (i - 1) thatrest ((thatcur :: thiscur) :: thisrest)
              else grouping N (thatcur :: thatrest) ([] :: List.rev(thiscur) :: thisrest)
    in
      if N > 0
        then List.rev (grouping N L [[]])
        else [[]]
    end;
  

(* testing area*)

fun inListTest () =
    let
        val inListT1 = ( inList(8,[7]) = false )
        val inListT2 = ( inList("one",["two","one"]) = true )
        val inListT3 = ( inList(true,[false,false]) = false )
        val inListT4 = ( inList(false,[]) = false)
        val inListT5 = ( inList(1,[]) = false)
        val inListT6 = ( inList("a",[]) = false)
        val inListT7 = ( inList(8,[7,9,10]) = false )
    in
        print ("\n------------- \n inList:\n" ^
        "test1: " ^ Bool.toString(inListT1) ^ "\n" ^
        "test2: " ^ Bool.toString(inListT2) ^ "\n" ^
        "test3: " ^ Bool.toString(inListT3) ^ "\n" ^
        "test4: " ^ Bool.toString(inListT4) ^ "\n" ^
        "test5: " ^ Bool.toString(inListT5) ^ "\n" ^
        "test6: " ^ Bool.toString(inListT6) ^ "\n" ^
        "test7: " ^ Bool.toString(inListT7) ^ "\n" )

    end;
val _ = inListTest();

fun removeDuplicatesTest() =
    let
	val test1 = (removeDuplicates([1,2,3,4,5]) = [1,2,3,4,5])
	val test2 = (removeDuplicates([1,1,2,2,1,1,2,2,1]) = [1,2])
	val test3 = (removeDuplicates([12, 12, 12, 12, 12, 12, 12]) = [12])
	val test4 = (removeDuplicates([~100, 50, 60, 75645, ~100, 23, 74, 60]) = [~100, 50, 60, 75645, 23, 74])
	val test5 = (removeDuplicates([]) = [])
    in
	print("\n----------------\nremoveDuplicatesTest:\n" ^
              "test1: " ^ Bool.toString(test1) ^ "\n" ^
	      "test2: " ^ Bool.toString(test2) ^ "\n" ^
	      "test3: " ^ Bool.toString(test3) ^ "\n" ^
	      "test4: " ^ Bool.toString(test4) ^ "\n" ^
	      "test5: " ^ Bool.toString(test5) ^
	      "\n----------------\n")
    end;

val _ = removeDuplicatesTest();

fun listIntersectTest() =
    let
	val test1 = (listIntersect ([1],[1])) = [1]
	val test2 = (listIntersect ([1,2,3],[1,1,2])) = [1,2]
	val test3 = (listIntersect ([[2,3],[1,2],[2,3]],[[1],[2,3]])) = [[2,3]]
	val test4 = (listIntersect ([],[[1,4,5],[2,3,6]])) = []
	val test5 = (listIntersect (["a","a","b","b"],["a","b","c","a","b","c"])) = ["a","b"]
    in
	print("\n----------------\nlistIntersectTest:\n" ^
              "test1: " ^ Bool.toString(test1) ^ "\n" ^
	      "test2: " ^ Bool.toString(test2) ^ "\n" ^
	      "test3: " ^ Bool.toString(test3) ^ "\n" ^
	      "test4: " ^ Bool.toString(test4) ^ "\n" ^
	      "test5: " ^ Bool.toString(test5) ^
	      "\n----------------\n")
    end;

val _ = listIntersectTest();

fun rangeTest() =
    let
	val test1 = (range 0 5 30) = [0,5,10,15,20,25]
	val test2 = (range 10 1 10) = []
	val test3 = (range 5 ~1 0) = [5,4,3,2,1]
	val test4 = (range 1 ~1 10) = []
	val test5 = (range 10 ~10 0) = [10]
    in
	print("\n----------------\nrangeTest:\n" ^
            "test1: " ^ Bool.toString(test1) ^ "\n" ^
	      "test2: " ^ Bool.toString(test2) ^ "\n" ^
	      "test3: " ^ Bool.toString(test3) ^ "\n" ^
	      "test4: " ^ Bool.toString(test4) ^ "\n" ^
	      "test5: " ^ Bool.toString(test5) ^
	      "\n----------------\n")
    end;

val _ = rangeTest();

fun numbersToSumTest() =
    let
	val test1 = (numbersToSum 100 [10, 20, 30, 40] = [10,20,30])
	val test2 = (numbersToSum 30 [5, 4, 6, 10, 4, 2, 1, 5] = [5,4,6,10,4])
	val test3 = (numbersToSum 1 [2] = [])
	val test4 = (numbersToSum 1 [] = [])
	val test5 = (numbersToSum 5 [1,1,1,1,1] = [1,1,1,1])
    in
	print("\n----------------\nnumbersToSumTest:\n" ^
              "test1: " ^ Bool.toString(test1) ^ "\n" ^
	      "test2: " ^ Bool.toString(test2) ^ "\n" ^
	      "test3: " ^ Bool.toString(test3) ^ "\n" ^
	      "test4: " ^ Bool.toString(test4) ^ "\n" ^
	      "test5: " ^ Bool.toString(test5) ^
	      "\n----------------\n")
    end;

val _ = numbersToSumTest();

fun replaceTest() =
    let
	val test1 = (replace 3 40 [1, 2, 3, 4, 5, 6]) = [1,2,3,40,5,6]
	val test2 = (replace 0 "X" ["a", "b", "c", "d"]) = ["X","b","c","d"]
	val test3 = (replace 4 false [true, false, true, true, true]) = [true,false,true,true,false]
	val test4 = (replace 0 20 [7]) = [20]
	val test5 = (replace 0 "X" ["a", "b", "c", "d"]) = ["X","b","c","d"]
    in
	print("\n----------------\nreplaceTest:\n" ^
              "test1: " ^ Bool.toString(test1) ^ "\n" ^
	      "test2: " ^ Bool.toString(test2) ^ "\n" ^
	      "test3: " ^ Bool.toString(test3) ^ "\n" ^
	      "test4: " ^ Bool.toString(test4) ^ "\n" ^
	      "test5: " ^ Bool.toString(test5) ^
	      "\n----------------\n")
    end;

    val _ = replaceTest();

    fun groupNrightTest() =
    let
	val test1 = (groupNright 2 [1, 2, 3, 4, 5]) = [[1, 2], [3, 4], [5]]
	val test2 = (groupNright 3 [1, 2, 3, 4, 5]) = [[1, 2, 3], [4, 5]]
	val test3 = (groupNright 3 ["phrase", "other", "words", "a", "b", "Z", "X"]) = [["phrase", "other", "words"], ["a", "b", "Z"], ["X"]]
	val test4 = (groupNright 5 []) = [[]]
	val test5 = (groupNright 2 [0, 0, 1, 1]) = [[0, 0], [1, 1]]
    in
	print("\n----------------\ngroupNrightTest:\n" ^
              "test1: " ^ Bool.toString(test1) ^ "\n" ^
	      "test2: " ^ Bool.toString(test2) ^ "\n" ^
	      "test3: " ^ Bool.toString(test3) ^ "\n" ^
	      "test4: " ^ Bool.toString(test4) ^ "\n" ^
	      "test5: " ^ Bool.toString(test5) ^
	      "\n----------------\n")
    end;

val _ = groupNrightTest();

fun groupNleftTest() =
    let
	val test1 = (groupNleft 2 [1, 2, 3, 4, 5]) = [[1], [2, 3], [4, 5]]
	val test2 = (groupNleft 3 [1, 2, 3, 4, 5]) = [[1, 2], [3, 4, 5]]
	val test3 = (groupNleft 1 [1, 2, 3, 4, 5]) = [[1], [2], [3], [4], [5]]
	val test4 = (groupNleft 5 ["a", "b", "c", "d", "e"]) = [["a", "b", "c", "d", "e"]]
	val test5 = (groupNleft 7 [0, 1, 2, 3, 4, 5, 6, 7]) = [[0], [1, 2, 3, 4, 5, 6, 7]]
    in
	print("\n----------------\ngroupNleftTest:\n" ^
              "test1: " ^ Bool.toString(test1) ^ "\n" ^
	      "test2: " ^ Bool.toString(test2) ^ "\n" ^
	      "test3: " ^ Bool.toString(test3) ^ "\n" ^
	      "test4: " ^ Bool.toString(test4) ^ "\n" ^
	      "test5: " ^ Bool.toString(test5) ^
	      "\n----------------\n")
    end;

val _ = groupNleftTest();