// Solution from Cloverleaf :

long andProduct(long a, long b) {
    return a & ~((1 << (int)log2(a ^ b)) - 1);
}
// explanation : https://www.hackerrank.com/challenges/and-product/forum/comments/174194

// My original attempt:
// 5 errors (Your code did not execute within the time limits)

long andProduct(long a, long b) {
    long ans = a;
    for (int i = a + 1; i < b + 1; i++) {
        if ((i & (i - 1)) != 0) {
            ans &= i;
        } else {
            return 0;
        }
    }
    return ans;
}
