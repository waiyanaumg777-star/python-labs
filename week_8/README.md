# Week 8 – Tutorial 8: Food Delivery System

## 1. Purpose of the Application

This project is a small Python backend component for a food delivery system. It collects customer and order information, calculates the subtotal, adds a 5% service charge, applies a RM5.00 delivery charge when delivery is selected, and prints a receipt.

The program separates responsibilities into modules so that customer input, receipt calculation, and the main application are easier to understand and maintain.

## 2. Tech Stack

- Python 3
- Python modules and functions
- Command-line input and output
- Visual Studio Code / GitHub Codespaces

## 3. Project Files

- `main.py`: Main application that connects the customer and receipt modules.
- `app.py`: Alternative entry point included to match the activity section's reference to an application module named app.py.
- `customer.py`: Collects and validates the customer's name, food choice, quantity, item price, and delivery choice.
- `receipt.py`: Calculates subtotal, 5% service charge, delivery charge, and grand total, then prints the receipt.

## 4. How to Use

1. Open a terminal in the `week_8` folder.
2. Run the application:

   ```bash
   python main.py
   ```

   Alternatively, run `python app.py`.

3. Enter the customer name.
4. Choose Cake or Muffin.
5. Enter a positive whole-number quantity.
6. Enter the item price in RM.
7. Enter Y for delivery or N for no delivery.
8. Read the printed receipt.

## 5. Calculation Rules

- Subtotal = quantity × price per item.
- Service charge = subtotal × 5%.
- Delivery charge = RM5.00 when the customer selects Y; otherwise RM0.00.
- Grand total = subtotal + service charge + delivery charge.

## 6. Example Demonstration

Example inputs:

- Customer name: izzad
- Food: Cake
- Quantity: 2
- Price per item: RM3.00
- Delivery: Y

Expected calculations:

- Subtotal = 2 × RM3.00 = RM6.00
- Service charge = RM6.00 × 5% = RM0.30
- Delivery charge = RM5.00
- Grand total = RM6.00 + RM0.30 + RM5.00 = RM11.30

Expected final line:

```text
TOTAL    : RM 11.30
```

## 7. Screen Recording Demonstration

The tutorial asks for a screen recording in video or GIF format. To create it:

1. Open the `week_8` folder in GitHub Codespaces.
2. Open the terminal and run `python main.py`.
3. Enter the example inputs listed above.
4. Record the terminal while entering the values and showing the completed receipt.
5. Save the recording as a video or GIF and submit it using the method specified by the lecturer.

The recording is not included in this repository yet; it must be captured by the student.

## 8. Conclusion

The application demonstrates modular programming in Python. The customer module handles input and validation, the receipt module performs the calculations and displays the receipt, and the main module coordinates the application. This structure makes each part easier to test, update, and maintain.
