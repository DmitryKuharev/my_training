from bowling import get_score


class BowlingReport:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.tour = {}

    def tour_winners(self):
        max_value = max(self.tour.values())
        max_dict = {key: value for key, value in self.tour.items() if value == max_value}
        self.tour = {}
        return max_dict

    def act(self):
        with open(self.input_file, 'r', encoding='utf-8') as in_file,\
                open(self.output_file, 'w', encoding='utf-8') as out_file:
            for line in in_file:
                format_line = line.split('\t')
                if len(format_line) == 2:
                    person_result = get_score(format_line[1][:-1])
                    if person_result:
                        self.tour[format_line[0]] = person_result
                    out_file.write(f"{format_line[0]}\t{format_line[1][:-1]:20}\t{str(person_result):<}\n")
                elif len(format_line) == 1:
                    if "winner" in line:
                        tour_winner = self.tour_winners()
                        out_file.write(f"winner is {', '.join(list(tour_winner))}\n")
                    else:
                        out_file.write(line)
