//      aprox. benchmark:
//      1 speed: 70000/s
//      2 speed: 18000/s
//      3 speed: 2080/s
//      4 speed: 136/s
//      5 speed: 8/s
//      6 speed: 0.6/s
//      7 speed: 0.036/s
//      8 speed: 0.002/s

package main

import (
        "crypto/md5"
        "fmt"
        "os"
        "runtime"
        "strconv"
        "sync"
        "time"
)

var (
        num   int64
        mutex sync.Mutex
        wg    sync.WaitGroup
        found int64
        start time.Time
)

func main() {
        var num_string = (os.Args[1])
        num, _ = strconv.ParseInt(num_string, 10, 64)
        start = time.Now()
        for i := 0; i < runtime.NumCPU(); i++ {
                wg.Add(1)
                go findHash()
        }
        wg.Wait()
        fmt.Println("Total found: ", found)
}

func findHash() {
        for {
                mutex.Lock()
                var currentNum = num
                num++
                mutex.Unlock()

                // convert number to string
                var numStr = strconv.FormatInt(currentNum, 10)

                // generate sha256 hash of the string "dark7void_" + number
                var hash = md5.Sum([]byte("dark7void_" + numStr))
                // convert hash to string and check if it starts with 6 zeros

                if hash[0] == 0 && hash[1] == 0 && hash[2] == 0 /* && hash[3] < 16 */ {
                        var hashStr = fmt.Sprintf("%x", hash)
                        println("------------------------")
                        fmt.Println("Found:", "dark7void_"+numStr)
                        fmt.Println("Hash:", hashStr)
                        mutex.Lock()
                        found++
                        var end = time.Now()
                        var diff = end.Sub(start)
                        var nseconds = diff.Nanoseconds()
                        var hps float64 = float64(found) / (float64(nseconds) / 1000000000)
                        fmt.Printf("Hashes per second: %f\n", hps)
                        mutex.Unlock()
                }
        }
        wg.Done()
}
