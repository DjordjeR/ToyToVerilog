# ToyoVerilogSimple
Simple program that converts asm to verilog file, that can be included.
This was created in order to avoid manually typing and coping the code
from asm to verilog friendly format. This program is not finished, it works
but has little to no error handling. It is to be used carefully and please
double check if everything is okay. For me worked fine, but it might not be
true for everyone.

## Usage
```
python3 toytoverilog.py

Enter filename with extension:test.asm
Your code
-----------------------
81FF
90FE
C115
91FF
C010
0000
-----------------------
File has been created : output.v
-----------------------
Bye!

```
