;(load "C:\\Users\\Ramiro\\OneDrive\\Documentos\\GitHub\\Facultad\\Inteligencia-Artificial\\CLIPS\\ejercicio2-1-JarrasHeuristica.clp")
; Estado inicial
(defrule estadoinicial
  =>
  (assert (estado 24 0 0 0))
  (assert (jarra 1 24))
  (assert (jarra 2 5))
  (assert (jarra 3 11))
  (assert (jarra 4 13))
)

; Función que cuenta cuántas jarras tienen 8 litros y devuelve el total
; Se le pasa como parámetro el estado actual de las jarras
(deffunction contar ($?estados)
  (bind ?cont 0)
  (loop-for-count (?i 1 4) do
    (if (= (nth$ ?i ?estados) 8) then 
      (bind ?cont (+ ?cont 1))
    )
  )
  (return ?cont)
)


; Función que realiza el movimiento de una jarra a otra
; Se le pasa como parámetro el número de la jarra origen, el número de la jarra destino,
; la capacidad de la jarra destino y el estado actual de las jarras
(deffunction general (?jarraOrigen ?jarraDestino ?capacidadDestino ?valores)
  (bind ?x (nth$ ?jarraOrigen ?valores))
  (bind ?y (nth$ ?jarraDestino ?valores))
  (bind ?movimiento (min ?x (- ?capacidadDestino ?y)))
  (bind ?nuevoX (- ?x ?movimiento))
  (bind ?nuevoY (+ ?y ?movimiento))
  (bind ?nuevoEstado (replace$ ?valores ?jarraOrigen ?jarraOrigen ?nuevoX))
  (bind ?nuevoEstado (replace$ ?nuevoEstado ?jarraDestino ?jarraDestino ?nuevoY))
  (assert (estado $?nuevoEstado))
)

; ------- Reglas de volcado con salience según la heurística -------
; Se priorizan los hechos que tengan mas jarras con 8 litros, y luego los que tengan menos jarras con 8 litros

; Regla para volcar de jarra a jarra, si hay 2 jarras con 8 litros
(defrule volcar-s2
  (declare (salience 20))
  ?estado <- (estado $?valores)
  (jarra ?jarraOrigen ?capacidadOrigen)
  (jarra ?jarraDestino ?capacidadDestino)
  ; Si la jarra origen tiene 0 litros, no se puede volcar
  (test (neq (nth$ ?jarraOrigen ?valores) 0))
  ; Si la jarra origen tiene 8 litros, no la usamos
  (test (neq (nth$ ?jarraOrigen ?valores) 8))
  ; Si la jarra destino tiene 8 litros, no la usamos
  (test (neq (nth$ ?jarraDestino ?valores) 8))
  ; Si la jarra origen y destino son diferentes
  (test (neq ?jarraOrigen ?jarraDestino))
  (test (= (contar ?valores) 2))
  =>
  ; Llamamos a la función general para realizar el movimiento
  (general ?jarraOrigen ?jarraDestino ?capacidadDestino ?valores)
  (printout t "[S2] Moviendo de jarra " ?jarraOrigen " a jarra " ?jarraDestino crlf)
)

; Regla para volcar de jarra a jarra, si hay 1 jarras con 8 litros
(defrule volcar-s1
  (declare (salience 10))
  ?estado <- (estado $?valores)
  (jarra ?jarraOrigen ?capacidadOrigen)
  (jarra ?jarraDestino ?capacidadDestino)
  (test (neq (nth$ ?jarraOrigen ?valores) 0))
  (test (neq (nth$ ?jarraOrigen ?valores) 8))
  (test (neq (nth$ ?jarraDestino ?valores) 8))
  (test (neq ?jarraOrigen ?jarraDestino))
  (test (= (contar ?valores) 1))
  =>
  (general ?jarraOrigen ?jarraDestino ?capacidadDestino ?valores)
  (printout t "[S1] Moviendo de jarra " ?jarraOrigen " a jarra " ?jarraDestino crlf)
)

; Regla para volcar de jarra a jarra, si hay 0 jarras con 8 litros
(defrule volcar-s0
  (declare (salience 0))
  ?estado <- (estado $?valores)
  (jarra ?jarraOrigen ?capacidadOrigen)
  (jarra ?jarraDestino ?capacidadDestino)
  (test (neq (nth$ ?jarraOrigen ?valores) 0))
  (test (neq ?jarraOrigen ?jarraDestino))
  (test (= (contar ?valores) 0))
  =>
  (general ?jarraOrigen ?jarraDestino ?capacidadDestino ?valores)
  (printout t "[S0] Moviendo de jarra " ?jarraOrigen " a jarra " ?jarraDestino crlf)
)

; Estado final con salience muy alto para que se dispare apenas se alcance
(defrule estadofinal
  (declare (salience 1000))
  (estado 8 0 8 8)
  =>
  (printout t "Estado final alcanzado: (8 0 8 8)" crlf)
  (halt)
)
