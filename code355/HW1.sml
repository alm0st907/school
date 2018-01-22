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
val pos = 0;

fun inList (ck,vallist) =
    if vallist = [] then false
    else if ck = List.nth (vallist,pos) then true
    else inList(ck,List.drop (vallist,1));
    
inList(7,list);
inList(6,list);
inList("a",strings);
inList("d",strings);



(*remove duplicates problem*)

val rmd = [1,2,3,3,4];

fun test list = 
    if inList(7, list) = true then print "Hello World, this is my first SML program!!!"
    else print "false";
    (**)


fun rm_dup list =
    print "compile it";
    val temp = List.drop (list,1);
    val comp = List.nth (list,0);
    val list = comp::temp;

    

rm_dup(rmd);
val test = temp;
val testlist = rmd; (*is returned unmodified*)
val test = comp::temp; (*concat value to beginning of list)*)
val test = test @ [comp]; (*concat list to to end*)

(*somewhat helpful code, just need to clean*)
fun delete(x,[]) = []
    | delete(x,y::l) = if x=y then delete(x,l) else y::delete(x,l);

fun remove_dup [] = []
    | remove_dup (x::l) = x::remove_dup(delete(x,l)); 

remove_dup(test);
remove_dup(rmd);