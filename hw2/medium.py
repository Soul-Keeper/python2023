import aspose.pdf as pdf

options = pdf.TeXLoadOptions()
document = pdf.Document("hw2/artifacts/easy.tex" , options)
document.save("hw2/artifacts/my_latex.pdf")