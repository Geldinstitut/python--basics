import multiprocessing

def burner():
    # Endlosschleife ohne Gnade
    while True:
        x = 1234.567678 ** 9.0123676767

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print(f"Hütte brennt. Stopp: Strg C")

    #alle kerne ansprechen
    processes = []
    for _ in range(cores):
        p = multiprocessing.Process(target=burner)
        p.start()
        processes.append(p)
