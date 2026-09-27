WatchInfo = "H34 is a samsung watch, it's price is 35 USD"
print(WatchInfo)
print(type(WatchInfo)) 

print(" Upper: " , WatchInfo.upper() )
print(" Lower:" , WatchInfo.lower() )
print(" Swap:" , WatchInfo.swapcase() )
print(" Tittle:" , WatchInfo.title() )
print(" Capitalize:" , WatchInfo.capitalize() ) 

Vendor = WatchInfo[10:17:1]
print(Vendor)

print(len(WatchInfo))
print(len(Vendor))

for x in WatchInfo:
    print(x)
    


