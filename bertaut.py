        import time
from threading import Thread, Lock
import sys
lock = Lock()
def animate_text(text, delay=0.00000001):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)
def sing_song():
    lyrics = [
        ("Bun,hidup berjalan seperti bajingan", 0.149),
        ("Seperti landak yang tak punya teman", 0.145),
        ("Ia menggonggong bak suara", 0.18),
        ("hujaaaaann",0.4),
        ("Dan kau pangeranku mengambil peran", 0.2),
        ("Bun,kalau saat hancur ku disayang", 0.17),
        ("Apalagi saat ku jadi juara", 0.2),
        ("Saat tak tau arah kau disana", 0.17),
        ("Menjadi gagah saat ku tak bisa", 0.17),
        ("Sedikit kujelaskan tentangku dan kamu", 0.17),
        ("Agar seisi dunia tau", 0.13),
        ("Keras kepalaku sama denganmu",0.15),
        ("Caraku marah caraku tersenyum",0.15),
        ("Seperti detak jantung yang bertaut",0.15),
        ("Nyawaku nyala karena denganmu",0.15),
        
    
    ]
    delays = [1.0, 10.0, 21.0,26.0, 31.0, 43.0,53.0, 64.0, 74.0,84.0,85.0,96.0,101.0,107.0,112.0]
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    sing_song()