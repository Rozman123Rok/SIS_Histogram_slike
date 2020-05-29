# Histogram slike
V tej nalogi implementirajte svoje funkcije za izračun histograma.

Pripravite Python skripto, ki ima definirane naslednje funkcije:

## def RGB_hist(slika):

- funkcija prejme barvno sliko
- slika je tabela oblike (H, W, 3), tipa numpy.uint8
- funkcija vrne tabelo vektorjev z vednostmi histograma za rdečo, zeleno in modro barvo (256, 3)
 
## def GRAY_hist(slika):

- funkcija prejme sivinsko sliko sliko
- slika je tabela oblike (H, W), tipa numpy.uint8
- funkcija vrne tabelo vektorjev z vednostmi histograma za sivine (256, 1)

Pripravite še odsek kode katero lahko lahko samostojno zaženete kot demo:

## if __name__ == '__main__':

- pripravite demo katerega lahko poženete
  - print("Modul za izdelavo histograma slike!")