/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    let add = 0 ;
    while(num > 9) {
        add=0;
        for(let val of `${num}`) {
            add += +val;

        }
        num = `${add}`
        
    }
    return +num;
    
};
