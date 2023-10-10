// Can you translate this driver code to unit tests?

const assert = require('assert');
const pal = require('./palindrome');

assert.strictEqual(pal.palindrome('racecar'), true);
assert.strictEqual(pal.palindrome('Noon'), true);
assert.strictEqual(pal.palindrome('ciVic'), true);
assert.strictEqual(pal.palindrome('nice'), false);
assert.strictEqual(pal.palindrome(434), true);
assert.strictEqual(pal.palindrome(123), false);

// console.log("The following should be true if you're trying to do the extra portion of this challenge");
assert.strictEqual(pal.palindrome("Sore was I ere I saw Eros."), true);
assert.strictEqual(pal.palindrome("A man, a plan, a canal -- Panama"), true);

console.log("All tests passed!");
