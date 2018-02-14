
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


(*
notes for 2-13

Turing machine -> natural set of problems
church -> create variables
        create functions
        apply functions

        total functions [ [partial functions()computable functions]]


tuples are 1 index'd

accessing sub tuple

#3 (#2 (1, (2,4,6,8,10), "true"));

returns 6,  #2 grabs the tuple within the tuple, #3 grabs the third element which is 6

fun b (x::y) = x^y;
fn b = fn: string list -> string


foldL can be tail recursive but might not be

if any part of a function is not tail recursive then the whole thing is immediately not

*)

(*

(true, [[false]], "true", ([1],[2,3]))
bool * bool list list * string * (int list * int list) is the type of this tuple

*)