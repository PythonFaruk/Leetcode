int hammingWeight(int n) {
    int num = n;
    int sum = 0;
    while (num > 0) {
        printf("Aktuelle Nummer: %d \n", num);
        printf("Summe :%d \n", sum);
        if (num % 2 == 1){
            sum = sum + 1;
        }
        num = num >> 1;
    }
    return sum;
}