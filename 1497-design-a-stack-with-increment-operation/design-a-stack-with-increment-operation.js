/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.maxSize = maxSize;
    this.stack = [];


    
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if(this.maxSize > this.stack.length) {
        this.stack.push(x);
    }
    
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    if(this.stack.length) {
        return this.stack.pop();
    } else {
        return -1
    }
    
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    for(let i = 0; i < Math.min(k, this.stack.length); i++) {
        this.stack[i] += val
    }
    
};

/** 
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */