int missingNumber(int* nums, int numsSize) {
    int arrXor = 0;
    for (int i = 0; i < numsSize; i++) {
        arrXor ^= nums[i] ^ (i+1);
    }
    return arrXor;
}