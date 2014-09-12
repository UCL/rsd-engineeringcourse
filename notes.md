{% for source in sorted(d)%}
{% if 'session' in source and '.md' in source %}
{{d[source]}}
{% endif %}
{% endfor %}