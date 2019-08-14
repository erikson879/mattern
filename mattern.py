#!/usr/bin/env python
nroProcesos = raw_input("Ingresar la cantidad de procesos >> ");
nroMensajes = raw_input("Ingresar la cantidad de mensajes >> ");
p = {};
for j in range(0,int(nroProcesos),+1):
    v= [];
    for i in range(0,int(nroProcesos),+1):
        v.append(0);
    p['p' + str(j+1)]= v
mensaje = 1;
while int(nroMensajes) >= mensaje:
    sender = raw_input("Proceso que envia mensaje numero "+ str(mensaje) +"   >> ");
    reciber = raw_input("Proceso que recibe mensaje numero "+ str(mensaje) +" >> ");
    if sender != reciber:
        getSender = p.get('p' + sender);
        getReciber = p.get('p'+ reciber);
        getSender[int(sender)-1] = getSender[int(sender)-1] + 1;
        getReciber[int(reciber)-1] = getReciber[int(reciber)-1] + 1;
        for i in range(0 , int(nroProcesos), +1):
             if getReciber[i] < getSender[i]:
                 getReciber[i] = getSender[i]
    else:
        getSender = p.get('p' + sender);
        print (getSender);
    mensaje = mensaje + 1;
for i in sorted(p.keys()):
    separador = ",";
    valor = i +"["+ separador.join(str(k) for k in p.get(i)) + "]";
    print(valor);
