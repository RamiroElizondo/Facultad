;Realice un programa que a partir de los siguientes hechos, y utilizando una 
;regla sume los valores y muestre el resultado
;(elemento (valor 21))
;(elemento (valor 52))
;(elemento (valor 13))
;C:/Users/Ramiro/OneDrive/Documentos/GitHub/Facultad/Inteligencia-Artificial/CLIPS/item1.clp
(deftemplate elemento
   (slot valor))

(deffacts elementos
   (elemento (valor 21))
   (elemento (valor 52))
   (elemento (valor 13)))

(defrule sumarNum
   (valor ?x)
   (valor ?y)
   (valor ?z)
   =>
   (bind ?suma (+ ?x ?y ?z))
   (printout t "El resultado es:" ?suma crlf))
   
(defrule suma-elementos
    ?e1 <- (elemento (valor ?v1))
    ?e2 <- (elemento (valor ?v2&:(neq ?v2 ?v1)))
    ?e3 <- (elemento (valor ?v3&:(and (neq ?v3 ?v1) (neq ?v3 ?v2))))
    =>
    (bind ?suma (+ ?v1 ?v2 ?v3))
    (printout t "La suma de los elementos es: " ?suma crlf))