#include <stdio.h>

long long maximumTripletValue(int* nums, int numsSize) {
    if (numsSize < 3) return 0; // Edge case: At least 3 elements are needed

    long long maxVal = 0;
    int maxPrefix[numsSize]; // To store max nums[i] seen so far
    int maxSuffix[numsSize]; // To store max nums[k] from right

    // Compute prefix max (max nums[i] seen so far)
    maxPrefix[0] = nums[0];
    for (int i = 1; i < numsSize; i++) {
        maxPrefix[i] = (nums[i] > maxPrefix[i - 1]) ? nums[i] : maxPrefix[i - 1];
    }

    // Compute suffix max (max nums[k] from the right)
    maxSuffix[numsSize - 1] = nums[numsSize - 1];
    for (int k = numsSize - 2; k >= 0; k--) {
        maxSuffix[k] = (nums[k] > maxSuffix[k + 1]) ? nums[k] : maxSuffix[k + 1];
    }

    // Iterate through possible j values (middle element)
    for (int j = 1; j < numsSize - 1; j++) {
        long long diff = maxPrefix[j - 1] - nums[j]; // (nums[i] - nums[j])
        if (diff > 0) {
            long long res = diff * maxSuffix[j + 1]; // (nums[i] - nums[j]) * nums[k]
            if (res > maxVal) {
                maxVal = res;
            }
        }
    }

    return maxVal;
}