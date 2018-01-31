
fun numbersToSum desSum L = 
    let
      fun addup [] = 0
        | addup (x::rest) = (x + addup rest)
    in   
        if ((addup L) < desSum andalso L <> []) then L
        else if (addup L>= desSum) then numbersToSum desSum (rev(tl(rev L)))
        else []
    end;
(*
numbersToSum 21 [5,5,5,5];
numbersToSum 20 [5,5,5,5];
numbersToSum 25 [5,2,3,10,4,1];
numbersToSum 24 [5,2,3,10,4,1,1];
*)

numbersToSum 100 [10, 20, 30, 40];
numbersToSum 30 [5, 4, 6, 10, 4, 2, 1, 5];
numbersToSum 1 [2];
numbersToSum 1 [];

val testlist = [10, 20, 30, 40];
val testlist = (rev((tl(rev testlist))));