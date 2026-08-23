def calculate_surf_score(wave_height, wave_period, wind_speed):
    """
    Calculate a basic surf score from 0 to 100.
    """

    wave_score = min(wave_height / 2.0, 1) * 40
    period_score = min(wave_period / 16.0, 1) * 40
    wind_score = max(1 - wind_speed / 30.0, 0) * 20

    score = wave_score + period_score + wind_score

    return round(score, 1)


score = calculate_surf_score(
    wave_height=1.5,
    wave_period=14,
    wind_speed=8
)

print(f"Surf Score: {score}/100")