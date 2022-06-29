# RandNSumK

Generates an array of N random, whole numbers whose sum is K, where N > 1 and K > 0.

I mostly use this for percentages; for example, given 100(K) assorted fruits of 3(N) different types, 29 are apples, 41 are oranges, and 30 are peaches.

I've done testing on over 10 million iterations of the same K and N values, and they always summed to K and averaged to a K/N value. If you wish to have the results closer to K/N, you can write a wrapper method that adds multiple arrays together, element by element, then dividing the final array's elements by the number of added arrays (hereby X). This will likely result in decimal values, and given a high X, the values may not perfectly add to K (one of the values tend to be something like 31.0000000001, but the other two are not decimals).
[23, 71, 6]
[48, 35, 17]
++++++++++++
[71, 106, 23]
/2/2/2/2/2/2/2
[35.5, 53, 11.5] = 100
