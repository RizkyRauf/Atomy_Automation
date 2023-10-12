# utils.py
import random

def select_random_index(options):
    jumlah_pilihan = len(options)
    indeks_acak = random.randint(1, jumlah_pilihan - 1)
    return indeks_acak