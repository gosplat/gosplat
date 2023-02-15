build:
	go build . 

updateDependencies:
	git submodule update --init --recursive

install: 
	bash install.sh
