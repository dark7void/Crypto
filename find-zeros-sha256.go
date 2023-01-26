package main

import (
    "crypto/sha256"
    "fmt"
    "runtime"
    "strconv"
    "sync"
    "time"
)

var (
    num int64 mutex sync.Mutex wg sync.WaitGroup found int64 start time.Time
)

func main() {
    start = time.Now()
    for i: = 0;
    i < runtime.NumCPU();
    i++{
        wg.Add(1)
        go findHash()
    }
    wg.Wait()
    fmt.Println("Total found: ", found)
}

func findHash() {
    for {
        mutex.Lock()
        currentNum: = num
        num++
        mutex.Unlock()

        numStr: = strconv.FormatInt(currentNum, 10)

        hash: = sha256.Sum256([] byte("dark7void_" + numStr))

        if hash[0] == 0 && hash[1] == 0 && hash[2] == 0 {
            hashStr: = fmt.Sprintf("%x", hash)
            fmt.Println("Number:", numStr)
            fmt.Println("SHA256:", hashStr)
            mutex.Lock()
            found++
            var end = time.Now()
            var diff = end.Sub(start)
            var nseconds = diff.Nanoseconds()
            fmt.Println(found, nseconds)
            var hps float64 = float64(found) / (float64(nseconds) / 1000000000)
            fmt.Printf("Hashes per second: %f\n", hps)
            mutex.Unlock()
        }
    }
    wg.Done()
}
