# Full Adder Circuit Simulator 

This is a simple Python-based logic circuit simulator for a **Full Adder**.  
The program allows the user to input the state of A, B, and Carry-in (`Cin`), and calculates the **Sum** and **Carry-out** outputs accordingly.

It also automatically generates the complete **Truth Table** for a Full Adder and saves it in a CSV file named `FAtruthTable.csv`.

---

## Features

- Command-line interaction: Input `y`/`n` for logical states  
- Class-based design using Python OOP  
- Custom XOR logic  
- Complete truth table generation (8 combinations)  
- Exports truth table as CSV for further use  

---

## Input

You will be prompted to enter the state (`y` for active / `n` for inactive) of:

- Input A  
- Input B  
- Carry-in (Cin)  

---

## Output

- Logical `Sum` and `Carry-out` values based on Full Adder logic  
- CSV file containing all 8 possible input combinations and their respective outputs  

Example output:  The sum of this circuit is 1 and the Carry-out of the circuit is 0

---


## Generated File

**FAtruthTable.csv**:
```
0,0,0,0,0
0,0,1,1,0
...
1,1,1,1,1
```

---

## Requirements

- Python 3.x  
(No external libraries required)  

---
## Run the code

```bash
python logicSimulator.py
```

---

Author: Tina Tavakolifar
https://github.com/tinatavakolifar

---