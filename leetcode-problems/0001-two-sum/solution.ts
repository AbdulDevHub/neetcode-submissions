function twoSum(nums: number[], target: number): number[] {
    // Key: the number itself, Value: its index in the array
    const seenNumbers = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        const currentNum = nums[i];
        const complement = target - currentNum;

        // Check if the number we need has already been seen
        if (seenNumbers.has(complement)) {
            // Return the index of the complement and the current index
            return [seenNumbers.get(complement), i];
        }

        // Otherwise, store the current number and its index for future reference
        seenNumbers.set(currentNum, i);
    }

    // Return an empty array if no solution is found (per standard safety)
    return [];
}
