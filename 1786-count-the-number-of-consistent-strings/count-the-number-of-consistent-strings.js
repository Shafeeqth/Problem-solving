/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function (allowed, words) {
    allowed = new Set(allowed);
    return words.reduce((acc, item) => {
        let set = Array.from(new Set(item))
        
        return (set.every(item => allowed.has(item))) ? acc + 1 : acc;


    }, 0)



};