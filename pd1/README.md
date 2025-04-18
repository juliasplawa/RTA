# Zadanie 1
Serwis API obsługujący adreds `/api/v1.0/predict`.

Przyjmuje dwie liczby `num1` i `num2`. Zwraca `1` jeśli ich suma jest większa od 5.8 i `0` wpp.

Aby zbudować kontener należy wykonać komendę:
```
docker build -t pd1 . 
```

Następnie należy go uruchomić komendą:
```
docker run -p 5000:5000 pd1
```

API wystawione jest na porcie `5000`.
