from django import template

register = template.Library()


@register.filter(name='remove_diacritics')
def remove_diacritics(value):
    replacements = {
        'š': 's', 'đ': 'dj', 'č': 'c', 'ć': 'c', 'ž': 'z',
        'Š': 'S', 'Đ': 'Dj', 'Č': 'C', 'Ć': 'C', 'Ž': 'Z'
    }
    for src, target in replacements.items():
        value = value.replace(src, target)
    return value
