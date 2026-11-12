FROM golang:1.24-alpine AS build
WORKDIR /src
COPY main.go .
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /hola main.go

FROM alpine:3.21
COPY --from=build /hola /hola
CMD ["/hola"]
