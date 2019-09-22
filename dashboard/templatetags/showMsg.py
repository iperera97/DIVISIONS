from django import template

register = template.Library()


@register.inclusion_tag('dashboard/formErr.html')
def showErrors(errDICT):

    if errDICT is not None:

        return {
            'FORM_ERRORS': errDICT
        }

    else:
        return None
