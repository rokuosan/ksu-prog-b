FROM golang:1.19-bullseye AS builder

ADD . /go/helloworld
WORKDIR /go/helloworld
RUN go build -o helloworld main.go

FROM scratch

COPY --from=builder /go/helloworld/helloworld /usr/bin/helloworld

ENTRYPOINT [ "/usr/bin/helloworld" ]
