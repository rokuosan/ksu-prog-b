package main

import (
  "fmt"
  "os"
)

func goMain(args []string) int {
  if len(args) == 0 {
    fmt.Println("Hello World");
  } else {
    fmt.Printf("Hello, %s\n", args[0])
  }
  return 0
}

func main() {
  status := goMain(os.Args[1:])
  os.Exit(status)
}
