int singleNumber(int* nums, int numsSize) {
    int cache = 0;
    for (int i = 0; i < numsSize; i++) {
        cache = cache ^ nums[i];
    }
    return cache;
}