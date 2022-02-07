from django.db import models


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

    @staticmethod
    def get_stats() -> tuple:
        count_mutants_dna = AnalyzedDna.objects.filter(type=AnalyzedDna.MUTANT).count()
        count_human_dna = AnalyzedDna.objects.filter(type=AnalyzedDna.HUMAN).count()
        ratio = count_mutants_dna / count_human_dna if count_human_dna > 0 else 0

        return count_mutants_dna, count_human_dna, ratio