#include <stdio.h>
#include <math.h>

int collatz(int x) {
    if (x % 2 == 0) {
        x = x / 2;
        printf("Принимает чётное, возвращает нечётное число: %d\n", x);
        return x;
    }
    else {
        x = x * 3 + 1;
        printf("Принимает нечётное, возвращает чётное число: %d\n", x);
        return x;
    }
}

double exponential_growth(int init_population, double growth_rate, int time) {
    double population = init_population * pow(2, time / growth_rate);
    return population;
}

double exponential_decay(int initial_amount, double half_life, int time) {
    double result = initial_amount * pow(0.5, (time / half_life));
    return result;
}
