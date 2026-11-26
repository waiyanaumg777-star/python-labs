# Tutorial 3 – Cafe Billing System Documentation

## 1. Answer the Questions

### 1.1 Problem Statement

A small café sells coffee for RM8.50, tea for RM6.00, and sandwiches for RM12.00. The cashier currently calculates customer bills manually. The problem is that manual calculations can take time and may lead to mistakes. The task is to develop a Python program that accepts the customer's name and the quantities of each item, calculates the bill automatically, and prints a receipt showing the order and total amount.

### 1.2 Inputs

The program requires these inputs from the user:

- Customer name.
- Number of coffees.
- Number of teas.
- Number of sandwiches.

The item quantities must be non-negative whole numbers.

### 1.3 Outputs

The program displays a receipt containing:

- Customer name.
- Coffee quantity.
- Tea quantity.
- Sandwich quantity.
- Total bill in Malaysian Ringgit (RM), formatted to two decimal places.

### 1.4 Typical Process Flow

1. Start the program.
2. Display the café billing system heading.
3. Ask the user to enter the customer's name.
4. Ask for the coffee quantity.
5. Ask for the tea quantity.
6. Ask for the sandwich quantity.
7. Calculate the total using the fixed prices:
   - Coffee: RM8.50 each.
   - Tea: RM6.00 each.
   - Sandwich: RM12.00 each.
8. Print the receipt with the customer's details and total amount.
9. End the program.

### 1.5 Constraints

- The program uses the fixed prices given in the scenario.
- Quantities must be whole numbers (integers).
- Quantities cannot be negative.
- The customer name cannot be blank.
- The total is displayed in RM with two decimal places.
- The program calculates the total only; the scenario does not specify tax, service charges, or discounts.

## 2. Decompose the Problem into Smaller Tasks

The problem can be divided into these smaller tasks:

1. **Collect customer information:** Ask for and validate the customer's name.
2. **Collect order quantities:** Ask for the quantities of coffee, tea, and sandwiches.
3. **Validate quantities:** Ensure each quantity is a non-negative whole number.
4. **Store item prices:** Use the given fixed prices for the three products.
5. **Calculate item costs:** Multiply each quantity by its item price.
6. **Calculate the bill:** Add the three item costs to obtain the total.
7. **Print the receipt:** Display the customer name, quantities, and total bill.
8. **Test the program:** Check the calculation with sample quantities and invalid inputs.

## 3. Pseudocode

```text
BEGIN
    DISPLAY "CAFE BILLING SYSTEM"

    INPUT customer_name
    WHILE customer_name is empty
        DISPLAY "Customer name cannot be empty"
        INPUT customer_name
    END WHILE

    INPUT coffee_quantity
    INPUT tea_quantity
    INPUT sandwich_quantity

    coffee_price = 8.50
    tea_price = 6.00
    sandwich_price = 12.00

    total = (coffee_quantity * coffee_price)
          + (tea_quantity * tea_price)
          + (sandwich_quantity * sandwich_price)

    DISPLAY "===== RECEIPT ====="
    DISPLAY customer_name
    DISPLAY coffee_quantity
    DISPLAY tea_quantity
    DISPLAY sandwich_quantity
    DISPLAY total

END
```

## 4. Python Program

The solution is divided into two Python files:

- **utils.py:** Contains the `calculate_total()` and `print_receipt()` functions.
- **main.py:** Collects and validates user input, calls the functions in `utils.py`, and runs the main program.

Run the program from the `Tutorial_3` folder using:

```bash
python main.py
```

## Sample Test

**Sample input**

```text
Customer name: Bobby
Coffee quantity: 3
Tea quantity: 3
Sandwich quantity: 2
```

**Expected calculation**

- Coffee: 3 × RM8.50 = RM25.50
- Tea: 3 × RM6.00 = RM18.00
- Sandwich: 2 × RM12.00 = RM24.00
- Total: RM25.50 + RM18.00 + RM24.00 = RM67.50

**Expected output**

```text
===== RECEIPT =====
Customer : Bobby
Coffee   : 3
Tea      : 3
Sandwich : 2
-------------------
Total = RM 67.50
```

The expected total matches the sample output provided in the tutorial.

## Conclusion

The café billing program automates the manual bill calculation. It uses separate functions to calculate the total and print the receipt. Separating the tasks into smaller functions makes the program easier to understand, test, and maintain.
