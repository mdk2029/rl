open Core.Std
open Printf

let skew pattern skewArray  =
  let plen = Array.length skewArray in
  for i = 0 to (plen - 2) do
    if Char.uppercase pattern.[i] = 'G' then
      skewArray.(i+1) <- skewArray.(i) + 1
    else if Char.uppercase pattern.[i] = 'C' then
      skewArray.(i+1) <- skewArray.(i) - 1
    else
      skewArray.(i+1) <- skewArray.(i)
  done

let main pattern =
  let skewArray = Array.create (String.length pattern + 1) 0 in
  begin
    skew pattern skewArray;
    let min = Array.fold ~init:(skewArray.(0)) ~f:(min) skewArray in
    let indices = Array.foldi ~init:[] ~f:(fun idx list x -> if x = min then list @ [idx] else list) skewArray in
    begin
      List.iter ~f:(printf "%d ") indices;
      printf "\n"
    end
  end

let maxskew pattern =
  let skewArray = Array.create (String.length pattern + 1) 0 in
  begin
    skew pattern skewArray;
    let max = Array.fold ~init:(skewArray.(0)) ~f:(max) skewArray in
    let indices = Array.foldi ~init:[] ~f:(fun idx list x -> if x = max then list @ [idx] else list) skewArray in
    begin
      List.iter ~f:(printf "%d ") indices;
      printf "\n"
    end
  end

(* let () = *)
(*   let file = "Downloads/dataset_7_6.txt" in *)
(*   let lines = In_channel.read_lines file in *)
(*   match (List.nth lines 0) with *)
(*   |  Some line -> main line *)
(*   |  _ -> printf "Unexpected input\n"; () *)


let () =
  maxskew "CATTCCAGTACTTCATGATGGCGTGAAGA"

					    

	    
	    
