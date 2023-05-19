from pydub import AudioSegment
a = AudioSegment.from_file("audio.wav")
b=float(input("Введите коэффициент ускорения:"))
a1 = a.speedup(b)
a1.export('audio1.wav', format= "wav")