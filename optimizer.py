def generate_recommendation(
    cpu,
    memory,
    latency
):
    """
    Generate infrastructure optimization
    recommendations based on resource utilization.
    """

    if cpu >= 85 or memory >= 85:

        return {
            "action": "SCALE UP",
            "severity": "HIGH",
            "reason": (
                "Resource utilization is "
                "critically high."
            )
        }

    if latency >= 500:

        return {
            "action": "INVESTIGATE",
            "severity": "MEDIUM",
            "reason": (
                "Application latency is "
                "above the normal threshold."
            )
        }

    if cpu <= 25 and memory <= 30:

        return {
            "action": "SCALE DOWN",
            "severity": "LOW",
            "reason": (
                "Infrastructure appears "
                "under-utilized."
            )
        }

    return {
        "action": "MAINTAIN",
        "severity": "NORMAL",
        "reason": (
            "Infrastructure utilization "
            "is within acceptable limits."
        )
    }
