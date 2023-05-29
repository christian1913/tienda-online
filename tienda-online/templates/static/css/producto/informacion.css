{% load static %}

<div class="col-lg-7 h-auto mb-30">
    <div class="h-100 bg-light p-30">
        <h3>{{ productos.nombre }}</h3>

        <h3 class="font-weight-semi-bold mb-4">{{ productos.precio }} €</h3>
        <p class="mb-4">{{ productos.descripcion }}</p>

        <div class="d-flex align-items-center mb-4 pt-2">
            <div class="input-group quantity mr-3" style="width: 130px;">
                <div class="input-group-btn">
                    <button class="btn btn-primary btn-minus">
                        <i class="fa fa-minus"></i>
                    </button>
                </div>
                <input type="text" class="form-control bg-secondary border-0 text-center" value="1">
                <div class="input-group-btn">
                    <button class="btn btn-primary btn-plus">
                        <i class="fa fa-plus"></i>
                    </button>
                </div>
            </div>
            <form method="POST" action="{% url 'agregar-producto' id=productos.id %}">
                {% csrf_token %}
                <button type="submit" class="btn btn-primary px-3">
                    <i class="fa fa-shopping-cart mr-1"></i> Add To Cart
                </button>
            </form>
        </div>
    </div>
</div>