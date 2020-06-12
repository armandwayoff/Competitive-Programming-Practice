// 8 / 12

long sumXor(long n) {
   long count = 0;
   for (int i = 0; i <= n; i++) {
      if ((n + i) == (n ^ i)) {
         count++;
      }
   }
   return count;
}
