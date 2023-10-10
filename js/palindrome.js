exports.palindrome = function (string) {
    string = String(string)
   
    const newString = string.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()
    
    const reverseString = newString.split('').reverse().join('')

    return newString === reverseString
};

