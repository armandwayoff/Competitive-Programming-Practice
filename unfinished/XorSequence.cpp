long xorSequence(long l, long r) {
   int arr[r] = {0};
   for (int i = 1; i <= r; i++) {
      arr[i]  = arr[i - 1] ^ i;
   }
   long result = arr[l];
   for (int i = l + 1; i <= r; i++) {
      result ^= arr[i];
   }
   return result;
}
