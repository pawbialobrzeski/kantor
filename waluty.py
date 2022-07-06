from tkinter import *
from tkinter import messagebox

class ujemnaError(Exception):
    pass

class rozwiniecieError(Exception):
    pass

class Kantor(object):
    def __init__(self):
        self.okno = Tk()
        self.okno.geometry('550x800')
        self.okno.title('Przelicznik walut')
        self.buduj()
        self.okno.mainloop()

    def buduj(self):

        self.etykieta1 = Label(self.okno, text='Podaj kwotę w złotówkach (PLN)',background='gold')
        self.etykieta1.grid(row=0, column=0, sticky='W')

        self.wejsciePLN = Text(self.okno, width=25, height=1,background='#F5DD6E')
        self.wejsciePLN.grid(row=0, column=1, sticky='W')

        self.etykieta2 = Label(self.okno, text='Przeliczona kwota w')
        self.etykieta2.grid(row=1, column=0, sticky='W')

        self.przyciskEUR = Button(self.okno, text='PRZELICZ NA EURO', width=20, height=1, background='#61BBE8')
        self.przyciskEUR['command'] = self.przeliczEUR
        self.przyciskEUR.grid(row=2, column=2, sticky='W')

        self.etykietaEUR = Label(self.okno, text='EURO',background='#6CE854',width=25)
        self.etykietaEUR.grid(row=2, column=0, sticky='W')

        self.wyjscieEUR = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieEUR.grid(row=2, column=1, sticky='W')

        self.przyciskUSD = Button(self.okno, text='PRZELICZ NA USD', width=20, height=1,background='#61BBE8')
        self.przyciskUSD['command'] = self.przeliczUSD
        self.przyciskUSD.grid(row=3, column=2, sticky='W')

        self.etykietaUSD = Label(self.okno, text='Dolar amerykański (USD)',background='#6CE854',width=25)
        self.etykietaUSD.grid(row=3, column=0, sticky='W')

        self.wyjscieUSD = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieUSD.grid(row=3, column=1, sticky='W')

        self.przyciskGBP = Button(self.okno, text='PRZELICZ NA GBP', width=20, height=1,background='#61BBE8')
        self.przyciskGBP['command'] = self.przeliczGBP
        self.przyciskGBP.grid(row=4, column=2, sticky='W')

        self.etykietaGBP = Label(self.okno, text='Funt brytyjski (GBP)',background='#6CE854',width=25)
        self.etykietaGBP.grid(row=4, column=0, sticky='W')

        self.wyjscieGBP = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieGBP.grid(row=4, column=1, sticky='W')

        self.przyciskCHF = Button(self.okno, text='PRZELICZ NA CHF', width=20, height=1,background='#61BBE8')
        self.przyciskCHF['command'] = self.przeliczCHF
        self.przyciskCHF.grid(row=5, column=2, sticky='W')

        self.etykietaCHF = Label(self.okno, text='Frank szwajcarski (CHF)',background='#6CE854',width=25)
        self.etykietaCHF.grid(row=5, column=0, sticky='W')

        self.wyjscieCHF = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieCHF.grid(row=5, column=1, sticky='W')

        self.przyciskRUB = Button(self.okno, text='PRZELICZ NA RUBLE', width=20, height=1,background='#61BBE8')
        self.przyciskRUB['command'] = self.przeliczRUB
        self.przyciskRUB.grid(row=6, column=2, sticky='W')

        self.etykietaRUB = Label(self.okno, text='Rubel rosyjski (RUB)',background='#6CE854',width=25)
        self.etykietaRUB.grid(row=6, column=0, sticky='W')

        self.wyjscieRUB = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieRUB.grid(row=6, column=1, sticky='W')

        self.przyciskJPY = Button(self.okno, text='PRZELICZ NA JENY', width=20, height=1,background='#61BBE8')
        self.przyciskJPY['command'] = self.przeliczJPY
        self.przyciskJPY.grid(row=7, column=2, sticky='W')

        self.etykietaJPY = Label(self.okno, text='Jen japoński (JPY)',background='#6CE854',width=25)
        self.etykietaJPY.grid(row=7, column=0, sticky='W')

        self.wyjscieJPY = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieJPY.grid(row=7, column=1, sticky='W')

        self.przyciskCZK = Button(self.okno, text='PRZELICZ NA KORONY CZ.', width=20, height=1,background='#61BBE8')
        self.przyciskCZK['command'] = self.przeliczCZK
        self.przyciskCZK.grid(row=8, column=2, sticky='W')

        self.etykietaCZK = Label(self.okno, text='Korona czeska (CZK)',background='#6CE854',width=25)
        self.etykietaCZK.grid(row=8, column=0, sticky='W')

        self.wyjscieCZK = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieCZK.grid(row=8, column=1, sticky='W')

        self.przyciskUAH = Button(self.okno, text='PRZELICZ NA HRYWNY', width=20, height=1,background='#61BBE8')
        self.przyciskUAH['command'] = self.przeliczUAH
        self.przyciskUAH.grid(row=9, column=2, sticky='W')

        self.etykietaUAH = Label(self.okno, text='Hrywna ukraińska (UAH)',background='#6CE854',width=25)
        self.etykietaUAH.grid(row=9, column=0, sticky='W')

        self.wyjscieUAH = Text(self.okno, width=25, height=1,background='#EBEA48')
        self.wyjscieUAH.grid(row=9, column=1, sticky='W')

        self.przyciskALL = Button(self.okno, text='Przelicz wszystko',width=20, height=1, background='#4C92B5')
        self.przyciskALL['command'] = self.przeliczALL
        self.przyciskALL.grid(row=10, column=1, sticky='W')

    def sprawdz_kwote(self):
        try:
            c = float(self.wejsciePLN.get(0.0, END))
            if c < 0:
                raise ujemnaError
            if c - round(c, 2) != 0:
                raise rozwiniecieError
        except ujemnaError:
            messagebox.showinfo('BŁĄD WARTOŚCI', 'Kwota nie może być ujemna')
        except ValueError:
            messagebox.showerror('BŁĄD FORMATU', 'Kwota powinna być liczbą')
        except rozwiniecieError:
            messagebox.showinfo('BŁĄD KWOTY', 'Kwota powinna mieć maksymalnie dwa miejsca po przecinku')
        else:
            return c

    def przeliczALL(self):
        self.przeliczCHF()
        self.przeliczCZK()
        self.przeliczRUB()
        self.przeliczEUR()
        self.przeliczUAH()
        self.przeliczGBP()
        self.przeliczUSD()
        self.przeliczJPY()

    def przeliczRUB(self):
        c = self.sprawdz_kwote()
        self.wyjscieRUB.delete(0.0, END)
        self.wyjscieRUB.insert(0.0, str(round(c/0.08 , 4)))

    def przeliczCZK(self):
        c = self.sprawdz_kwote()
        self.wyjscieCZK.delete(0.0, END)
        self.wyjscieCZK.insert(0.0, str(round(c/0.19 , 4)))

    def przeliczJPY(self):
        c = self.sprawdz_kwote()
        self.wyjscieJPY.delete(0.0, END)
        self.wyjscieJPY.insert(0.0, str(round(c/0.034 , 4)))

    def przeliczUAH(self):
        c = self.sprawdz_kwote()
        self.wyjscieUAH.delete(0.0, END)
        self.wyjscieUAH.insert(0.0, str(round(c/0.15 , 4)))

    def przeliczCHF(self):
        c = self.sprawdz_kwote()
        self.wyjscieCHF.delete(0.0, END)
        self.wyjscieCHF.insert(0.0, str(round(c/4.61 , 4)))

    def przeliczEUR(self):
        c = self.sprawdz_kwote()
        self.wyjscieEUR.delete(0.0, END)
        self.wyjscieEUR.insert(0.0, str(round(c/4.7, 4)))

    def przeliczUSD(self):
        c = self.sprawdz_kwote()
        self.wyjscieUSD.delete(0.0, END)
        self.wyjscieUSD.insert(0.0, str(round(c/4.52, 4)))

    def przeliczGBP(self):
        c = self.sprawdz_kwote()
        self.wyjscieGBP.delete(0.0, END)
        self.wyjscieGBP.insert(0.0, str(round(c/5.49, 4)))

k = Kantor()