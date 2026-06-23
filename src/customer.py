from src import utils


def get_customer_details():
    """Collect and validate a customer's profile and financial details."""
    utils.print_section("CUSTOMER PROFILE AND FINANCIAL SUMMARY")

    name = utils.get_non_empty_string("Enter customer name: ")
    age = utils.get_number_in_range("Enter age: ", 1, 120, value_type=int)
    city = utils.get_non_empty_string("Enter city: ")
    income = utils.get_non_negative_number("Enter monthly income: ")
    expenses = utils.get_non_negative_number("Enter monthly expenses: ")
    emi = utils.get_non_negative_number("Enter existing EMI amount: ")
    score = utils.get_number_in_range("Enter credit score (300-900): ", 300, 900, value_type=int)
    segment = utils.get_value_from_set(
        f"Enter customer segment {utils.VALID_SEGMENTS}: ", utils.VALID_SEGMENTS
    )

    return {
        "name": name,
        "age": age,
        "city": city,
        "income": income,
        "expenses": expenses,
        "emi": emi,
        "score": score,
        "segment": segment,
    }


def calculate_savings(income, expenses, emi):
    """Monthly savings = income - expenses - EMI."""
    return income - expenses - emi


def calculate_savings_percentage(savings, income):
    """Savings percentage = savings / income, as a percentage."""
    if income == 0:
        return 0.0
    return (savings / income) * 100


def calculate_emi_to_income_ratio(emi, income):
    """EMI-to-income ratio = EMI / income, as a percentage."""
    if income == 0:
        return 0.0
    return (emi / income) * 100


def classify_risk(score, savings_pct, emi_ratio):
    """
    Low Risk    : credit score >= 750, savings% >= 25, EMI-to-income ratio <= 25
    Medium Risk : credit score >= 650, savings% >= 10, EMI-to-income ratio <= 40
    High Risk   : all remaining cases
    """
    if score >= 750 and savings_pct >= 25 and emi_ratio <= 25:
        return "Low Risk"
    if score >= 650 and savings_pct >= 10 and emi_ratio <= 40:
        return "Medium Risk"
    return "High Risk"


def classify_value(income, segment, savings_pct):
    """
    High Value   : monthly income >= 150000, OR Enterprise segment with savings% >= 20
    Medium Value : monthly income >= 60000, OR Premium segment
    Low Value    : all remaining cases
    """
    if income >= 150000 or (segment == "Enterprise" and savings_pct >= 20):
        return "High Value"
    if income >= 60000 or segment == "Premium":
        return "Medium Value"
    return "Low Value"


def build_summary(customer):
    """Run all Feature 1 calculations and return them as a dictionary."""
    savings = calculate_savings(customer["income"], customer["expenses"], customer["emi"])
    savings_pct = calculate_savings_percentage(savings, customer["income"])
    emi_ratio = calculate_emi_to_income_ratio(customer["emi"], customer["income"])
    risk = classify_risk(customer["score"], savings_pct, emi_ratio)
    value = classify_value(customer["income"], customer["segment"], savings_pct)

    return {
        "savings": savings,
        "savings_pct": savings_pct,
        "emi_ratio": emi_ratio,
        "risk": risk,
        "value": value,
    }


def display_summary(customer, summary):
    print()
    print(f"Customer Name        : {customer['name']}")
    print(f"Age                  : {customer['age']}")
    print(f"City                 : {customer['city']}")
    print(f"Segment              : {customer['segment']}")
    print(f"Monthly Income       : {utils.format_currency(customer['income'])}")
    print(f"Monthly Expenses     : {utils.format_currency(customer['expenses'])}")
    print(f"Existing EMI         : {utils.format_currency(customer['emi'])}")
    print(f"Credit Score         : {customer['score']}")
    print("-" * 60)
    print(f"Monthly Savings      : {utils.format_currency(summary['savings'])}")
    print(f"Savings Percentage   : {utils.format_percentage(summary['savings_pct'])}")
    print(f"EMI-to-Income Ratio  : {utils.format_percentage(summary['emi_ratio'])}")
    print(f"Risk Category        : {summary['risk']}")
    print(f"Customer Value       : {summary['value']}")


def run():
    """Entry point called by main.py for menu option 1."""
    customer = get_customer_details()
    summary = build_summary(customer)
    display_summary(customer, summary)
