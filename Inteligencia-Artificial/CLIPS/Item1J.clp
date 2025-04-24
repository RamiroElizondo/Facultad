; Item1
; Realice un programa que a partir de los siguientes hechos, y utilizando una regla sume los valores y muestre el resultado
; (load "D:\\Facultad\\4to-Anio\\1er-Semestre\\IA\\Ejercicios-Clips\\Item1.clp")
(deffacts BD
    (valor 21)
    (valor 52)
    (valor 13)
)

(defrule sumarNum
   (valor ?x)
   (valor ?y)
   (valor ?z)
   =>
   (bind ?suma (+ ?x ?y ?z))
   (printout t "El resultado es:" ?suma crlf))
   
(defrule sumarNumxyzDistintos
   (valor ?x)
   (valor ?y&:(neq ?y ?x))
   (valor ?z&:(and (neq ?y ?z) (neq ?x ?z)))
   =>
   (bind ?suma (+ ?x ?y ?z))
   (printout t "El resultado cuando x="?x" ;y="?y" ;z= "?z" :" ?suma crlf))

