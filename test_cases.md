# Test Cases

1. Test Case 1  
Input values: Valid customer with age 30, income 80000, expenses 30000, EMI 10000, score 780, segment Premium.  
Expected output or decision: Monthly savings 40000, medium/high customer value, low risk.  
Reason for expected output: Strong credit, good savings, and low EMI ratio satisfy low-risk rules.

2. Test Case 2  
Input values: Valid customer with age 24, income 50000, expenses 30000, EMI 12000, score 680, segment Standard.  
Expected output or decision: Medium risk.  
Reason for expected output: Credit score and savings are acceptable but not strong enough for low risk.

3. Test Case 3  
Input values: Valid customer with age 22, income 25000, expenses 18000, EMI 6000, score 590, segment Standard.  
Expected output or decision: High risk.  
Reason for expected output: Low score and weak savings make the customer high risk.

4. Test Case 4  
Input values: Product quantity 3, unit price 2000, discount 10, GST 18, delivery 120.  
Expected output or decision: Final bill includes discount, GST, and no delivery waiver because discounted amount is 5400 so delivery is waived.  
Reason for expected output: Amount after discount exceeds the waiver threshold.

5. Test Case 5  
Input values: Product quantity 1, unit price 1200, discount 5, GST 18, delivery 100.  
Expected output or decision: Delivery charge applied.  
Reason for expected output: Discounted amount remains below waiver threshold.

6. Test Case 6  
Input values: Customer from Premium segment, high value, savings 30 percent.  
Expected output or decision: Premium Upsell Campaign.  
Reason for expected output: Premium segment and high value match the first campaign rule.

7. Test Case 7  
Input values: Customer from Lucknow, savings 18 percent, medium value.  
Expected output or decision: Cashback Campaign.  
Reason for expected output: City and savings meet cashback campaign rule.

8. Test Case 8  
Input values: Customer age 20.  
Expected output or decision: Loan rejected.  
Reason for expected output: Age below 21 fails the minimum age rule.

9. Test Case 9  
Input values: Age entered as -5.  
Expected output or decision: Error message and re-entry prompt.  
Reason for expected output: Negative age is invalid input.

10. Test Case 10  
Input values: Credit score entered as 950.  
Expected output or decision: Error message and re-entry prompt.  
Reason for expected output: Credit score must stay within 300 to 900.

11. Test Case 11  
Input values: Quantity entered as 0.  
Expected output or decision: Error message and re-entry prompt.  
Reason for expected output: Quantity must be greater than 0.

12. Test Case 12  
Input values: Discount percentage entered as 120.  
Expected output or decision: Error message and re-entry prompt.  
Reason for expected output: Discount percentage must be within 0 to 100.
