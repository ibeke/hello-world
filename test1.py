import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np

# Fájl beolvasása és adatok DataFrame-be való konvertálása
file_path = 'meresi_adatok.txt'
delimiter = ';'  # Az adatokat ';' választja el

# Bootstrap ismétlődések száma
bootstrap_iterations = 100000


# Adatok beolvasása és elnevezése
data = pd.read_csv(file_path, sep=delimiter, names=['Ido', 'Meres'])

# Listák az ismétlődő mintavételekkel számított hibák tárolásához
bootstrap_errors = []

start_time = time.time()  # Kezdeti időmérés

for _ in range(bootstrap_iterations):
    # Véletlenszerű mintavétel az eredeti adatokból (ismétlődés engedélyezve)
    bootstrap_sample = data.sample(n=len(data), replace=True)
    
    # Az ismétlődő mintavétel hibájának kiszámítása
    sample_std_deviation = bootstrap_sample['Meres'].std()
    bootstrap_errors.append(sample_std_deviation)

end_time = time.time()  # Vége időmérésnek

# Az ismétlődő mintavételekkel kiszámolt hibák átlaga és szórása
bootstrap_mean_error = np.mean(bootstrap_errors)
bootstrap_std_deviation_error = np.std(bootstrap_errors)

# Eredmények kiíratása
print(f'Bootstrap módszerrel becsült hiba: {bootstrap_mean_error}')
print(f'Standard hiba a Bootstrap hibájából: {bootstrap_std_deviation_error}')

# Futási idő megjelenítése
run_time = end_time - start_time
print(f'Futási idő: {run_time:.4f} másodperc')
