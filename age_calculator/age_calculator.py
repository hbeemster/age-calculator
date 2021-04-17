"""Main module."""
import arrow


# ------------------------------------------------------------------------
def age_in_days(date_of_birth, date_of_death=None):
    """Calculates the age in days."""
    return date_diff(date_of_birth, date_of_death)


# ------------------------------------------------------------------------
def age_in_hours(date_of_birth, date_of_death=None):
    """Calculates the age in hours."""
    return 24 * date_diff(date_of_birth, date_of_death)


# ------------------------------------------------------------------------
def date_diff(date_from, date_to=None):
    """Generic function to calculate the difference between two dates

    :param date_from: The start date
    :param date_to: The end date, default 'Today'
    :return: The difference in days, int

    """
    date_to = arrow.get(date_to) if date_to else arrow.utcnow()
    return (date_to - arrow.get(date_from)).days
