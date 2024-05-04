package main

// 268. Missing Number
func missingNumber(nums []int) int {
	n := len(nums)
	totalSum := (n * (n + 1)) / 2
	numsSum := 0
	for i := 0; i < n; i++ {
		numsSum += nums[i]
	}
	return totalSum - numsSum
}

//func main() {
//	nums := []int{1}
//	fmt.Println(missingNumber(nums))
//}
