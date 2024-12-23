package main

import (
	"fmt"
)

func findMaxRecursive(prices []int, index int) int {
    if index == len(prices)-1 {
        return prices[index]
    }
    maxRest := findMaxRecursive(prices, index+1)
    if prices[index] > maxRest {
        return prices[index]
    }
    return maxRest
}

func findHighestBid(bid []int) int {

	if len(bid) == 0 {
		panic("tidak ada tawaran yang tersedia")
	}

	highestBid := bid[0]
	for i := 0; i < len(bid); i++ {
		if bid[i] > highestBid {
			highestBid = bid[i]
		}
	}

	return highestBid
}

func main() {
	tawaran := []int{5478347, 2036212, 6314665, 5960549, 6723070, 6617103, 7619257, 8110738, 8295414,
		6561101, 9724660, 5159416, 2007685, 1999631, 4236631, 4979046, 2565918, 9727834,
		7604379, 8930135, 9290564, 6813089, 8284082, 7354843, 4050657, 3245247, 3460083,
		5041304, 8954357, 4567129, 2259858, 5198457, 3080519, 6166033, 5145029, 7369333,
		2461038, 1384166, 3953980, 8683653, 8909956, 1613607, 4653718, 4620678, 3214299,
		5359704, 6145858, 2680357, 4037929, 5764306, 6947103, 8112162, 3592811, 4037367,
		7314225, 5255208, 9024744, 4009872, 9727190, 4969443, 4578960, 8256965, 5689216,
		8772133, 5060872, 4380698, 2280345, 4543940, 6279150, 7518486, 7043518, 8857683,
		4395196, 6483604, 4697782, 4917703, 2188396, 6178844, 5674445, 1317377, 9337108,
		1111982, 1409567, 9326064, 7435273, 5445850, 6661456, 7788475, 1946458, 4469162,
		2237776, 5841771, 6334621, 2563923, 4525733, 4694893, 7343971, 6173087, 5160124,
		7503392}

	highest := findHighestBid(tawaran)

	fmt.Printf("The highest bid is: %d\n", highest)

}
