def recMC(coins,change):
   minCoins = change
   if change in coins:         return 1
   else:
       for i in [c for c in coins if c <= change]:           numCoins = 1 + recMC(coins,change-i)           if numCoins < minCoins:
            minCoins = numCoins
   return minCoins
