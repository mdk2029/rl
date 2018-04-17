open Core.Std

let rec hamming_distance str1 str2 =
  let len = String.length str1 in 
  if len = 0 then 0
  else if len = 1 then (if str1.[0] <> str2.[0] then 1 else 0)
  else
    let substr1 = String.sub str1 1 (len-1) in
    let substr2 = String.sub str2 1 (len-1) in
    (if str1.[0] <> str2.[0] then 1 else 0) + (hamming_distance substr1 substr2)    


let str1 = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG" in
let str2 = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT" in
let d = hamming_distance str1 str2 in
printf "%d\n" d

(* let () = *)
(*   let file = "Downloads/dataset_9_3.txt" in *)
(*   let lines = In_channel.read_lines file in *)
(*   let input1 = *)
(*     match List.nth lines 0 with *)
(*     | Some line -> String.strip line *)
(*   in *)
(*   let input2 = *)
(*     match List.nth lines 1 with *)
(*     | Some line -> String.strip line *)
(*   in *)
(*   printf "%d\n" (hamming_distance input1 input2) *)


    
