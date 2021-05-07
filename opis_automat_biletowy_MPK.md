

#Link do repozytorium
https://github.com/KacperMroz/Automat_biletowy

##TEMAT NR 1 


###Opis zadania

- Automat przechowuje informacje o monetach/banknotach znajdujących się w
nim (1,2, 5. 10, 20. 50gr, 1, 2. 5, 10, 20, 50zł) [dziedziczenie: można napisać
uniwersalną klasę PrzechowywaczMonet po której dziedziczyć będzie automat]
- Okno z listą biletów w różnych cenach (jako przyciski). Wymagane bilety:
20-minutowy, 40-minutowy, 60-minulowy w wariantach normalnym i ulgowym.
-Możliwość wybrania więcej niż jednego rodzaju biletu. Możliwość
wprowadzenia liczby biletów.
- Po wybraniu biletu pojawia się okno z listą monet (przyciski) oraz możliwoscią dodania kolejnego biletu lub liczby biletow.
- Interfejs ma dodatkowo zawierać pole na wybór liczby wrzucanych monet (domyślnie jedna).

- Po wrzuceniu monet, których wartość jest większa lub równa cenie wybranych biletów, automat sprawdza czy może wydać resztę.

    - Brak reszty/moze wydać: wyskakuje okienko z informacją o zakupach. wydaje
    resztę (dolicza wrzucone monety. odlicza wydane jako reszta), wraca do
    wyboru biletów.

    - Nie może wydać: wyskakuje okienko z napisem "Tylko odliczona kwota" oraz zwraca wlożone monety.

Testy

1. Bilet kupiony za odliczona kwotę - oczekiwany brak reszty.

2. Bilet kupiony placąc więcej - oczekiwana reszta.

3. Bilet kupiony placac więcej, automat nie ma jak wydać reszty - oczekiwana informacja o blędzie oraz zwrócenie takiej samej liczby monet o tych samych nominalach, co wrzucone.

4. Zakup biletu placąc po 1gr - suma stu monet 1gr ma być równa 1zł(dla floatów  suma sto razy 0.01+0.O1+...+0.01 nie będzie równa 1.0). Platności można dokonać za pomoca pętli for w interpreterze.

5. Zakup dwóch różnych biletów naraz - cena powinna być suma.

6. Dodanie biletu, wrzucenie kilku monet, dodanie drugiego biletu, wrzucenie pozostalych monet. Zakup za odliczona kwotę - oczekiwany brak reszty (wrzucone monety nie zeruja się po dodaniu biletu).

7. Proba wrzucenia ujemnej oraz niecałkowitej liczby monet (oczekiwany komunikat  o błędzie).