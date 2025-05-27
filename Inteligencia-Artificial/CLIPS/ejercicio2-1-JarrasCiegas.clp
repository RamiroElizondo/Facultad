;(load "C:\\Users\\Ramiro\\OneDrive\\Documentos\\GitHub\\Facultad\\Inteligencia-Artificial\\CLIPS\\ejercicio2-1-JarrasCiegas.clp")
(defrule estadoinicial
    ;Definimos el estado inicial de las jarras
    ;Definimos cada jarra
    =>
    (assert (estado 24 0 0 0))
    (assert (jarra 1 24))
    (assert (jarra 2 5))
    (assert (jarra 3 11))
    (assert (jarra 4 13))
)

(defrule volcar
    ;Regla para volcar el contenido de una jarra a otra
    ;Obtenemos el estado actual de las jarras
    ?estado <- (estado $?valores)
    
    ;Obtenemos la jarra origen y destino, y sus capacidades
    (jarra ?jarraOrigen ?capacidadOrigen)
    (jarra ?jarraDestino ?capacidadDestino)

    ;Obtenemos el contenido de ambas jarras, desde el estado actual
    
    (test (neq (nth$ ?jarraOrigen ?valores) 0))
    (test (neq ?jarraOrigen ?jarraDestino))
    =>
    (bind ?x (nth$ ?jarraOrigen ?valores))
    (bind ?y (nth$ ?jarraDestino ?valores))
    
    (printout t "Jarra Origen Numero: " ?jarraOrigen " Su contenido: " ?x " Jarra Destino Numero: " ?jarraDestino " Su contenido: " ?y  crlf)
    
    ;Calculamos el movimiento a realizar, que es el mínimo entre la cantidad de líquido en la jarra origen y la capacidad de la jarra destino
    (bind ?movimiento (min ?x (- ?capacidadDestino ?y)))
    (bind ?nuevoX (- ?x ?movimiento))
    (bind ?nuevoY (+ ?y ?movimiento))

    ;;Actualizamos el estado de las jarras, reemplazando el contenido de la jarra origen y destino por el nuevo contenido
    (bind ?nuevoEstado (replace$ ?valores ?jarraOrigen ?jarraOrigen ?nuevoX))
    (bind ?nuevoEstado (replace$ ?nuevoEstado ?jarraDestino ?jarraDestino ?nuevoY))
    (assert (estado $?nuevoEstado))
    
)

(defrule estadofinal
    ;Regla para verificar si se ha alcanzado el estado final, le damos prioriedad a esta regla y terminamos el programa cuando llega el estado final
    (declare (salience 1000))
    (estado 8 0 8 8)
    =>
    (printout t "Estado final alcanzado: (8 0 8 8)" crlf)
    (halt)
)
