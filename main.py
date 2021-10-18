def citireLista():
    l = []
    givenString = input("Dati elementele listei, separate prin virgula: ")
    numbersAsString = givenString(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def concatenare(l):
    '''
    afiseaza numarul format prin concatenarea numerelor din lista
    :param l: lista de numere intregi
    :return: numarul format
    '''
    for x in l:
        res = int("".join(map(str, l)))
    print(l)


def sumaMinMax(l):
    '''
    determina suma dintre cel mai mare si cel mai mic numar din lista
    :param l: lista de numere intregi
    :return: suma dintre minim si maxim
    '''
    y = 0
    z = 0
    for x in l:
        y = min(l)
        z = max(l)
    print(int(y + z))


def test_sumaMinMax():
    assert sumaMinMax([10, -3, 25, -1, 3, 25, 18]) == 22
    assert sumaMinMax([0, 56, 23, 8, 100]) == 100
    assert sumaMinMax([5, 8, -10, 10]) == 0


def sumaCifrelor(l, k, rezultat=[]):
    '''
    calculeaza suma cifelor numerelor din lista sile returneaza pe cele care au suma mai mare sau egala cu un nr dat
    :param l: lista de numere
    :return: numerele care au suma cifrelor mai mare sau egala cu un nr dat
    '''
    sumaCifre = 0
    for x in l:
        copy = x
        rezultat == []
        while copy:
            sumaCifre = sumaCifre + copy % 10
            copy = copy / 10
        if sumaCifre > k or sumaCifre == k:
            rezultat.append(x)


def test_sumaCifrelor(l, k):
    assert sumaCifrelor([25, 11, 10, 24, 39], 7) == [25, 39]
    assert sumaCifrelor([56, 4, 13], 4) == [4, 13]
    assert sumaCifrelor([55, 91, 19], 10) == [55, 91, 19]


def main():
    test_sumaMinMax()
    test_sumaCifrelor()
    test_sumaMinMax()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afisarea numarului obtinut prin concatenare")
        print("3. Afisare suma dintre cel mai mic si cel mai mare numar din lista")
        print("4. Afisare numerele din lista care au suma cifrelor mai mare sau egala cu un mr dat")

        optiune = input("Dati optiunea: ")

        if optiune == '1':
            l = citireLista()
        elif optiune == '2':
            print(concatenare(l))
        elif optiune == '3':
            print(sumaMinMax())
        elif optiune == '4':
            k = int(input('Dati un nr.: '))
            print(sumaCifrelor())


main()
