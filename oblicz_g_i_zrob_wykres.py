import matplotlib.pyplot as plt
import numpy as np

def oblicz_g(h, l, t1_s, t1_k, t2_s, t2_k, fps):
    t1 = t1_s + t1_k / fps
    t2 = t2_s + t2_k / fps
    t = t2 - t1

    if t <= 0:
        raise ValueError("Czas koncowy musi byc mniejszy niz poczatkowy!")

    g = (14 * l ** 2) / (5 * h * t ** 2)
    return g

if __name__ == "__main__":
    # --- Stale ---
    DLUGOSC = 1.73  # metry
    FPS = 60  # klatek na sekunde

    # --- Dane dla 4 pomiarow ---
    pomiary = [
        (0.2, 6, 56, 9, 18),
        (0.5, 4, 1, 5, 27),
        (0.7, 4, 10, 5, 23),
        (1.0, 3, 42, 4, 39)
    ]

    wysokosci = []
    g_wartosci = []
    katy = []

    # --- Obliczenia ---
    for i, (wysokosc, t1s, t1k, t2s, t2k) in enumerate(pomiary, start=1):
        try:
            g_value = oblicz_g(wysokosc, DLUGOSC, t1s, t1k, t2s, t2k, FPS)
            theta = np.degrees(np.arcsin(wysokosc / DLUGOSC))
            print(f"Pomiar {i} dla h = {wysokosc} m (kąt ≈ {theta:.2f}°): g = {g_value:.2f} m/s^2")
            wysokosci.append(wysokosc)
            g_wartosci.append(g_value)
            katy.append(theta)
        except ValueError as e:
            print(f"Pomiar {i} dla h = {wysokosc} m: BLAD - {e}")

    # --- Wykres ---
    if wysokosci:
        plt.figure(figsize=(9, 5))
        plt.plot(wysokosci, g_wartosci, marker='o', label="Obliczone g")
        plt.axhline(y=9.81, color='red', linestyle='--', label="g = 9.81 m/s²")

        for x, y, h, theta in zip(wysokosci, g_wartosci, wysokosci, katy):
            plt.text(x, y + 0.3, f"{theta:.1f}°", ha='center', va='bottom', fontsize=9, color='black')

        plt.xlabel("Wysokość h [m]")
        plt.ylabel("Obliczone przyspieszenie g [m/s²]")
        plt.title("Zależność obliczonego g od wysokości (z kątem nachylenia)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
