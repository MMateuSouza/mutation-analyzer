from django.db.utils import IntegrityError
from django.test import Client, TestCase
from django.urls import reverse

import json

from mutation_analyzer.models import AnalyzedDna


class AnalyzedDnaTestCase(TestCase):
    def setUp(self) -> None:
        self.human_dna = {
            "dna": "CTGGAACTGCTCTGCTGTAGAGGGTCCCTATCACTG",
            "type": AnalyzedDna.HUMAN,
        }
        AnalyzedDna.objects.create(**self.human_dna)

        self.mutant_dna = {
            "dna": "CTGAGACTATGCTATTGTAGAGGGCCCCTATCACTG",
            "type": AnalyzedDna.MUTANT,
        }
        AnalyzedDna.objects.create(**self.mutant_dna)

    # Garantir que não seja possível inserir registros duplicados
    def test_should_throw_integrity_error_when_trying_to_insert_an_already_existing_dna(self):
        with self.assertRaises(IntegrityError):
            AnalyzedDna.objects.create(**self.human_dna)

    # Garantir que um registro já analisado e não possa ser modificado
    def test_should_throw_integrity_error_when_trying_to_update_an_already_analyzed_dna(self):
        updated_dna = {
            "dna": self.human_dna["dna"],
            "type": self.mutant_dna["type"],
        }
        with self.assertRaises(IntegrityError):
            AnalyzedDna.objects.create(**updated_dna)

    def test_should_return_correct_stats_information(self):
        client = Client()
        response = client.get(reverse("stats"))

        expected_status_code = 200
        expected_content_type = "application/json"
        expected_stats_information = {"count_mutants_dna": 1, "count_human_dna": 1, "ratio": 1.0}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_stats_information, response.json())

    def test_should_return_status_code_200_with_mutated_dna(self):
        data = {"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 200
        expected_content_type = "application/json"
        expected_content = {"success": True, "is_valid": True, "message": "O DNA informado é válido."}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    def test_should_return_status_code_403_with_human_dna(self):
        data = {"dna": ["CTGGAA", "CTGCTC", "TGCTGT", "AGAGGG", "TCCCTA", "TCACTG"]}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"success": False, "is_valid": True, "message": "O DNA informado é válido."}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    def test_should_return_status_code_403_when_dna_is_of_str_type(self):
        data = {"dna": self.human_dna["dna"]}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"is_valid": False, "message": "O DNA informado é inválido.", "success": False}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    def test_should_return_status_code_403_when_dna_is_of_int_type(self):
        data = {"dna": 5432}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"is_valid": False, "message": "O DNA informado é inválido.", "success": False}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    def test_should_return_status_code_403_when_dna_is_of_none_type(self):
        data = {"dna": None}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"message": "É necessário informar uma cadeia de DNA", "success": False}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    def test_should_return_status_code_403_when_dna_is_an_empty_list(self):
        data = {"dna": []}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"message": "É necessário informar uma cadeia de DNA", "success": False}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    def test_should_return_status_code_403_when_dna_is_an_integer_list(self):
        data = {"dna": [1, 22, 333, 4444, 55555, 666666]}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"is_valid": False, "message": "O DNA informado é inválido.", "success": False}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    def test_should_return_status_code_403_when_dna_is_not_an_nxn_order_matrix(self):
        data = {"dna": ["A", "CC", "TTT", "GGGG"]}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"is_valid": False, "message": "O DNA informado é inválido.", "success": False}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())

    # Quando houver uma matriz de ordem inferior a 4 não haverá repetição de 4 caracteres, logo, é considerado humano
    def test_should_return_status_code_403_when_dna_is_an_matrix_of_order_less_than_4(self):
        data = {"dna": ["CTG", "CTA", "TAT"]}

        client = Client()
        response = client.post(reverse("mutants"), data, "application/json")

        expected_status_code = 403
        expected_content_type = "application/json"
        expected_content = {"success": False, "is_valid": True, "message": "O DNA informado é válido."}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_content_type, response.headers["Content-Type"])
        self.assertEqual(expected_content, response.json())
