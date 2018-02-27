# step 1:
### commit: create training files

faccio il merge dei valori tra i file contenuti nelle cartelle mocapfiles e emo_evaluation creando i csv nella cartella output 

# step2:
### commit: trim output

elimino dai csv nella cartella output i frame che non appartengono ai singoli chunk con i label emotivi; e elimino anche le colonne del csv relative a numero_frame, time e i tre valori activation, valence, dominance in quanto non utili ai fini della classificazione

# step 3:
### commit: average trimmed output
faccio la media dei valori delle colonne per creare un unico array di valori per ogni chunk ( mi sembra che poria abbia fatto più o meno così)



