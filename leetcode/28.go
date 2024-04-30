package main

import (
	"fmt"
	"strings"
)

// 28. Find the Index of the First Occurrence in a String

func strStr(haystack string, needle string) int {
	for i := 0; i <= len(haystack)-len(needle); i++ {
		if haystack[i:i+len(needle)] == needle {
			return i
		}
	}
	return -1

}

func strStr2(haystack string, needle string) int {
	occurrence := false
	var index int
	hList := strings.Split(haystack, "")
	nList := strings.Split(needle, "")
	//var right, left string
	for i, letter := range hList {
		if letter == nList[i] {
			//left = letter
		}
	}
	fmt.Println(occurrence)
	return index

}
