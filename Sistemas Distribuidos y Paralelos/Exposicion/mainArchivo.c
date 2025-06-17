#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h> // Incluir biblioteca para booleanos
#include <omp.h>

#define N 1000  // Usar may�sculas para evitar conflictos con variables

// Prototipos de Función
void generarMatriz(int n, bool matriz[N][N]);
void generarVector(int n, bool vector[N]);
void productoMatrizVector(int n, bool matriz[N][N], bool vector[N], bool resultado[N]);
void imprimirMatriz(int n, bool matriz[N][N]);
void imprimirVector(int n, bool vector[N], char* nombre);

void generarMatriz(int n, bool matriz[N][N]) {
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matriz[i][j] = rand() % 2; // Valores true (1) o false (0)
        }
    }
}

void generarVector(int n, bool vector[N]) {
    for (int i = 0; i < n; i++) {
        vector[i] = rand() % 2; // Valores true (1) o false (0)
    }
}

void productoMatrizVector(int n, bool matriz[N][N], bool vector[N], bool resultado[N]) {
    #pragma omp parallel for
    for (int i = 0; i < n; i++) {
        resultado[i] = false;
        for (int j = 0; j < n; j++) {
            resultado[i] = resultado[i] || (matriz[i][j] && vector[j]);
        }
    }
}


void imprimirMatriz(int n, bool matriz[N][N]) {
    printf("Matriz (%dx%d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
}

void imprimirVector(int n, bool vector[N], char* nombre) {
    printf("%s:\n", nombre);
    for (int i = 0; i < n; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n");
}

int main() {
    bool matriz[N][N];
    bool vector[N];
    bool resultado[N];
    double inicio, fin;
    int band = 0;
    FILE *archivo = fopen("tiempos.txt", "a"); // modo append

    if (archivo == NULL) {
        perror("No se pudo abrir el archivo CSV");
        return 1;
    }
    // Escribir encabezado si el archivo está vacío
    fseek(archivo, 0, SEEK_END);
    if (ftell(archivo) == 0) {
        fprintf(archivo, "Hilos,Tiempo\n");
    }


    generarMatriz(N, matriz);
    generarVector(N, vector);

    #pragma omp parallel
    {
        #pragma omp single
        {
            printf("Cantidad de Hilos listos para usar: %d\n", omp_get_num_threads());
        }
    }
    while(band != 1){
        printf("Ingrese la cantidad de hilos a usar (1-12) 0 para terminar:");
        int hilos;
        scanf("%d", &hilos);
        if(hilos < 1 || hilos > 12){
            printf("Cantidad de hilos no valida o Ingreso Cero para terminar\n");
            band = 1;
        }else{
            omp_set_num_threads(hilos);

            inicio = omp_get_wtime();
            productoMatrizVector(N, matriz, vector, resultado);
            fin = omp_get_wtime();
            printf("Tiempo de ejecucion: %f segundos\n", fin - inicio);
            fprintf(archivo, "%d,%.10f\n", hilos, fin - inicio);
            //imprimirVector(N, resultado, "Resultado");
        }
    }
    fclose(archivo);
    return 0;
}
