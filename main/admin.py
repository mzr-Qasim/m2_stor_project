from django.contrib import admin
from .models import PricingSection, PricingPlan, PricingFeature

# -----------------------------
# Pricing Section Admin
# -----------------------------
@admin.register(PricingSection)
class PricingSectionAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'section_subtitle')
    # Optional: you can make fields editable directly in list view
    # list_editable = ('section_subtitle',)

# -----------------------------
# Pricing Plan Admin with Features Inline
# -----------------------------
class FeatureInline(admin.TabularInline):
    model = PricingFeature
    extra = 1   # allow adding extra feature quickly
    can_delete = True  # optional for inline, but deletion is better via FeatureAdmin
    fields = ('feature',)

    

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('plan', 'price', 'duration', 'link_button','recommended')
    list_filter = ('recommended',)
    inlines = [FeatureInline]



@admin.register(PricingFeature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'plan')
    list_filter = ('plan',)