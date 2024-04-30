package main

//75. Sort Colors

// bubble sort
func sortColors(nums []int) {
	var isdone bool
	for !isdone {
		isdone = true
		for i := 0; i < len(nums)-1; i++ {
			if nums[i] > nums[i+1] {
				nums[i], nums[i+1] = nums[i+1], nums[i]
				isdone = false
			}
		}
	}
}
