def calculate_climate_score(
    temperature,
    humidity,
    rainfall
):

    score = 100

    reasons = []

    # Temperature

    if 20 <= temperature <= 35:

        reasons.append("✅ Ideal temperature")

    else:

        score -= 15

        reasons.append("⚠ Temperature not ideal")

    # Humidity

    if humidity >= 50:

        reasons.append("✅ Good humidity")

    else:

        score -= 10

        reasons.append("⚠ Low humidity")

    # Rainfall

    if rainfall >= 100:

        reasons.append("✅ Good rainfall")

    else:

        score -= 20

        reasons.append("⚠ Low rainfall")

    return {
        "score": score,
        "reasons": reasons
    }