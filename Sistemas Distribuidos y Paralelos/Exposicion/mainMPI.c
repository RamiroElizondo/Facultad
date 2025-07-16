#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <time.h>

#define N 10000

void productoMatrizVector(int filas, int columnas, int **matriz, int *vector, int *resultado){
    for (int i = 0; i < filas; i++) {
        resultado[i] = 0;
        for (int j = 0; j < columnas; j++) {
            resultado[i] += matriz[i][j] * vector[j];
        }
    }
}

int main(int argc, char *argv[]){
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int **matriz = NULL, *vector = NULL, *resultado = NULL;
    int **subMatriz, *subResultado;
    int filasPorProceso = N / size;

    if(rank == 0){
        srand(time(NULL));
        // Reservar memoria dinámica para la matriz y el vector
        matriz = malloc(N * sizeof(int*));
        for (int i = 0; i < N; i++) {
            matriz[i] = malloc(N * sizeof(int));
        }
        vector = malloc(N * sizeof(int));
        resultado = malloc(N * sizeof(int));

        // Inicializar matriz y vector de forma binaria (0 o 1)
        for (int i = 0; i < N; i++) {
            vector[i] = rand() % 2;
            for (int j = 0; j < N; j++) {
                matriz[i][j] = rand() % 2;
            }
        }
    } else {
        vector = malloc(N * sizeof(int));
    }

    // Reservar memoria para subMatriz y subResultado
    subMatriz = malloc(filasPorProceso * sizeof(int*));
    for (int i = 0; i < filasPorProceso; i++) {
        subMatriz[i] = malloc(N * sizeof(int));
    }
    subResultado = malloc(filasPorProceso * sizeof(int));

    // Enviar submatrices y vector a cada proceso
    if(rank == 0){
        int *flatMatrix = malloc(N * N * sizeof(int));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                flatMatrix[i * N + j] = matriz[i][j];
            }
        }
        MPI_Scatter(flatMatrix, filasPorProceso * N, MPI_INT,
                    &subMatriz[0][0], filasPorProceso * N, MPI_INT,
                    0, MPI_COMM_WORLD);
        free(flatMatrix);
    } else {
        MPI_Scatter(NULL, filasPorProceso * N, MPI_INT,
                    &subMatriz[0][0], filasPorProceso * N, MPI_INT,
                    0, MPI_COMM_WORLD);
    }

    MPI_Bcast(vector, N, MPI_INT, 0, MPI_COMM_WORLD);

    MPI_Barrier(MPI_COMM_WORLD); // sincroniza todos los procesos
    double start_time = MPI_Wtime();

    // Cada proceso calcula su parte
    productoMatrizVector(filasPorProceso, N, subMatriz, vector, subResultado);

    // Recolectar resultados parciales
    MPI_Gather(subResultado, filasPorProceso, MPI_INT,
               resultado, filasPorProceso, MPI_INT,
               0, MPI_COMM_WORLD);

    MPI_Barrier(MPI_COMM_WORLD); // sincroniza todos los procesos
    double end_time = MPI_Wtime();

    if(rank == 0){
        printf("\nTiempo de cálculo: %f segundos\n", end_time - start_time);
    }

    

    if(rank == 0){
        for (int i = 0; i < N; i++) {
            free(matriz[i]);
        }
        free(matriz);
        free(resultado);
    }

    MPI_Finalize();
    return 0;
}

