#! /bin/sh

NAME=helloworld
VERSION=1.0.0
DIST=${NAME}-${VERSION}

# refer from https://pod.hatenablog.com/entry/2017/06/13/150342
__make_dist_file() {
	echo "create dist/${DIST}_${1}_${2}.tar.gz ...."
	mkdir -p dist/${1}_${2}/${DIST}/bin
	GOOS=$1 GOARCH=$2 go build -o dist/${1}_${2}/${DIST}/bin/${NAME}${3} ./main.go
	cp -r README.md LICENSE dist/${1}_${2}/${DIST}
	tar cfz dist/${DIST}_${1}_${2}.tar.gz -C dist/${1}_${2} ${DIST}
	echo "done."
}

__make_dist_file "darwin"  "amd64"
__make_dist_file "darwin"  "arm64"
__make_dist_file "windows" "amd64"
__make_dist_file "windows" "arm64"
__make_dist_file "linux"   "amd64"
__make_dist_file "linux"   "arm64"
