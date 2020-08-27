if ("$ENV{HI3559_SDK_ROOT}" STREQUAL "")
    message(FATAL_ERROR "HI3559_SDK_ROOT not set
    Please set HI3559_SDK_ROOT as following...
        export HI3559_SDK_ROOT=/media/hhd2/lvjianfeng/hisi3559/Hi3559V200_MobileCam_SDK_V1.0.1.5"
    )
endif()

set(CMAKE_C_COMPILER arm-himix100-linux-gcc)
set(CMAKE_CXX_COMPILER arm-himix100-linux-g++)
set(CMAKE_LINKER arm-himix100-linux-ld)
set(CMAKE_AR arm-himix100-linux-ar)

add_definitions(-D__arm__ -DHISI_CHIP -D__HI3559V200__ -D_FILE_OFFSET_BITS=64
                -D_LARGE_FILE -D_LARGEFILE64_SOURCE -DMW_VERSION=\"2.0.1.0\"
                -DENABLE_PROC -DENABLE_LOG -DENABLE_AUDIO -DFILE_FALLOCATE_ENABLE -DLOSCFG_PLATFORM_HISI_AMP -D__HI3559V200__  -D__DualSys__
                -DLANE_DIVIDE_MODE=LANE_DIVIDE_MODE_0 -DCFG_LANE_DIVIDE_MODE_0
                -DSENSOR_IMX458 -DCFG_SENSOR_TYPE0=IMX458 -DSENSOR_UNUSED -DCFG_SENSOR_TYPE1=UNUSED -DCFG_SENSOR_TYPE2=UNUSED -DCFG_SENSOR_TYPE3=UNUSED
                -DCFG_SENSOR_TYPE4=UNUSED -DCFG_SENSOR_TYPE5=UNUSED -DCFG_SENSOR_TYPE6=UNUSED  -DCFG_SENSOR_TYPE7=UNUSED
                -DSUPPORT_DIS -DSUPPORT_HDMI -DSUPPORT_RECORDVQE -DSUPPORT_H264 -DSUPPORT_H265 -DMAPI_LOG_ALL)

add_compile_options(-mcpu=cortex-a7 -mfloat-abi=softfp -mfpu=neon-vfpv4 -Wall -Werror
        -O2 -fstack-protector-all -fPIC -ffunction-sections)