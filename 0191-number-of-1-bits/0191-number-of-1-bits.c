int hammingWeight(int n) {
    int num = n;
    int sum = 0;
    while (num > 0) {
        if (num % 2 == 1){
            sum = sum + 1;
        }
        num = num >> 1;
    }
    return sum;
}