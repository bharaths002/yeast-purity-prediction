from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .ml_model import predict_purity

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_purity(request):
    if request.method == 'POST':
        molasses_amount = request.POST.get('molasses_amount')
        grain_starch_amount = request.POST.get('grain_starch_amount')
        potato_starch_amount = request.POST.get('potato_starch_amount')
        water = request.POST.get('water')
        nutrients_vitamins = request.POST.get('nutrients_vitamins')
        emulsifiers = request.POST.get('emulsifiers')

        # Convert input values to the correct type
        molasses_amount = float(molasses_amount)
        grain_starch_amount = float(grain_starch_amount)
        potato_starch_amount = float(potato_starch_amount)
        water = float(water)
        nutrients_vitamins = float(nutrients_vitamins)
        emulsifiers = float(emulsifiers)

        purity = predict_purity(molasses_amount, grain_starch_amount, potato_starch_amount, water, nutrients_vitamins, emulsifiers)

        return render(request, 'index.html', {
            'purity': purity,
            'molasses_amount': molasses_amount,
            'grain_starch_amount': grain_starch_amount,
            'potato_starch_amount': potato_starch_amount,
            'water': water,
            'nutrients_vitamins': nutrients_vitamins,
            'emulsifiers': emulsifiers
        })
    return render(request, 'index.html')
