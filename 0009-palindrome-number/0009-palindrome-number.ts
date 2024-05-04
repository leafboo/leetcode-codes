function isPalindrome(x: number): boolean {
     // Convert the integer to a string
    const str = x.toString();
    
    // Initialize pointers for the start and end of the string
    let left = 0;
    let right = str.length - 1;
    
    // Continue checking until the pointers meet
    while (left < right) {
        // If characters at left and right pointers are not equal, it's not a palindrome
        if (str[left] !== str[right]) {
            return false;
        }
        // Move the pointers towards the center
        left++;
        right--;
    }
    
    // If the loop completes, the string is a palindrome
    return true;
};
// 12345
// 1221
// 11
