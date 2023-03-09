from ImageGenerator import ImageGenerator

generator = ImageGenerator(300, 300, True, "hw2/artifacts")

def gen_latex(input: list[list, list]) -> str:
    latex = "\\documentclass{article}\n\\usepackage{graphicx}\n\\graphicspath{ {./hw2/artifacts/} }\n\\begin{document}\n"
    latex += gen_table(input)
    latex += add_picture("img")
    return latex + "\\end{document}"

def gen_table_line(input: list) -> str:
    return " " + str(input).strip('[]').replace(',', ' &') + " \\\\\n"

def gen_table(input: list[list, list]) -> str:
    table = "\\begin{center}\n\\begin{tabular}{ |c|c|c| }\n \hline\n"
    for line in input:
        table += gen_table_line(line)
    return table + " \hline\n\\end{tabular}\n\\end{center}\n"

def add_picture(file_name: str) -> str:
    generator.generate()
    return "\\includegraphics{" + file_name + "}\n"

def save_latex(input: list[list, list]) -> None:
    with open("hw2/artifacts/easy.tex", "w") as out_file:
        out_file.write(gen_latex(input))
  
save_latex([[1, 2, 3], [3, 2, 1]])

