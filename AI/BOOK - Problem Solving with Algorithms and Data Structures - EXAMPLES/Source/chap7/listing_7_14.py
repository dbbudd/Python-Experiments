def dpMakeChange(coinList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinList if c <= cents]:  
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   coinDict = {}
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print thisCoin
      coin = coin - thisCoin
