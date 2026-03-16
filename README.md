# Ice Cream Flavor Counter 

## Description

This Python program asks the user to choose an ice cream flavor multiple times and counts how many times each flavor is selected.
The available flavors are **vainilla**, **chocolate**, and **fresa**.

The program runs a loop **5 times**, asking the user to enter a number corresponding to the flavor they want. After all inputs are collected, the program prints the total number of orders for each flavor.

---

## How It Works

1. Three variables are initialized to store the number of orders for each flavor:

   * `vainilla`
   * `chocolate`
   * `fresa`

2. A `for` loop runs **5 times** to simulate 5 ice cream orders.

3. During each iteration, the user is asked to enter a number:

   * `1` → vainilla
   * `2` → chocolate
   * `3` → fresa

4. The program checks the input using `if`, `elif`, and `else` statements:

   * If the user selects **1**, the `vainilla` counter increases.
   * If the user selects **2**, the `chocolate` counter increases.
   * If the user selects **3**, the `fresa` counter increases.
   * If the user enters an invalid number, an error message is displayed.

5. After the loop finishes, the program prints the total number of selections for each flavor.

---

## Example

Input from user:

```
1
2
3
1
2
```

Output:

```
numero de pedido por sabor:
vainilla: 2
chocolate: 2
fresa: 1
```

---

## Requirements

* Python 3.x

---

## How to Run

1. Save the file as `heladeria.py`
2. Open a terminal in the same folder.
3. Run the program:

```
python heladeria.py
```

---

## Author

Student project for learning basic Python concepts such as:

* Variables
* Loops (`for`)
* Conditional statements (`if`, `elif`, `else`)
* User input
*