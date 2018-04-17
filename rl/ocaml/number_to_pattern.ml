open Core.Std

let rec number_to_pattern num plen pattern = 

  let symbol_at_idx idx =
    if idx = 0 then 'A'
    else if idx = 1 then 'C'
    else if idx = 2 then 'G'
    else if idx = 3 then 'T'
    else raise (Invalid_argument "foo")

  in

  if plen = 0 then pattern 
  else
    let q = num / 4 in
    let r = num % 4 in
    let s = symbol_at_idx r in 
    number_to_pattern q (plen-1) (String.of_char s) ^ pattern

let pat = number_to_pattern 19 3 "" in 
printf "%s\n"  pat

    
    
    
	
