from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Returns the multiplication of value and arg."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0  # Return 0 if invalid values
