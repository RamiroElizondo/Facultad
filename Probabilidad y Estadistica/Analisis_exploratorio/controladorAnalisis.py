import Analisis_exploratorio.analisisExploratorio as ae

class ControladorAnalisis:
    
    def __init__(self,ruta_csv):
        """
        Inicializa la clase cargando el dataset.
        """
        
        self.analisis = ae(ruta_csv)

   
        

    def mostrar_info(self):
        self.analisis.mostrar_info()
    
    def estadisticas_descriptivas(self):
        self.analisis.estadisticas_descriptivas()
    
    def histograma(self, columna):
        self.analisis.histograma(columna)
    
    def boxplot(self, columna):
        self.analisis.boxplot(columna)
    
    def matriz_correlacion(self):
        self.analisis.matriz_correlacion()
    
    def detectar_valores_nulos(self):
        self.analisis.detectar_valores_nulos()
    
    def detectar_valores_atipicos(self, columna):
        self.analisis.detectar_valores_atipicos(columna)

if __name__ == "__main__":
    controlador = ControladorAnalisis("biased_leukemia_dataset.csv")
    controlador.menu() 