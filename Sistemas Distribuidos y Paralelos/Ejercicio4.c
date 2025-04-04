#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#define N 100

/*oid cargarVectoresAleatorios(int vecto1[], int vecto2[]){
    srand(time(NULL));  // Inicializa la semilla de números aleatorios
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        vecto1[i] = rand() % 2;  // Genera 0 o 1
        vecto2[i] = rand() % 2;  // Genera 0 o 1
    }
}*/

void cargarVectoresAleatorios(int vecto1[], int vecto2[]){
    srand(time(NULL));  
    for (int i = 0; i < N; i++) {
        vecto1[i] = rand() % 100; 
        vecto2[i] = rand() % 100;  
    }
}

void sumarVectores(int vector1[N],int vector2[N],int resultado[N],int hilos){
    double inicio, fin; // Variables para almacenar el tiempo
    omp_set_num_threads(hilos);
    
    inicio = omp_get_wtime(); // Tomamos el tiempo antes de ejecutar el código paralelo
    
    #pragma omp parallel
    {
        #pragma omp single
        {
            printf("Cantidad de Hilos listos para usar: %d\n", omp_get_num_threads());
        }
        #pragma omp for schedule(static, 2)
        for(int i=0;i<N;i++){
            //printf("Hilo %d ejecuta i = %d\n", omp_get_thread_num(), i);
            resultado[i]= vector1[i]+vector2[i];
        }
    }
    fin = omp_get_wtime();
    printf("Tiempo de ejecucion: %f segundos\n", fin - inicio); 
}

void mostrarVectores(int vector1[N],int vector2[N],int resultado[N]){
    printf("Vector 1:\n");
    for(int i=0;i<N;i++){
        printf("%d ",vector1[i]);
    }
    printf("\nVector 2:\n");
    for(int i=0;i<N;i++){
        printf("%d ",vector2[i]);
    }
    printf("\nResultado:\n");
    for(int i=0;i<N;i++){
        printf("%d ",resultado[i]);
    }
}

int main(void){
    int vecto1[N];
    int vecto2[N];
    int resultado[N];
    int band = 0;

    cargarVectoresAleatorios(vecto1, vecto2);
    while(band != 1){
        printf("Ingrese la cantidad de hilos a usar (1-12) 0 para terminar:");
        int hilos;
        scanf("%d", &hilos);
        if(hilos < 1 || hilos > 12){
            printf("Cantidad de hilos no valida o Ingreso Cero para terminar\n");
            band = 1;
        }else{
            sumarVectores(vecto1, vecto2, resultado,hilos);
            //mostrarVectores(vecto1, vecto2, resultado);
        }
    }
    return 0;
}