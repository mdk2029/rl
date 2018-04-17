open Core.Std

let rec read_and_accum accum =
    let line = In_channel.input_line In_channel.stdin in
	match line with
	      | None -> accum
	      | Some x -> read_and_accum (accum +. Float.of_string x)


let string_to_list s =
    Core.Std.String.to_list s

let rec pattern_to_number pattern = 

    let symbol_index s =
	if Char.uppercase s = 'A' then 0
	else if Char.uppercase s = 'C' then 1
	else if Char.uppercase s = 'G' then 2
	else if Char.uppercase s = 'T' then 3
	else raise ( Invalid_argument "foo")
    in
	let plen = String.length pattern in
	    if plen = 0 then 0
	    else
	    	 let prefix = (String.sub pattern 0 (plen-1)) in 
	    	    4 * (pattern_to_number prefix) + (symbol_index pattern.[plen-1])



let res = pattern_to_number "CAT" in
    printf "Index is %d\n" res
							

			  
