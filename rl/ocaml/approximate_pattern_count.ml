open Core.Std
open Printf

let rec hamming_distance str1 str2 =
  let len = String.length str1 in 
  if len = 0 then 0
  else if len = 1 then (if str1.[0] <> str2.[0] then 1 else 0)
  else
    let substr1 = String.sub str1 ~pos:1 ~len:(len-1) in
    let substr2 = String.sub str2 ~pos:1 ~len:(len-1) in
    (if str1.[0] <> str2.[0] then 1 else 0) + (hamming_distance substr1 substr2)    
       
let approx_count pattern genome tolerance =
  let glen = String.length genome in
  let plen = String.length pattern in

  let rec approx_count_impl idx count = 
    if idx > (glen-plen) then count
    else
      let candidate = String.sub genome ~pos:idx ~len:plen in
      let distance = hamming_distance candidate pattern in
      approx_count_impl (idx+1)
        (if (distance <= tolerance) then (count+1) else count)
  in
  approx_count_impl 0 0
    

let () =
  let pattern = "TGT" in
  let genome = "CGTGACAGTGTATGGGCATCTTT" in
  let tolerance = 1 in
  let count = approx_count pattern genome tolerance in
  printf "%d \n" count ;
  

  (* let file = "Downloads/dataset_9_6.txt" in *)
  (* let lines = In_channel.read_lines file in *)
  (* let pattern = *)
  (*   match (List.nth lines 0) with *)
  (*   |  Some line -> String.strip line *)
  (*   | _ -> raise (Invalid_argument "could not read pattern") *)
  (* in *)
  (* let genome = *)
  (*   match (List.nth lines 1) with *)
  (*   | Some line -> String.strip line *)
  (*   | _ -> raise (Invalid_argument "could not read genome") *)
  (* in *)
  (* let tolerance = *)
  (*   match (List.nth lines 2) with *)
  (*   | Some line -> int_of_string (String.strip line) *)
  (*   | _ ->raise (Invalid_argument "could not read tolerance") *)
  (* in *)
  (* let count = approx_count pattern genome tolerance in *)
  (* printf "%d\n" count; *)
