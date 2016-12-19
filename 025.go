package main

import ("math"; "fmt")

var fibNumList map[int]uint64

func fib(n int) uint64 {
    fibNumCached, exists := fibNumList[n]
    if exists {
        return fibNumCached
    }
    if n <= 2 {
        fibNumList[n] = 1
        return 1
    }
    res := fib(n-1) + fib(n-2)
    fibNumList[n] = res
    return res
}

func main() {
    fibNumList = make(map[int]uint64)
    fibNumList[1] = 1
    fibNumList[2] = 1
    nDigits := 1000
    limit := uint64(math.Pow(10, float64(nDigits) - 1)) - 1    
    fmt.Printf("Límite superior para el FibNum: %d\n", limit)
    index := 1
    for {
        num := fib(index)
        if num > limit {
            fmt.Printf("F(%d) = %d\n", index, num)
            return
        }
        index++
    } 
}