long theGreatXor(long x) {
    long count = 0;
    for (int i = 1; i < x; i++) {
        if ((x ^ i) > x) {
            count++;
        }
    }
    return count;
}
