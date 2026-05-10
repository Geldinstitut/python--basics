import multiprocessing

def burner():
    # Endlosschleife ohne Gnade
    while True:
        x = 1234.5678 ** 9.0123

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print(f"Brutzel-Modus auf {cores} Kernen aktiv!")
    print("STOPPEN MIT: STRG + C")
    
    processes = []
    for _ in range(cores):
        p = multiprocessing.Process(target=burner)
        p.start()
        processes.append(p)