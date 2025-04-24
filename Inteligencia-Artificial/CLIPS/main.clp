; Definir una plantilla (estructura) para los síntomas
(deftemplate sintoma
   (slot nombre)
   (slot valor))

; Preguntar al usuario si tiene fiebre
(defrule preguntar-fiebre
   =>
   (printout t "¿Tienes fiebre? (si/no): ")
   (bind ?respuesta (read))
   (assert (sintoma (nombre fiebre) (valor ?respuesta))))

; Regla para quedarse en casa si tiene fiebre
(defrule quedarse-en-casa
   (sintoma (nombre fiebre) (valor si))
   =>
   (printout t "Tienes fiebre. Deberías quedarte en casa." crlf))

; Regla para salir si no tiene fiebre
(defrule salir
   (sintoma (nombre fiebre) (valor no))
   =>
   (printout t "No tienes fiebre. Puedes salir." crlf))

