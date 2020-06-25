long theGreatXor(long x) {
    return (pow(2, 64 - __builtin_clzll(x)) - x - 1);
}
