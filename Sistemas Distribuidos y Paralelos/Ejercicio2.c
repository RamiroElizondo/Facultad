#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>


int main(void){
    int valor = 0;

    #pragma omp parallel
    {
        int id = omp_get_thread_num(); // Obtener el ID del hilo actual
        valor += 1; // Incrementar el valor en cada hilo
        printf("Valor en el hilo %d: %d\n", id, valor); // Mostrar el valor en cada hilo
    }

    printf("Valor final: %d\n", valor);
    int valor2;
    int cont = 0;
    while (cont != 10){
        printf("Hola");
        #pragma omp parallel private(valor2)
        {
            valor2 = 0;
            unsigned int seed = omp_get_thread_num();
            srand(time(NULL) + seed * 100);
            valor2 += rand() % 100;
            printf("Valor en el hilo %d: %d\n", seed, valor2); // Mostrar el valor en cada hilo
        }
        cont++;
    }
    return 0;
}