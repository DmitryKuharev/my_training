from lesson_14.bowling import get_score


class BowlingReport:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.tour_winner = {}

    def act(self):
        with open(self.input_file, 'r', encoding='utf-8') as in_file,\
                open(self.output_file, 'w', encoding='utf-8') as out_file:
            for line in in_file:
                format_line = line.split('\t')
                if len(format_line) == 2:
                    out_file.write(f"{format_line[0]}\t{format_line[1][:-1]:20}\t"
                                   f"{str(get_score(format_line[1][:-1])):<}\n")
                elif len(format_line) == 1:
                    if "winner" in line:
                        out_file.write(f"winner is ")
                    else:
                        out_file.write(line)

    # def append_report(self, line_to_append):
    #     with open(self.output_file, 'a', encoding='utf-8') as out_file:



report = BowlingReport('tournament.txt', 'report_tournament.txt')
report.act()