# Week 2 - Tutorial 2

## 1. Identify the Components

### 1.1. What are the inputs?
* `age` (Integer)
* `is_accompanied` (Boolean: True/False)
* `has_ticket` (Boolean: True/False)

### 1.2. What is the process?
1. Check if `age >= 13` OR `is_accompanied == True`.
2. Take that result and check if it is True **AND** `has_ticket == True`.

### 1.3. What is the output?
* `is_allowed_entry` (Boolean: True/False)

---

## 2. Design the Algorithm

### 2.1. Logic Diagram Text representation
* Inputs `Age >= 13` and `Accompanied` connect to an **OR** gate.
* The output of the **OR** gate and `Has Ticket` connect to an **AND** gate.

### 2.2. Truth Table
| A (Age >= 13) | B (Accompanied) | C (Has Ticket) | A OR B | (A OR B) AND C (Output) |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | **0 (Denied)** |
| 0 | 0 | 1 | 0 | **0 (Denied)** |
| 0 | 1 | 0 | 1 | **0 (Denied)** |
| 0 | 1 | 1 | 1 | **1 (Allowed)** |
| 1 | 0 | 0 | 1 | **0 (Denied)** |
| 1 | 0 | 1 | 1 | **1 (Allowed)** |
| 1 | 1 | 0 | 1 | **0 (Denied)** |
| 1 | 1 | 1 | 1 | **1 (Allowed)** |

### 2.3. Design an Algorithm
1. Start.
2. Input `age`, `is_accompanied`, `has_ticket`.
3. IF (`age` >= 13 OR `is_accompanied` == True) AND `has_ticket` == True THEN:
* Set `status` = "Allowed to enter"
ELSE:
* Set `status` = "Denied entry"
4. Output `status`.
5. End.

### 2.4. Create Pseudocode
```text
BEGIN
READ age, is_accompanied, has_ticket
IF (age >= 13 OR is_accompanied == TRUE) AND has_ticket == TRUE THEN
DISPLAY "Admission Allowed"
ELSE
DISPLAY "Admission Denied"
ENDIF
END

