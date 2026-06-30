def predict_risk(age: int, salary: float):
    """
    Fake ML logic (placeholder for SageMaker)
    """

    # simple rule-based logic
    if salary > 80000 and age < 40:
        return "LOW", 0.2
    elif salary > 50000:
        return "MEDIUM", 0.5
    else:
        return "HIGH", 0.85