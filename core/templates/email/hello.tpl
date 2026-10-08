{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
<img src='https://www.cybersuccess.biz/wp-content/uploads/2021/03/uses-of-python-programming-language.jpg'>
This is an <strong>html</strong> message.
{% endblock %}