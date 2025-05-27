; Templates
(deftemplate persona
    (slot nombre (type STRING))
    (slot edad (type INTEGER))
    (slot profesion (type SYMBOL))
    (slot estado_civil (type SYMBOL))
    (slot estado_jubilacion (type SYMBOL)))

(deftemplate hombre
    (slot nombre (type STRING)))

(deftemplate mujer
    (slot nombre (type STRING)))

; Template para el hecho ordenado de docentes a jubilar
(deftemplate docente-a-jubilar
    (slot nombre (type STRING))
    (slot edad (type INTEGER)))

; b) Regla para mostrar mujeres solteras docentes próximas a jubilarse
(defrule mostrar-docentes-proximas-jubilacion
    "Regla que identifica mujeres solteras docentes próximas a jubilarse"
    (persona (nombre ?nombre) 
             (edad ?edad&:(>= ?edad 59)) 
             (profesion docente) 
             (estado_civil soltera) 
             (estado_jubilacion FALSE))
    (mujer (nombre ?nombre))
    =>
    ; Mostrar información por pantalla
    (printout t "Docente próxima a jubilarse: " ?nombre 
                ", Edad: " ?edad " años" crlf)
    ; Agregar nuevo hecho ordenado a la memoria de trabajo
    (assert (docente-a-jubilar (nombre ?nombre) (edad ?edad))))

; c) Hechos en la Memoria de Trabajo para verificar la regla

; Hechos de personas
(deffacts personas-ejemplo
    ; Mujeres docentes que cumplen los criterios
    (persona (nombre "Maria Rodriguez") (edad 60) (profesion docente) (estado_civil soltera) (estado_jubilacion FALSE))
    (persona (nombre "Ana Garcia") (edad 59) (profesion docente) (estado_civil soltera) (estado_jubilacion FALSE))
    (persona (nombre "Carmen Lopez") (edad 62) (profesion docente) (estado_civil soltera) (estado_jubilacion FALSE))
    
    ; Mujeres docentes que NO cumplen los criterios (para verificar que la regla filtra correctamente)
    (persona (nombre "Sofia Martinez") (edad 58) (profesion docente) (estado_civil soltera) (estado_jubilacion FALSE)) ; Edad < 59
    (persona (nombre "Elena Fernandez") (edad 61) (profesion docente) (estado_civil casada) (estado_jubilacion FALSE)) ; No soltera
    (persona (nombre "Isabel Ruiz") (edad 60) (profesion enfermera) (estado_civil soltera) (estado_jubilacion FALSE)) ; No docente
    (persona (nombre "Lucia Torres") (edad 63) (profesion docente) (estado_civil soltera) (estado_jubilacion TRUE)) ; Ya jubilada
    
    ; Hombres (para verificar que no se incluyen)
    (persona (nombre "Carlos Jimenez") (edad 61) (profesion docente) (estado_civil soltero) (estado_jubilacion FALSE))
    
    ; Hechos de género
    (mujer (nombre "Maria Rodriguez"))
    (mujer (nombre "Ana Garcia"))
    (mujer (nombre "Carmen Lopez"))
    (mujer (nombre "Sofia Martinez"))
    (mujer (nombre "Elena Fernandez"))
    (mujer (nombre "Isabel Ruiz"))
    (mujer (nombre "Lucia Torres"))
    (hombre (nombre "Carlos Jimenez")))

; Regla adicional para mostrar resumen de docentes a jubilar
(defrule mostrar-resumen-docentes
    "Regla para mostrar resumen final de docentes identificadas"
    (declare (salience -10)) ; Se ejecuta después de la regla principal
    =>
    (printout t crlf "=== RESUMEN DE DOCENTES PROXIMAS A JUBILARSE ===" crlf)
    (do-for-all-facts ((?f docente-a-jubilar))
        TRUE
        (printout t "- " ?f:nombre " (" ?f:edad " anios)" crlf))
    (printout t "=============================================" crlf))

; Comando para ejecutar el sistema
; Para probar: (reset) (run) (facts)