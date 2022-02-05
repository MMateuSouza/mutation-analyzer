class MutationAnalyzer:
    @staticmethod
    def __analysis(dna, lines, columns) -> bool:
        nitrogen_bases_sequences_found = 0

        for x in range(lines):
            for y in range(columns):
                current_nitrogen_base = dna[x][y]

                has_not_horizontal_overflow = (y + 4 <= columns)
                has_not_bottom_vertical_overflow = (x + 4 <= lines)
                has_not_reverse_horizontal_overflow = (3 - y >= 0)  # Esquerda para direita

                # Horizontal se estiver no limite de colunas
                if has_not_horizontal_overflow:
                    nitrogen_bases_sequences_found += MutationAnalyzer.__horizontal_analysis(dna, lines, columns, current_nitrogen_base, x, y)

                # Vertical inferior se estiver no limite de linhas
                if has_not_bottom_vertical_overflow:
                    nitrogen_bases_sequences_found += MutationAnalyzer.__vertical_analysis(dna, lines, columns, current_nitrogen_base, x, y)
                    MutationAnalyzer.__check_nitrogen_bases_sequences_found(nitrogen_bases_sequences_found)

                # Diagonal "primária" se estiver no limite de linhas X colunas
                if has_not_horizontal_overflow and has_not_bottom_vertical_overflow:
                    nitrogen_bases_sequences_found += MutationAnalyzer.__primary_diagonal_analysis(dna, lines, columns, current_nitrogen_base, x, y)
                    MutationAnalyzer.__check_nitrogen_bases_sequences_found(nitrogen_bases_sequences_found)

                # Diagonal "secundária" se estiver no limite de linhas X colunas
                if has_not_reverse_horizontal_overflow and has_not_bottom_vertical_overflow:
                    nitrogen_bases_sequences_found += MutationAnalyzer.__secondary_diagonal_analysis(dna, lines, columns, current_nitrogen_base, x, y)
                    MutationAnalyzer.__check_nitrogen_bases_sequences_found(nitrogen_bases_sequences_found)

        return MutationAnalyzer.__check_nitrogen_bases_sequences_found(nitrogen_bases_sequences_found)

    @staticmethod
    def __check_nitrogen_bases_sequences_found(nitrogen_bases_sequences_found):
        if nitrogen_bases_sequences_found > 1:
            return True
        return False

    @staticmethod
    def __check_cartesian_limits(lines, columns, x, y) -> bool:
        return x < 0 or y < 0 or x >= lines or y >= columns

    @staticmethod
    def __check_summation(summation) -> bool:
        return summation == 4

    @staticmethod
    def __different_nitrogen_bases(last_nitrogen_base, current_nitrogen_base) -> bool:
        return last_nitrogen_base != current_nitrogen_base

    @staticmethod
    def __horizontal_analysis(dna, lines, columns, last_nitrogen_base, x, y, summation=0) -> int:
        if MutationAnalyzer.__check_summation(summation):
            return 1

        if MutationAnalyzer.__check_cartesian_limits(lines, columns, x, y):
            return 0

        current_nitrogen_base = dna[x][y]
        if MutationAnalyzer.__different_nitrogen_bases(last_nitrogen_base, current_nitrogen_base):
            return 0

        return MutationAnalyzer.__horizontal_analysis(dna, lines, columns, current_nitrogen_base, x, y + 1, summation + 1)

    @staticmethod
    def __vertical_analysis(dna, lines, columns, last_nitrogen_base, x, y, summation=0) -> int:
        if MutationAnalyzer.__check_summation(summation):
            return 1

        if MutationAnalyzer.__check_cartesian_limits(lines, columns, x, y):
            return 0

        current_nitrogen_base = dna[x][y]
        if MutationAnalyzer.__different_nitrogen_bases(last_nitrogen_base, current_nitrogen_base):
            return 0

        return MutationAnalyzer.__vertical_analysis(dna, lines, columns, current_nitrogen_base, x + 1, y, summation + 1)

    @staticmethod
    def __primary_diagonal_analysis(dna, lines, columns, last_nitrogen_base, x, y, summation=0) -> int:
        if MutationAnalyzer.__check_summation(summation):
            return 1

        if MutationAnalyzer.__check_cartesian_limits(lines, columns, x, y):
            return 0

        current_nitrogen_base = dna[x][y]
        if MutationAnalyzer.__different_nitrogen_bases(last_nitrogen_base, current_nitrogen_base):
            return 0

        return MutationAnalyzer.__primary_diagonal_analysis(dna, lines, columns, current_nitrogen_base, x + 1, y + 1, summation + 1)

    @staticmethod
    def __secondary_diagonal_analysis(dna, lines, columns, last_nitrogen_base, x, y, summation=0) -> int:
        if MutationAnalyzer.__check_summation(summation):
            return 1

        if MutationAnalyzer.__check_cartesian_limits(lines, columns, x, y):
            return 0

        current_nitrogen_base = dna[x][y]
        if MutationAnalyzer.__different_nitrogen_bases(last_nitrogen_base, current_nitrogen_base):
            return 0

        return MutationAnalyzer.__secondary_diagonal_analysis(dna, lines, columns, current_nitrogen_base, x + 1, y - 1, summation + 1)

    @staticmethod
    def print_dna(dna):
        lines = len(dna)
        columns = len(dna[0]) if lines > 0 else 0

        for x in range(lines):
            for y in range(columns):
                print(f"{dna[x][y]}", end="\t")
            print()

    @staticmethod
    def has_mutation(dna: list) -> bool:
        lines = len(dna)
        columns = len(dna[0]) if lines > 0 else 0

        # Se a matriz (N x N) for inferior a 4 não será possível ter repetições
        if lines < 4:
            return False

        return MutationAnalyzer.__analysis(dna, lines, columns)


def main() -> None:
    dna = ["CTGAGA", "CTATGC", "TATTGT", "AGAGGG", "CCCCTA", "TCACTG"]
    has_mutation = MutationAnalyzer.has_mutation(dna)
    MutationAnalyzer.print_dna(dna)
    print(has_mutation)


if __name__ == "__main__":
    main()
