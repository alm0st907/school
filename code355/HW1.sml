(*
Garrett Rudisill
WSU ID 11461816
HW 1 for CptS 355
*)

(*inList problem*)
val list = [1,2,3,4,5,6];
val strings = ["a","b","c"];
val list_length = List.length list;
val problemData = (1,list);
val temp = List.nth (list,5); (* accesses the list value at n+1 position since they're 0 based*)
val temp2= List.nth (list,4); (* I can use nth to iterate through list values recursively*)
val pos = 0;

fun inList (ck,vallist) =
    if ck = List.nth (vallist,pos) then true
    else if pos+1 = List.length vallist then pos = 0
    else if pos+1 = List.length vallist then false
    else if pos+1 < List.length vallist then pos = pos +1
    else inList(ck,vallist);

inList(7,list);
inList("a",strings);

(*remove duplicates problem*)

val rmd = [1,2,3,3,4];

(*fun duplicates dup_list = *)
