package main

import (
	"fmt"
	"net"
	"net/http"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("Request at %v\n", time.Now())
	proxyIP, _, _ := net.SplitHostPort(r.RemoteAddr)
	realIP := r.Header.Get("X-Real-Ip")
	fmt.Fprintf(w, "real: %sproxy: %s", realIP, proxyIP)
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":9090", nil)
}
