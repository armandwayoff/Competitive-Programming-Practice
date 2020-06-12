string counterGame(long n) {
   int count = 0;
   while (n > 1) {
      if ((n & (n - 1)) == 0) {
         n /= 2;
         count++;
      } else {
         n -= (1 << int(log2(n)));
         count++;
      }
   }
   if (count % 2 == 0) {
      return "Richard";
   } else {
      return "Louise";
   }
}
