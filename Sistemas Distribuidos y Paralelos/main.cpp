#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 4  // Tamaño de la matriz y el vector

// Función para cargar la matriz manualmente
void cargarMatrizManual(int matriz[N][N]) {
    printf("Ingrese los valores de la matriz (0 o 1):\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &matriz[i][j]);
            // Validar que solo se ingresen 0s y 1s
            while (matriz[i][j] != 0 && matriz[i][j] != 1) {
                printf("Valor inválido. Ingrese 0 o 1: ");
                scanf("%d", &matriz[i][j]);
            }
        }
    }
}

// Función para cargar la matriz de forma aleatoria
void cargarMatrizAleatoria(int matriz[N][N]) {
    srand(time(NULL));  // Inicializa la semilla de números aleatorios
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            matriz[i][j] = rand() % 2;  // Genera 0 o 1
        }
    }
}

// Función para imprimir la matriz
void imprimirMatriz(int matriz[N][N]) {
    printf("Matriz:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
}

// Función para multiplicar la matriz booleana por un vector booleano
void multiplicarMatrizVector(int matriz[N][N], int vector[N], int resultado[N]) {
    for (int i = 0; i < N; i++) {
        resultado[i] = 0;
        for (int j = 0; j < N; j++) {
            resultado[i] |= (matriz[i][j] && vector[j]);
        }
    }
}

// Función para imprimir un vector
void imprimirVector(int vector[N]) {
    for (int i = 0; i < N; i++) {
        printf("%d\n", vector[i]);
    }
}

int main() {
    int matriz[N][N];
    int vector[N] = {1, 0, 1, 0};  // Vector de ejemplo (puede modificarse)
    int resultado[N];
    int opcion;

    printf("Seleccione el metodo de carga de la matriz:\n");
    printf("1 - Carga manual\n");
    printf("2 - Carga aleatoria\n");
    scanf("%d", &opcion);

    if (opcion == 1) {
        cargarMatrizManual(matriz);
    } else if (opcion == 2) {
        cargarMatrizAleatoria(matriz);
    } else {
        printf("Opción inválida. Saliendo del programa.\n");
        return 1;
    }

    imprimirMatriz(matriz);
    
    multiplicarMatrizVector(matriz, vector, resultado);

    printf("Resultado de la multiplicación:\n");
    imprimirVector(resultado);

    return 0;
}
