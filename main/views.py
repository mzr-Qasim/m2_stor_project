from django.shortcuts import render
from main.models import PricingPlan, PricingSection

# Create your views here.
def home(request):
    pricing_section = PricingSection.objects.all()
    pricing_plans = PricingPlan.objects.prefetch_related('features').all()

    context={
        'pricing_section':pricing_section,
        'pricing_plans': pricing_plans,
    }
    return render(request, 'index.html', context)  



    