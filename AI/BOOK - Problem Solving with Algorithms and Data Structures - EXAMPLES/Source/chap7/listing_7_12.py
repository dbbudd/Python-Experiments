def recDC(coins,change,res):
   minCoins = change
   if change in coins:         res[change] = 1
      return 1
   elif res[change] > 0:       return res[change]
   else:
       for i in [c for c in coins if c <= change]:
         numCoins = 1 + recDC(coins,change-i,res)
         if numCoins < minCoins:
            minCoins = numCoins
            res[change] = minCoins
   return minCoins
