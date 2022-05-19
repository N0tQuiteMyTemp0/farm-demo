# Odczyt danych z inwertera farmy PV.

## Uruchomienie przykładowej symulacji
```
python3 farm_app.py
```

## Założenia projektowe
- Jak najprostszy interfejs końcowego użytkownika. 
- Łatwe rozszerzanie naszego modułu o urządzenia nowego producenta.

## Implementacja
- Klasa abstrakcyjna ```Inverter``` definiująca ogólny szablon tego jak powinien wyglądać kod dla nowego urządzenia, aby był on kompatybilny z naszym modułem
    - dwie implementacje: ```InverterHdk125x5``` oraz ```InverterSbsc1175``` (aktulanie urządzenie Sbsc1175 zużywa dwa razy wicej energii, ale oczywiście łatwo możemy zakodować konkretne działanie odpowiednio przeładowując metody odbsługujące konkretne parametry

