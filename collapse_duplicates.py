import os
from os import listdir

fpin = "NOCC/inputs/"
fpout = "NOCC/outputs/"

index = 0
inputs = os.listdir(fpin)
for file in inputs:
    input_fn = fpin + file
    output_fn = fpout + file
    
    prev_id = None
    prev_row = None
    row_out = []
    with open(input_fn, "r") as fin, open(output_fn, "w") as fout:
        for line in fin:
            curr_row = line.split('\t')
            curr_id = curr_row[index]
            if prev_id == curr_id:
                new_row = []
                for i, el in enumerate(curr_row):
                    if i != index:
                        calc = float(prev_row[i]) + float(curr_row[i])
                        if calc == 0:
                            calc = int(0)
                        new_row.append(str(calc))
                    else:
                        new_row.append(curr_row[i])
                prev_row = new_row
                prev_row.append("\n")
            else:
                if prev_row:
                    fout.write("\t".join(prev_row))
                prev_row = curr_row
            
            prev_id = curr_id

    fin.close()
