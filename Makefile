#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = caa-aviation-data

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Clean downloaded data files
clean-all:
	rm -f src/data/**/*

clean:
	rm -f src/data/interim/* src/data/processed/*

build:
	docker build -f docker/prophet/prophet.dockerfile -t honir/prophet:latest ./docker/prophet

prophet:
	docker-compose up -d prophet

build-rprophet:
	docker build -f docker/rprophet/rprophet.dockerfile -t honir/rprophet:latest ./docker/rprophet

shell:
	docker-compose run --rm -w /usr/src/app prophet /bin/bash
