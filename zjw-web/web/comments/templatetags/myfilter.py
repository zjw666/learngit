from django import template
import markdown

register = template.Library()
@register.filter
def markdown_change(content):
	content = markdown.markdown(content,extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc',])
	return content