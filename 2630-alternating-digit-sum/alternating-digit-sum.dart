class Solution {
  int alternateDigitSum(int n) {
    int result = 0;
    var strN = n.toString();
    for(var i = 0; i < strN.length; i++) {
        i % 2 == 0 ? result += int.tryParse(strN[i])!: result -= int.tryParse(strN[i])!;
    }
    return result ;
    
  }
}