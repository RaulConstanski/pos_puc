## PROJETO DO CURSO PYTHON SCRIPTING (TURMA U)
## ALUNO: RAUL CONSTANSKI RODRIGUES
## MATRICULA: 40102383
## JUSTIFICATIVA: SOU INICIANTE NA PROGRAMAÇÃO, RESOLVI ALGUNS PEQUENOS PROBLEMAS COM VBA EXCEL, POR ISSO RESOLVI FAZER UMA MISTURA ENTRE A LISTA DE EXERCICIO E UM PROJETO.
from tkinter import *

def abrir_calc():
    framecalc = Toplevel()
    framecalc.title("Calculadora")
    #framecalc.geometry("200x200")
    Button(framecalc, text="Limpar").grid(column=0, row=0)
    Entry(framecalc, text="Limpar").grid(column=1, row=0, columnspan=2)
    Button(framecalc, text="7", width="10", height="2").grid(column=1, row=1)
    Button(framecalc, text="4", width="10", height="2").grid(column=1, row=2)
    Button(framecalc, text="1", width="10", height="2").grid(column=1, row=3)
    Button(framecalc, text="8", width="10", height="2").grid(column=2, row=1)
    Button(framecalc, text="5", width="10", height="2").grid(column=2, row=2)
    Button(framecalc, text="2", width="10", height="2").grid(column=2, row=3)
    Button(framecalc, text="9", width="10", height="2").grid(column=3, row=1)
    Button(framecalc, text="6", width="10", height="2").grid(column=3, row=2)
    Button(framecalc, text="3", width="10", height="2").grid(column=3, row=3)
    Button(framecalc, text="Fechar", command=framecalc.destroy).grid(column=5, row=5)

janela = Tk()
janela.title("Projeto - Raul")
janela.geometry("500x200")
frm = Frame()
frm.grid()
Label(frm, text="Projeto Conclusão - Raul Constanski Rodrigues", font=("Arial Bold" , 8)).grid(column=0, row=0)
## Lista de funcionalidades
Button(frm, text="Cálculadora", width="15", height="2", command=abrir_calc).grid(column=0, row=1)
Button(frm, text="Aniversário",  width="15", height="2", command=janela.destroy).grid(column=0, row=2)
Button(frm, text="Média - Notas",  width="15", height="2", command=janela.destroy).grid(column=1, row=1)
Button(frm, text="Compra de Produto",  width="15", height="2", command=janela.destroy).grid(column=1, row=2)


Button(frm, text="Quit", width="15", height="2", command=janela.destroy).grid(column=1, row=4)
janela.mainloop()