def calculate_wave_score(wave_height):
    """Score wave height from 0 to 100."""
    return min(wave_height / 2.0, 1) * 100


def calculate_period_score(wave_period):
    """Score wave period from 0 to 100."""
    return min(wave_period / 16.0, 1) * 100


def calculate_wind_score(wind_speed):
    """Score wind speed from 0 to 100."""
    return max(1 - wind_speed / 30.0, 0) * 100


def calculate_surf_score(wave_height, wave_period, wind_speed):
    """Calculate overall surf score from 0 to 100."""

    wave_score = calculate_wave_score(wave_height)
    period_score = calculate_period_score(wave_period)
    wind_score = calculate_wind_score(wind_speed)

    score = (
        wave_score * 0.30
        + period_score * 0.30
        + wind_score * 0.25
        + 50 * 0.15
    )

    return round(score, 1)


score = calculate_surf_score(
    wave_height=1.5,
    wave_period=14,
    wind_speed=8
)

print(f"Surf Score: {score}/100")