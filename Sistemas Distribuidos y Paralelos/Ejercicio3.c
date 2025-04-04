#include <stdio.h>
#include <omp.h>

int main() {
    printf("\nCantidad de Procesadores: %d ", omp_get_num_procs());
    omp_set_num_threads(8);
    
    #pragma omp parallel
    {   
        #pragma omp single
        {
            printf("Cantidad de Hilos listos para usar: %d\n", omp_get_num_threads());
        }
    }

    
    printf("\nCon Schedule estatico\n");
    // Distribuye las iteraciones en bloques (chunk_size) de manera equitativa entre los hilos
    #pragma omp parallel for schedule(static, 2)
        for (int i = 0; i < 16; i++) {
            printf("Hilo %d ejecuta i = %d\n", omp_get_thread_num(), i);
        }

    //Cada hilo toma la siguiente tarea disponible dinámicamente.
    printf("\nCon Schedule dinamico\n");
    #pragma omp parallel for schedule(dynamic, 2)
        for (int i = 0; i < 10; i++) {
            printf("Hilo %d ejecuta i = %d\n", omp_get_thread_num(), i);
        }

    //Asigna iteraciones en bloques grandes al principio y más pequeños después.
    printf("\nCon Schedule guiado\n");
    #pragma omp parallel for schedule(guided, 2)
        for (int i = 0; i < 10; i++) {
            printf("Hilo %d ejecuta i = %d\n", omp_get_thread_num(), i);
        }
    
    //El compilador elige automáticamente la mejor estrategia.
    printf("\nCon Schedule auto\n");
    #pragma omp parallel for schedule(auto)
        for (int i = 0; i < 10; i++) {
            printf("Hilo %d ejecuta i = %d\n", omp_get_thread_num(), i);
        }
    return 0;
}
