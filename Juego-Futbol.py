print("JUEGO DE FÚTBOL")
print("Cada partido es diferente\n")
import random

score = 0

nivel1 = [
{"pregunta":"¿Cuántos jugadores hay en un equipo de fútbol?","opciones":"A) 10  B) 11  C) 12","respuesta":"B"},
{"pregunta":"¿Qué color tiene el Real Madrid?","opciones":"A) Blanco  B) Azul  C) Rojo","respuesta":"A"},
{"pregunta":"¿Qué deporte se juega con balón y portería?","opciones":"A) Fútbol  B) Tenis  C) Golf","respuesta":"A"},
{"pregunta":"¿Cuántas partes tiene un partido de fútbol reglamentario?","opciones":"A) 1  B) 2  C) 3","respuesta":"B"},
{"pregunta":"¿Qué país ganó el Mundial 2010?","opciones":"A) Italia  B) España  C) Alemania","respuesta":"B"},
{"pregunta":"¿Qué se usa para jugar al fútbol?","opciones":"A) Raqueta  B) Balón  C) Disco","respuesta":"B"},
{"pregunta":"¿Cuánto dura un partido sin prórroga?","opciones":"A) 90 min  B) 80 min  C) 100 min","respuesta":"A"},
{"pregunta":"¿Qué equipo es de Barcelona?","opciones":"A) Real Madrid  B) Barça  C) Sevilla","respuesta":"B"},
{"pregunta":"¿Qué parte del cuerpo no se usa en fútbol (portero aparte)?","opciones":"A) Manos  B) Cabeza  C) Piernas","respuesta":"A"},
{"pregunta":"¿Cuántas sustituciones se permiten actualmente por equipo en partidos oficiales de fútbol?","opciones":"A) 3  B) 5  C) 7","respuesta":"B"}
]

nivel2 = [
    {"pregunta": "¿Qué entrenador ganó la Champions con Chelsea en 2021?", "opciones": "A) Tuchel  B) Klopp  C) Guardiola", "respuesta": "A"},
    {"pregunta": "¿Qué país ganó el Mundial 2018?", "opciones": "A) Brasil  B) Francia  C) Alemania", "respuesta": "B"},
    {"pregunta": "¿Dónde jugaba Neymar antes del PSG?", "opciones": "A) Barcelona  B) Milan  C) United", "respuesta": "A"},
    {"pregunta": "¿Cuántas Champions tiene el Real Madrid (aprox.)?", "opciones": "A) 10  B) 15  C) 7", "respuesta": "B"},
    {"pregunta": "¿Qué país organizó el Mundial 2014?", "opciones": "A) Brasil  B) Rusia  C) Qatar", "respuesta": "A"},
    {"pregunta": "¿Qué liga es la Premier League?", "opciones": "A) España  B) Inglaterra  C) Italia", "respuesta": "B"},
    {"pregunta": "¿Qué jugador es conocido como 'CR7'?", "opciones": "A) Cristiano Ronaldo  B) Ronaldo Nazario  C) Ribéry", "respuesta": "A"},
    {"pregunta": "¿Qué equipo es el AC Milan?", "opciones": "A) Inglaterra  B) Italia  C) Francia", "respuesta": "B"},
    {"pregunta": "¿Cuántos cambios permite el fútbol moderno (aprox.)?", "opciones": "A) 3  B) 5  C) 7", "respuesta": "B"},
    {"pregunta": "¿Qué color viste el FC Barcelona?", "opciones": "A) Azul y rojo  B) Verde  C) Negro", "respuesta": "A"}
]

nivel3 = [
    {"pregunta": "¿Quién ganó el Balón de Oro 2007?", "opciones": "A) Kaká  B) Messi  C) Cristiano", "respuesta": "A"},
    {"pregunta": "Máximo goleador histórico de la Champions?", "opciones": "A) Messi  B) Cristiano Ronaldo  C) Lewandowski", "respuesta": "B"},
    {"pregunta": "¿Qué país eliminó a España en 2014?", "opciones": "A) Chile  B) Holanda  C) Brasil", "respuesta": "A"},
    {"pregunta": "¿En qué club debutó Messi?", "opciones": "A) Barcelona  B) Newell's  C) PSG", "respuesta": "A"},
    {"pregunta": "¿Qué jugador ganó más Mundiales?", "opciones": "A) Pelé  B) Messi  C) Maradona", "respuesta": "A"},
    {"pregunta": "¿Qué equipo ganó la Champions 2022?", "opciones": "A) Liverpool  B) Real Madrid  C) Bayern", "respuesta": "B"},
    {"pregunta": "¿Dónde se jugó el Mundial 2022?", "opciones": "A) Qatar  B) Rusia  C) Brasil", "respuesta": "A"},
    {"pregunta": "¿Qué portero es famoso por 'La parada del siglo' (Maradona)?", "opciones": "A) Shilton  B) Buffon  C) Neuer", "respuesta": "A"},
    {"pregunta": "¿Qué equipo tiene más ligas españolas?", "opciones": "A) Barcelona  B) Real Madrid  C) Atlético", "respuesta": "B"},
    {"pregunta": "¿Qué país ganó la Eurocopa 2020?", "opciones": "A) Italia  B) Inglaterra  C) Francia", "respuesta": "A"}
]

print("\n🟢 NIVEL 1 - CALENTAMIENTO")
print("-------------------------")
for p in random.sample(nivel1,4):
    print("\n" + p["pregunta"])
    print(p["opciones"])

    respuesta = input("Tu respuesta: ").upper()

    if respuesta == p["respuesta"]:
        print("✅ Correcto!")
        score += 1
    else:
        print("❌ Incorrecto")

print("\n🟡 NIVEL 2 - PARTIDO SERIO")
print("-------------------------")
for p in random.sample(nivel2,4):
    print("\n" + p["pregunta"])
    print(p["opciones"])

    respuesta = input("Tu respuesta: ").upper()

    if respuesta == p["respuesta"]:
        print("✅ Correcto!")
        score += 1
    else:
        print("❌ Incorrecto")

print("\n🔴 NIVEL 3 - MODO LEYENDA")
print("-------------------------")

for p in random.sample(nivel3,4):
    print("\n" + p["pregunta"])
    print(p["opciones"])

    respuesta = input("Tu respuesta: ").upper()

    if respuesta == p["respuesta"]:
        print("✅ Correcto!")
        score += 1
    else:
        print("❌ Incorrecto")

print("\n🏁 FIN DEL PARTIDO 🏁")
print("----------------------")
print("Tu puntuación:", score, "/ 12") 

if score >= 9:
    print("Nivel: Leyenda del fútbol")
elif score >= 6:
    print("Nivel: Buen fan")
else:
    print("Nivel: Aficionado")