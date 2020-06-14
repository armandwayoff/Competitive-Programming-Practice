# 5 erreurs (Your code did not execute within the time limits)

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
