from django.contrib import admin

from mutation_analyzer.models import AnalyzedDna


@admin.register(AnalyzedDna)
class AnalyzedDnaAdmin(admin.ModelAdmin):
    list_display = ("id", "dna", "type",)
    empty_value_display = "Não há DNAs analisados."
    readonly_fields = ("id", "dna", "type",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
