from django.db import models


class PricingSection(models.Model):
    section_title = models.CharField(max_length=200, help_text="Main heading for the pricing section", blank=True, default='')
    section_subtitle = models.CharField(max_length=200, help_text="Bold or slogan text")
    section_paragraph = models.TextField(help_text="Paragraph / description text")

    class Meta:
        verbose_name = "Pricing Section"
        verbose_name_plural = "Pricing Section"

    def __str__(self):
        return self.section_title




class PricingPlan(models.Model):
    plan = models.CharField(max_length=100)
    price = models.CharField(max_length=8, blank=True, default='')
    duration = models.CharField(max_length=50)  # e.g., "per month"
    link_button = models.CharField(max_length=60, blank=True, default='')
    recommended = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Pricing Plan"
        verbose_name_plural = "Pricing Plans"

    def __str__(self):
        return self.plan

class PricingFeature(models.Model):
    plan = models.ForeignKey(PricingPlan, related_name='features', on_delete=models.CASCADE)
    feature = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Pricing Feature"
        verbose_name_plural = "Pricing Features"

    def __str__(self):
        return f"{self.feature} ({self.plan.plan})"
