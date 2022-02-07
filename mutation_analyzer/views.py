from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from mutation_analyzer.helpers import MutationAnalyzer
from mutation_analyzer.models import AnalyzedDna
from mutation_analyzer.utils import json_response, json_serializer


@method_decorator(csrf_exempt, name="dispatch")
class MutationAnalyzerView(View):
    def post(self, request):
        data = json_serializer(request.body)
        dna = data.get("dna", None)

        if not dna:
            return json_response({"success": False, "message": "É necessário informar uma cadeia de DNA"}, 403)

        success, message = MutationAnalyzer.has_mutation(dna)
        status_code = 200 if success else 403

        return json_response({"success": success, "message": message}, status_code)


class StatsView(View):
    def get(self, request):
        count_mutants_dna, count_human_dna, ratio = AnalyzedDna.get_stats()
        return json_response({"count_mutants_dna": count_mutants_dna, "count_human_dna": count_human_dna, "ratio": ratio}, 200)
