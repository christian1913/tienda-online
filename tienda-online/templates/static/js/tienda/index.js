{% extends "frontend/base.html" %}
{% load static %}

{% block content %}

<!-- Shop Start -->
<div class="container-fluid">
    <div class="row px-xl-5">

        {% block filtros %}
        {% include 'frontend/tienda/filtros.html' %}
        {% endblock %}
    
        <div class="col-lg-9 col-md-8">
            <div class="row pb-3">

                {% block subnav %}
                {% include 'frontend/tienda/subnav.html' %}
                {% endblock %}

                {% block productos %}
                {% include 'frontend/tienda/productos.html' %}
                {% endblock %}
                
                {% block paginas %}
                {% include 'frontend/tienda/paginas.html' %}
                {% endblock %}
            </div>
        </div>

    </div>
</div>




{% endblock %}