/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    let obj = {}
    s1.split(' ').forEach(item => {
        obj[item] = (obj[item] || 0)+ 1;
    })
    s2.split(' ').forEach(item => {
        obj[item] = (obj[item] || 0)+ 1;
    })
    console.log(obj)
    result = []
    for(let val in obj) {
        if(obj[val] == 1) result.push(val)
    }
    
    return result;
};