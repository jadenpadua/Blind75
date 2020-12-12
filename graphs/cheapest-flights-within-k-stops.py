class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for f in flights:
            s, d, p = f[0], f[1], f[2]
            graph[s].append((d, p))
        
        best = float('inf')
        queue = collections.deque([(src, 0, -1)])
        # the items in queue record the current city, the current total price, and the current number of stops
        
        priceMap = {}
        # the priceMap record the best total price from src to the 'key' city during traversal
        # this is critical for early pruning
        while queue:
            curr = queue.popleft()
            # check whether the number of stops has exceeeded the limit K or not
            if curr[2] > K:
                break
            # if we find a route to the dst, we update the best price so far, and we we stop continuing along this route
            if curr[0] == dst:
                best = min(best, curr[1])  
            # else, we continue the traversal
            else:
                for (nex, price) in graph[curr[0]]:
                    # if we have previously seen nex, and current total price is larger than previously recorded price,
					# then we don't need to continue along this route (early pruning)
                    if nex not in priceMap or priceMap[nex] > price + curr[1]:
                        priceMap[nex] = price + curr[1]
                        queue.append((nex, price + curr[1], curr[2] + 1))
            
        return best if best < float('inf') else -1
            
