def angular_distance(direction_1, direction_2):
    """Calculate the shortest angular distance between two directions."""
    difference = abs(direction_1 - direction_2)
    return min(difference, 360 - difference)


def wave_height_score(height):
    """Score wave height from 0 to 100."""
    if height < 0.3:
        return 10
    elif height < 0.6:
        return 35
    elif height < 1.0:
        return 65
    elif height < 1.5:
        return 85
    elif height < 2.5:
        return 100
    else:
        return 70


def wave_period_score(period):
    """Score wave period from 0 to 100."""
    if period < 6:
        return 10
    elif period < 8:
        return 35
    elif period < 10:
        return 65
    elif period < 14:
        return 85
    else:
        return 100


def wind_speed_score(wind_speed):
    """Score wind speed from 0 to 100."""
    if wind_speed < 5:
        return 100
    elif wind_speed < 10:
        return 85
    elif wind_speed < 15:
        return 65
    elif wind_speed < 20:
        return 40
    elif wind_speed < 25:
        return 20
    else:
        return 5


def swell_direction_score(actual_direction, preferred_direction):
    """Score swell direction based on angular distance."""
    distance = angular_distance(
        actual_direction,
        preferred_direction
    )

    score = max(100 - (distance / 90) * 100, 0)

    return round(score, 1)


def wind_direction_score(actual_direction, preferred_direction):
    """Score wind direction based on angular distance."""
    distance = angular_distance(
        actual_direction,
        preferred_direction
    )

    score = max(100 - (distance / 90) * 100, 0)

    return round(score, 1)


def calculate_surf_score(
    wave_height,
    wave_period,
    wind_speed,
    wave_direction,
    preferred_swell_direction,
    wind_direction,
    preferred_wind_direction
):
    """Calculate the overall Surf Score from 0 to 100."""

    height_score = wave_height_score(wave_height)

    period_score = wave_period_score(wave_period)

    wind_speed_score_value = wind_speed_score(wind_speed)

    swell_direction_score_value = swell_direction_score(
        wave_direction,
        preferred_swell_direction
    )

    wind_direction_score_value = wind_direction_score(
        wind_direction,
        preferred_wind_direction
    )

    score = (
        height_score * 0.25
        + period_score * 0.25
        + wind_speed_score_value * 0.15
        + swell_direction_score_value * 0.15
        + wind_direction_score_value * 0.20
    )

    return round(score, 1)