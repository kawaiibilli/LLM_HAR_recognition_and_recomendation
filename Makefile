IMAGE=app
CONTAINER=app_cont
ENV_FILE=.env

build:
	docker build -t $(IMAGE) .
run:
	docker run --rm --name $(CONTAINER) --env-file=$(ENV_FILE) -p 8989:8989 $(IMAGE)
stop:
	docker stop $(CONTAINER)
clean:
	docker rm -f $(CONTAINER)
	docker rmi $(IMAGE)
all: build run
