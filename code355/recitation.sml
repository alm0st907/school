(*this is code from the recitation*)
(*
lists can be of varying size but must be of same type

tuples have static size of <maybe> different types

# notation for tuples are 1 base indexed

unless val goes before, = is just equivalence operator



0, 1, few, many, oops
                    boundaries,negative number
*)


(* 1-26 class code*)

fun addUp []= 0 (*setting return type in this case also sets what happens if empty list passed in*)
    |addUp(x::rest)= x+addUp (rest);

(*pass in a tuple of lists*)
fun append ([],L)=L (* lets us set return type, then bar is what is evaluate*)
    |append(x::rest,L) = x::append(rest,L);

fun reverse [] = []
    |reverse(x::rest) = append(reverse (rest),x::[]);
                        (*append (reverse rest,[x]*)

fun revappend ([],L) = L
    | revappend((x::rest),L)= revappend(rest,x::L);
