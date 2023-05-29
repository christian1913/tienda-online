{% load static %}

<!-- Shop Sidebar Start -->
<div class="col-lg-3 col-md-4">
    <!-- Price Start -->
    <h5 class="section-title position-relative text-uppercase mb-3"><span class="bg-secondary pr-3">Filtro por precio</span></h5>
    <div class="bg-light p-4 mb-30">
        <form>
            <div class="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">
                <input type="checkbox" class="custom-control-input" checked id="price-all">
                <label class="custom-control-label" for="price-all">Precio</label>
                <span class="badge border font-weight-normal"></span>
            </div>
            <div class="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">
                <input type="checkbox" class="custom-control-input" id="price-1">
                <label class="custom-control-label" for="price-1">1 - 300 €</label>
                <span class="badge border font-weight-normal"></span>
            </div>
        </form>
    </div>
    <!-- Price End -->
    
    <!-- Color Start -->
    <h5 class="section-title position-relative text-uppercase mb-3"><span class="bg-secondary pr-3">Filtro por año</span></h5>
    <div class="bg-light p-4 mb-30">
        <form>
            <div class="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">
                <input type="checkbox" class="custom-control-input" checked id="color-all">
                <label class="custom-control-label" for="price-all">Año</label>
                <span class="badge border font-weight-normal"></span>
            </div>
            <div class="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">
                <input type="checkbox" class="custom-control-input" id="color-1">
                <label class="custom-control-label" for="color-1">1900-2000</label>
                <span class="badge border font-weight-normal"></span>
            </div>
        </form>
    </div>
    <!-- Color End -->

    <!-- Size Start -->
    <h5 class="section-title position-relative text-uppercase mb-3"><span class="bg-secondary pr-3">Filtro por fecha</span></h5>
    <div class="bg-light p-4 mb-30">
        <form>
            <div class="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">
                <input type="checkbox" class="custom-control-input" checked id="size-all">
                <label class="custom-control-label" for="size-all">Estado</label>
                <span class="badge border font-weight-normal"></span>
            </div>
            <div class="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">
                <input type="checkbox" class="custom-control-input" id="size-1">
                <label class="custom-control-label" for="size-1">Óptimo</label>
                <span class="badge border font-weight-normal"></span>
            </div>
        </form>
    </div>
    <!-- Size End -->
</div>
<!-- Shop Sidebar End -->