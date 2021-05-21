"""Main module."""
import arrow


# ------------------------------------------------------------------------
def age_in_days(date_of_birth, date_of_death=None):
    """Calculates the age in days.

    :param date_of_birth: The date of birth
    :param date_of_death: The date of death, optional. If not given the current date is used.
    :return int: The age in days
    """
    return date_diff(date_of_birth, date_of_death)


# ------------------------------------------------------------------------
def age_in_hours(date_of_birth, date_of_death=None):
    """Calculates the age in hours.

    :param date_of_birth: The date of birth
    :param date_of_death: The date of death, optional. If not given the current date is used.
    :return int: The age in hours
    """
    return 24 * date_diff(date_of_birth, date_of_death)


# ------------------------------------------------------------------------
def date_diff(date_from, date_to=None):
    """Generic function to calculate the difference between two dates

    :param date_from: The start date
    :param date_to: The end date, default 'Today'
    :return: The difference in days, int

    """
    date_to = arrow.get(date_to) if date_to else arrow.utcnow()
   # return (date_to - arrow.get(date_from)).days
    date = (date_to - arrow.get(date_from)).days
    if date < 0:
        raise Exception("ValueError")

    else:
        date_1 = date
    return date_1
