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
    DLUGOSC = 1.75  # metry
    FPS = 60  # klatek na sekunde

    # --- Dane dla 4 pomiarow ---
    pomiary = [
        (0.2, 6, 56, 9, 18),
        (0.5, 4, 1, 5, 27),
        (0.7, 4, 10, 5, 23),
        (1.0, 3, 42, 4, 39)
    ]

    # --- Obliczenia ---
    for i, (wysokosc, t1s, t1k, t2s, t2k) in enumerate(pomiary, start=1):
        try:
            g_value = oblicz_g(wysokosc, DLUGOSC, t1s, t1k, t2s, t2k, FPS)
            print(f"Pomiar {i} dla h = {wysokosc} m: g = {g_value:.2f} m/s^2")
        except ValueError as e:
            print(f"Pomiar {i} dla h = {wysokosc} m: BLAD - {e}")
