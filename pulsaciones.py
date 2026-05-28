seguir=1
while(seguir==1):
    while True:
        try:
            pulsaciones=int(input('Pulsaciones detectadas'))
            break
        except ValueError:
            print('Error, escriba un número entero')
        
    movimiento=bool
    while True:
        try:
            detector_movimiento=int(input('Detección de movimiento'))
            if detector_movimiento==0 or detector_movimiento==1:
                break
            else:
                print('Error, escriba 1 o 0')
        except ValueError:
            print('Escriba un número entero (1 o 0)')

    if detector_movimiento==1:
        movimiento=True
    elif detector_movimiento==0:
        movimiento=False

    if pulsaciones==0:
        print('PARADA CARDíACA')
    elif pulsaciones>60 and pulsaciones<=100:
        print('Paciente estable')
    else:
        if movimiento==True:
            print('Falso positivo por movimiento, ignorar alarma')
        else:
            print('ALERTA MÉDICA. Ritmo irregular detectado')
    while True:
        try:
           seguir=int(input('¿Continuar simulación?'))
           if seguir==0 or seguir==1:
               break
           else:
               print('Error, escriba 1 o 0')
        except ValueError:
            print('Error, escriba un número entero')
        
print('Lectura finalizada')