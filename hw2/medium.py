import aspose.pdf as pdf

options = pdf.TeXLoadOptions()
document = pdf.Document("artifacts/easy.tex" , options)
document.save("artifacts/my_latex.pdf")