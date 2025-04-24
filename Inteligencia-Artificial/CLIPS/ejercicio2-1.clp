;2.1) Problemas de jarras:
;a) Representar, en reglas, el conocimiento que permite realizar los diferentes movimientos de líquidos entra jarras 
;y sus llenados y vaciamiento.
;b) Realizar todo es espacio de búsqueda (ForwarChaining) numerando los nodos en una búsqueda hacia lo profundo y 
;hacia lo ancho.
;c) En cada forma de búsqueda exprese los pasos hasta encontrar la solución.
;d) Utilice y explique una heurística que le permita moverse solamente por el camino más promisorio!!
;e) Realice una implementación en Clips que le permita encontrar la solución con alguna de las instancias ciegas y 
;con la heurística propuesta en el punto d) Marque las diferencias en los tiempos de ejecución.
;De qué modo podrías dividir el contenido de una jarra de 24 litros en tres partes iguales, utilizando solamente la 
;jarra original y otras tres de 5, 11 y 13 litros de capacidad respectivamente.(0,65)
;(load "C:\\Users\\Ramiro\\OneDrive\\Documentos\\GitHub\\Facultad\\Inteligencia-Artificial\\CLIPS\\ejercicio2-1-jarras.clp")

(deftemplate jarra
    (slot contenido (type INTEGER)(default ?NONE))
    (slot capacidad (type INTEGER)(default ?DERIVE))
)

(deftemplate estado
    (slot x (type INTEGER)(default 0))
    (slot y (type INTEGER)(default 0))
    (slot z (type INTEGER)(default 0))
    (slot w (type INTEGER)(default 0))
)

(deffacts jarras
    (jarra (contenido 24)(capacidad 24))
    (jarra (contenido 0)(capacidad 5))
    (jarra (contenido 0)(capacidad 11))
    (jarra (contenido 0)(capacidad 13))
    (estado (x 0)(y 0)(z 0)(w 0))
)
;Movimientos Jarra 24 a Jarra 5
(defrule movimientos1
    ?j1 <- (jarra (contenido ?c1&:(>= ?c1 0))(capacidad 24))
    ?j2 <- (jarra (contenido ?c2&:(>= ?c2 0))(capacidad 5))
    ?estado <- (estado (x ?x)(y ?y)(z ?z)(w ?w))
    => 
    (bind ?nuevoX (+ ?x (- ?c1 5)))
    (bind ?nuevoY (+ ?y 5))
    (modify ?j1 (contenido (- ?c1 5)))
    (modify ?j2 (contenido (+ ?c2 5)))
    (modify ?estado (x ?nuevoX)(y ?nuevoY))

    (printout t "Movimientos Jarra 24 a Jarra 5" crlf)
    (printout t "Jarra 24: " ?c1 " Jarra 5: " (+ ?c2 5) crlf)
    (printout t "Estado: " ?nuevoX " " ?nuevoY " " ?z " " ?w crlf)
    (printout t "------------------------" crlf)
)
    