ENV_VERIFY:
	@if [ -z "${HI3559_SDK_ROOT}" ] ; then\
		(echo "please setenv HI3559_SDK_ROOT first!") && false; \
	fi

.DEFAULT_GOAL := all

all: ENV_VERIFY clean
	@mkdir -p build && cd build && cmake -DCMAKE_TOOLCHAIN_FILE=../arm-himix.cmake .. && make

.PHONY: clean
clean:
	@rm -rf build

