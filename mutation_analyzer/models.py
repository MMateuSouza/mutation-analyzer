from django.db import models

from mutation_analyzer.helpers import MutationAnalyzer


class AnalyzedDna(models.Model):
    HUMAN = "H"
    MUTANT = "M"

    DNA_TYPES = [
        (HUMAN, "Humano"),
        (MUTANT, "Mutante"),
    ]

    dna = models.TextField(verbose_name="DNA", unique=True)
    type = models.CharField(verbose_name="Tipo de DNA", max_length=1, choices=DNA_TYPES)

    class Meta:
        db_table = "analyzed_dna"
        verbose_name = "DNA Analisado"
        verbose_name_plural = "DNAs Analizados"

    def __str__(self) -> str:
        return f"[{self.get_type_display()}] {self.dna}"

    @staticmethod
    def get_stats() -> tuple:
        count_mutants_dna = AnalyzedDna.objects.filter(type=AnalyzedDna.MUTANT).count()
        count_human_dna = AnalyzedDna.objects.filter(type=AnalyzedDna.HUMAN).count()
        ratio = count_mutants_dna / count_human_dna if count_human_dna > 0 else 0

        return count_mutants_dna, count_human_dna, ratio

    @staticmethod
    def has_mutation(dna: list) -> tuple:
        success, is_valid, message, dna_string = MutationAnalyzer.has_mutation(dna)

        if is_valid:
            dna_type = AnalyzedDna.MUTANT if success else AnalyzedDna.HUMAN
            dna_object, created = AnalyzedDna.objects.get_or_create(dna=dna_string, type=dna_type)

        return success, is_valid, message