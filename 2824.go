package main

import (
	"fmt"
	"sort"
)

// todo Count Pairs Whose Sum is Less than Target

func countPairs(nums []int, target int) int {
	count := 0
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] < target {
				fmt.Println(nums[i], nums[j])
				count++
				fmt.Println(count)
			}
		}
	}
	return count
}

//-1 2
//-1 3
//-1 4
//-1 6
//-1 7
//2 3
//2 4
//3 4
