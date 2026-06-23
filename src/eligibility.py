from src import utils


# ---------- Feature 3: Loan Eligibility ----------

def get_loan_inputs():
    """Collect and validate inputs needed for the loan eligibility decision."""
    utils.print_section("LOAN ELIGIBILITY DECISION")

    age = utils.get_number_in_range("Enter age: ", 1, 120, value_type=int)
    income = utils.get_positive_number("Enter monthly income: ")
    existing_emi = utils.get_non_negative_number("Enter existing EMI amount: ")
    score = utils.get_number_in_range("Enter credit score (300-900): ", 300, 900, value_type=int)
    savings_pct = utils.get_number_in_range("Enter savings percentage: ", 0, 100)
    requested_loan = utils.get_positive_number("Enter requested loan amount: ")

    return {
        "age": age,
        "income": income,
        "existing_emi": existing_emi,
        "score": score,
        "savings_pct": savings_pct,
        "requested_loan": requested_loan,
    }


def calculate_projected_emi_ratio(income, existing_emi, requested_loan):
    """
    Projected EMI       = requested loan amount / LOAN_PROJECTION_MONTHS
    Projected EMI ratio = (existing EMI + projected EMI) / income, as a percentage
    """
    projected_emi = requested_loan / utils.LOAN_PROJECTION_MONTHS
    total_emi = existing_emi + projected_emi
    ratio = (total_emi / income) * 100 if income else 0.0
    return projected_emi, ratio


def decide_loan_eligibility(loan_data):
    """
    Rejected                : age < 21
    Approved                : credit score >= 750, savings% >= 20, projected EMI ratio <= 40
    Manual Review Required  : credit score >= 650, savings% >= 10, projected EMI ratio <= 55
    Rejected                : all other cases
    """
    age = loan_data["age"]
    score = loan_data["score"]
    savings_pct = loan_data["savings_pct"]
    projected_emi, ratio = calculate_projected_emi_ratio(
        loan_data["income"], loan_data["existing_emi"], loan_data["requested_loan"]
    )

    if age < 21:
        return "Rejected", "Age is below the minimum eligible age of 21.", projected_emi, ratio

    if score >= 750 and savings_pct >= 20 and ratio <= 40:
        return (
            "Approved",
            "Credit score, savings percentage, and projected EMI ratio all meet the approval criteria.",
            projected_emi,
            ratio,
        )

    if score >= 650 and savings_pct >= 10 and ratio <= 55:
        return (
            "Manual Review Required",
            "Credit score is acceptable, but the savings percentage or projected EMI ratio "
            "does not fully meet the approval criteria.",
            projected_emi,
            ratio,
        )

    return (
        "Rejected",
        "Credit score, savings percentage, and projected EMI ratio do not meet the minimum requirements.",
        projected_emi,
        ratio,
    )


def display_loan_decision(loan_data, decision, reason, projected_emi, ratio):
    print()
    print(f"Age                      : {loan_data['age']}")
    print(f"Monthly Income           : {utils.format_currency(loan_data['income'])}")
    print(f"Existing EMI             : {utils.format_currency(loan_data['existing_emi'])}")
    print(f"Credit Score             : {loan_data['score']}")
    print(f"Savings Percentage       : {utils.format_percentage(loan_data['savings_pct'])}")
    print(f"Requested Loan Amount    : {utils.format_currency(loan_data['requested_loan'])}")
    print(f"Projected EMI            : {utils.format_currency(projected_emi)}")
    print(f"Projected EMI Ratio      : {utils.format_percentage(ratio)}")
    print("-" * 60)
    print(f"Decision: {decision}")
    print(f"Reason: {reason}")


def run_loan_eligibility():
    """Entry point called by main.py for menu option 3."""
    loan_data = get_loan_inputs()
    decision, reason, projected_emi, ratio = decide_loan_eligibility(loan_data)
    display_loan_decision(loan_data, decision, reason, projected_emi, ratio)


# ---------- Feature 4: Campaign Eligibility ----------

def get_campaign_inputs():
    """Collect and validate inputs needed for the campaign eligibility decision."""
    utils.print_section("CAMPAIGN ELIGIBILITY")

    segment = utils.get_value_from_set(
        f"Enter customer segment {utils.VALID_SEGMENTS}: ", utils.VALID_SEGMENTS
    )
    city = utils.get_non_empty_string("Enter city: ")
    savings_pct = utils.get_number_in_range("Enter savings percentage: ", 0, 100)
    value = utils.get_value_from_set(
        f"Enter customer value category {utils.VALID_VALUE_CATEGORIES}: ", utils.VALID_VALUE_CATEGORIES
    )

    return {"segment": segment, "city": city, "savings_pct": savings_pct, "value": value}


def decide_campaign(data):
    """
    Premium Upsell Campaign : Premium segment AND High Value
    Cashback Campaign       : target city AND savings% >= 15
    Loan Offer Campaign     : Medium or High Value, not matched by an earlier rule
    No Campaign              : all remaining cases
    """
    if data["segment"] == "Premium" and data["value"] == "High":
        return (
            "Premium Upsell Campaign",
            "Customer is in the Premium segment and classified as High Value.",
        )

    if data["city"] in utils.CASHBACK_CITIES and data["savings_pct"] >= 15:
        return (
            "Cashback Campaign",
            f"Customer is based in a target city ({data['city']}) and savings percentage "
            f"({data['savings_pct']:.2f}%) is at least 15%.",
        )

    if data["value"] in ("Medium", "High"):
        return (
            "Loan Offer Campaign",
            f"Customer is classified as {data['value']} Value and did not match an earlier campaign rule.",
        )

    return "No Campaign", "Customer does not meet the criteria for any active campaign."


def display_campaign_decision(data, campaign, reason):
    print()
    print(f"Segment              : {data['segment']}")
    print(f"City                 : {data['city']}")
    print(f"Savings Percentage   : {utils.format_percentage(data['savings_pct'])}")
    print(f"Customer Value       : {data['value']}")
    print("-" * 60)
    print(f"Campaign Assigned: {campaign}")
    print(f"Reason: {reason}")


def run_campaign_eligibility():
    """Entry point called by main.py for menu option 4."""
    data = get_campaign_inputs()
    campaign, reason = decide_campaign(data)
    display_campaign_decision(data, campaign, reason)
