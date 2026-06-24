# Python Business Rules Capstone Project

## Assignment Title
Customer Evaluation, Product Billing, Loan Decision, and Campaign Eligibility System

## Student Details
- Student Name: Abhilash Pandey
- Student ID: 2602008

## Problem Summary
This command-line Python application helps a business team collect customer information, calculate product billing, evaluate loan eligibility, and assign campaign eligibility using business rules.

## Features Implemented
- Customer profile and financial summary
- Product billing calculator
- Loan eligibility decision with reason
- Campaign eligibility with reason
- Menu-driven program that runs until exit
- Input validation and error handling
- Multi-file Python structure using the `src/` folder

## Business Rules Used
### Risk Category
- Low Risk: credit score at least 750, savings percentage at least 25, and EMI-to-income ratio at most 25.
- Medium Risk: credit score at least 650, savings percentage at least 10, and EMI-to-income ratio at most 40.
- High Risk: all remaining cases.

### Customer Value Category
- High Value: monthly income at least 150000, or Enterprise segment with savings percentage at least 20.
- Medium Value: monthly income at least 60000, or Premium segment.
- Low Value: all remaining cases.

### Billing Rules
- Gross amount = quantity × unit price.
- Discount amount = gross amount × discount percentage.
- GST is calculated on amount after discount.
- Delivery charge is waived when amount after discount is above the threshold constant of 5000.

### Loan Eligibility Rules
- Rejected if age is below 21.
- Approved if credit score is at least 750, savings percentage is at least 20, and projected EMI ratio is at most 40.
- Manual Review Required if credit score is at least 650, savings percentage is at least 10, and projected EMI ratio is at most 55.
- Rejected in all other cases.

### Campaign Rules
- Premium Upsell Campaign: Premium segment and High Value customer.
- Cashback Campaign: target city customer with savings percentage at least 15.
- Loan Offer Campaign: Medium Value or High Value customer not matched earlier.
- No Campaign: all remaining cases.

## File Structure Explanation
- `main.py`: controls the menu and calls feature functions.
- `src/customer.py`: handles customer input, summary calculations, and risk/value rules.
- `src/billing.py`: handles product billing logic.
- `src/eligibility.py`: handles loan and campaign decisions.
- `src/utils.py`: validation helpers, formatting helpers, and constants.
- `outputs/sample_output.txt`: contains one complete sample run.
- `tests/test_cases.md`: contains at least 10 test cases.

## How to Run the Program
1. Open the project folder in VS Code or terminal.
2. Run the command: `python main.py`
3. Choose a menu option and enter the required values.
4. Continue using the menu until you choose Exit.

## Sample Input and Output

A full sample run covering all four features and invalid-input handling is in
`outputs/sample_output.txt`.

Example — Customer Profile and Financial Summary (Feature 1):

\`\`\`
Enter customer name: Rohan Mehta
Enter age: -5
  -> Invalid input. Value must be between 1 and 120. Please try again.
Enter age: 30
...
Monthly Savings      : Rs. 40,000.00
Savings Percentage   : 50.00%
EMI-to-Income Ratio  : 12.50%
Risk Category        : Low Risk
Customer Value       : Medium Value
\`\`\`

See `outputs/sample_output.txt` for the complete run across all 4 menu options.

## Screenshots

**Feature 1 — Customer Profile and Financial Summary**
![Customer Profile](outputs/screenshots/screenshot_1_customer_profile.png)

**Feature 2 — Product Billing Calculator**
![Billing Calculator](outputs/screenshots/screenshot_2_billing.png)

**Feature 3 — Loan Eligibility Decision**
![Loan Decision](outputs/screenshots/screenshot_3_loan_approved.png)

## Assumptions Made
- Loan EMI projection is estimated as requested loan amount divided by 24 months.
- Only Standard, Premium, and Enterprise are valid customer segments.
- Cashback target cities are Lucknow, Delhi, Mumbai, Bangalore, and Hyderabad.
- Delivery waiver threshold is stored as a constant in the code.
