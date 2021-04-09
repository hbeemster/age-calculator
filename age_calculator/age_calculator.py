"""Main module."""
import arrow


def age_in_days(date_of_birth, date_of_death=None):
    """Calculates the age in days."""
    date_of_death = arrow.get(date_of_death) if date_of_death else arrow.utcnow()
    return (date_of_death - arrow.get(date_of_birth)).days


def age_in_hours(date_of_birth, date_of_death=None):
    """Calculates the age in hours."""
    raise NotImplemented
