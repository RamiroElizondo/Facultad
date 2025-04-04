#include <stdio.h>
#include <omp.h>

int main(void){

    printf("\nCantidad de Procesadores: %d ", omp_get_num_procs());
    printf("\nCantidad de Hilos listos para usar: %d ", omp_get_num_threads()); // muestra 1 solo, porque no esta dentro del bloque en paralelo
    printf("\nCantidad Maxima Hilos: %d ", omp_get_max_threads());
    printf("\nEl paralelismo anidado: %d", omp_get_nested());
    printf("\nParalelismo anidado disponible: %s\n", omp_get_nested() ? "Si" : "No");

    omp_set_num_threads(8);  // Cantidad de hilos a usar, esto tambien se puede indicar en la misma fila donde se abre la region paralela con num_threads()

    // Ejecutar una region paralela
    #pragma omp parallel num_threads(4)
    {
        printf("\nCantidad de Hilos listos para usar: %d ", omp_get_num_threads()); //esto se muestra por cada hilo activo
        int id = omp_get_thread_num();
        int total = omp_get_num_threads();
        printf("\nHola desde el hilo %d de %d\n", id, total);
    }

    return 0;
}
