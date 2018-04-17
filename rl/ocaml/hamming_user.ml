open Core.Std
open Printf

let rec hamming_distance str1 str2 =
  let len = String.length str1 in 
  if len = 0 then 0
  else if len = 1 then (if str1.[0] <> str2.[0] then 1 else 0)
  else
    let substr1 = String.sub str1 1 (len-1) in
    let substr2 = String.sub str2 1 (len-1) in
    (if str1.[0] <> str2.[0] then 1 else 0) + (hamming_distance substr1 substr2)    
       
let approximate_count pattern genome tolerance =
  let glen = String.length genome in
  let plen = String.length pattern in

  let rec approximate_count_impl idx approximates =
    if idx > (glen-plen) then approximates
    else
      let candidate = String.sub genome idx plen in
      let distance = hamming_distance candidate pattern in
      approximate_count_impl (idx+1) 
        (if (distance <= tolerance) then approximates@[idx] else approximates)
  in
  approximate_count_impl 0 []


let () =
  (* let pattern = "ATTCTGGA" in *)
  (* let genome = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT" in *)

  let file = "Downloads/approximate_match_data" in
  let lines = In_channel.read_lines file in
  let pattern = 
    match (List.nth lines 1) with
    |  Some line -> String.strip line
  in                      
  let genome =
    match (List.nth lines 2) with
    | Some line -> String.strip line
  in
  let approximates = approximate_count pattern genome 5 in
  List.iter ~f:(printf "%d ") approximates;
  printf "\n";



                                    

    

    
