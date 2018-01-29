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