class RiskAgent:

    def calculate(self, probability: float, odds: float = 2.0):
        """
        Kelly Criterion

        f = (bp - q) / b

        b = decimal odds - 1
        p = probability of winning
        q = probability of losing
        """

        b = odds - 1
        p = probability
        q = 1 - p

        kelly = (b * p - q) / b

        if kelly < 0:
            kelly = 0

        return {
            "kelly_fraction": round(kelly, 4),
            "recommended_position_percent": round(kelly * 100, 2)
        }