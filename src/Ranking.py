#Funcion para calcular los puntos de un jugador
def calcular_puntos(kills, assists, deaths):
    return (kills * 3) + (assists) - (deaths)
#Funcion para calcular el MVP de una ronda
def calcular_mvp(ronda):
    mvp = None
    max_puntos = -1
    for jugador, stats in ronda.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = stats['deaths']
        puntos = calcular_puntos(kills, assists, deaths)
        if puntos > max_puntos:
            max_puntos = puntos
            mvp = jugador
    return mvp
#incializar el diccionario de jugadores
def inicializar_jugadores():
    jugadores = {}
    for jugador in ['Shadow', 'Blaze', 'Viper', 'Frost', 'Reaper']:
        jugadores[jugador] = {
            'kills': 0,
            'assists': 0,
            'deaths': 0,
            'mvp_count': 0,
            'total_points': 0
        }
    return jugadores

#Actualizar el diccionario de jugadores con los resultados de una ronda
def actualizar_jugadores(jugadores, ronda):
    for jugador, stats in ronda.items():
        jugadores[jugador]['kills'] += stats['kills']
        jugadores[jugador]['assists'] += stats['assists']
        jugadores[jugador]['deaths'] += int(stats['deaths'])
        if jugador == calcular_mvp(ronda):
            jugadores[jugador]['mvp_count'] += 1
        jugadores[jugador]['total_points'] = calcular_puntos(jugadores[jugador]['kills'], jugadores[jugador]['assists'], jugadores[jugador]['deaths'])
    return jugadores



#Programa principal
def Ranking(rounds):
    jugadores = inicializar_jugadores()
    for i, ronda in enumerate(rounds):
        jugadores = actualizar_jugadores(jugadores, ronda)
        mvp_ronda = calcular_mvp(ronda)
        
        # Ordenar jugadores por puntos totales en orden decreciente
        jugadores_ordenados = sorted(jugadores.items(), key=lambda x: x[1]['total_points'], reverse=True)

        if i == 4:
            print("Ranking final:")
        else:
            print(f"\nResultados de la ronda {i + 1}:")
        print(f"MVP de la ronda: {mvp_ronda}")
        print("Jugador      Kills      Asistencias      Muertes      MVPs      Puntos")
        print("------------------------------------------------------------------------------")
        for jugador, stats in jugadores_ordenados:
            print(jugador, "      ", stats['kills'], "             ", stats['assists'], "          ", stats['deaths'], "          ", stats['mvp_count'], "         ", stats['total_points'])
        print("------------------------------------------------------------------------------")
