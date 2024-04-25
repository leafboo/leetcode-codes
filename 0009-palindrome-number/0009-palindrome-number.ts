function isPalindrome(x: number): boolean {
    const stringNumber = x.toString();

    let left = 0;
    let right = stringNumber.length - 1;

    while(left < right) {
        if (stringNumber[left] !== stringNumber[right]) {
            return false
        }
        left++;
        right--;
    }

    return true;
};