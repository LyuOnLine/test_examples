set(_hisi_prefix $ENV{HI3559_SDK_ROOT}/reference/out/hi3559v200_actioncam_demb_imx458/lib/Linux)

simple_imported_target(securec STATIC ${_hisi_prefix})
simple_imported_target(datafifo_a7_linux STATIC ${_hisi_prefix})
simple_imported_target(mpi STATIC ${_hisi_prefix})
simple_imported_target(ipcmsg_a7_linux STATIC ${_hisi_prefix})
simple_imported_target(msg_client STATIC ${_hisi_prefix})
simple_imported_target(mbuf STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_acap_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_vcap_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_adec_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_aenc_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_ao_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_disp_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_log_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_msg_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_osd_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_sys_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_venc_client STATIC ${_hisi_prefix})
simple_imported_target(hi3559v200_mapi_vproc_client STATIC ${_hisi_prefix})



add_library(hisi_mpp INTERFACE IMPORTED)
set_property(TARGET hisi_mpp PROPERTY INTERFACE_LINK_LIBRARIES
    pthread
    mbuf
    msg_client

    hi3559v200_mapi_acap_client
    hi3559v200_mapi_vcap_client
    hi3559v200_mapi_adec_client
    hi3559v200_mapi_ao_client
    hi3559v200_mapi_osd_client
    hi3559v200_mapi_msg_client
    hi3559v200_mapi_disp_client
    ipcmsg_a7_linux
    hi3559v200_mapi_sys_client
    hi3559v200_mapi_vproc_client
    hi3559v200_mapi_msg_client     # circluar dependency
    hi3559v200_mapi_disp_client    # circluar dependency
    hi3559v200_mapi_venc_client
    hi3559v200_mapi_aenc_client
    hi3559v200_mapi_log_client
    datafifo_a7_linux
    mpi
    securec
    )
# include directories
execute_process(COMMAND find "$ENV{HI3559_SDK_ROOT}/middleware/ndk" -type d "\(" -name hi3559v200 -o -name include "\)"
    OUTPUT_VARIABLE _include_ndk)
#message("lvjf....${_include_ndk}")
string(REPLACE "\n" ";" _include_ndk ${_include_ndk})
execute_process(COMMAND bash -c "find $ENV{HI3559_SDK_ROOT}/middleware/common -name include -type d"
    OUTPUT_VARIABLE _include_middleware_common)
string(REPLACE "\n" ";" _include_middleware_common ${_include_middleware_common})
#mpp
set(_include_mpp $ENV{HI3559_SDK_ROOT}/amp/a7_linux/mpp/include
                $ENV{HI3559_SDK_ROOT}/amp/a7_liteos/mpp/include
                )
set_property(TARGET hisi_mpp PROPERTY
    INTERFACE_INCLUDE_DIRECTORIES
        ${_include_ndk}
        ${_include_middleware_common}
        ${_include_mpp}
)


simple_imported_target(rtspserver STATIC ${_hisi_prefix})
simple_imported_target(servercommon STATIC ${_hisi_prefix})

add_library(hisi_rtpserver INTERFACE IMPORTED)
set_property(TARGET hisi_rtpserver PROPERTY INTERFACE_LINK_LIBRARIES
    rtspserver
    servercommon
    mbuf
    securec
    )
# include directories
set_property(TARGET hisi_rtpserver PROPERTY INTERFACE_INCLUDE_DIRECTORIES
    $ENV{HI3559_SDK_ROOT}/middleware/sample/livestream/rtspserver/include
    $ENV{HI3559_SDK_ROOT}/middleware/sample/livestream/server_common/include/
)


simple_imported_target(nnie STATIC ${_hisi_prefix})
add_library(hisi_svp INTERFACE IMPORTED)
set_property(TARGET hisi_svp PROPERTY INTERFACE_LINK_LIBRARIES
    nnie
    securec
    )
# include directories
set_property(TARGET hisi_svp PROPERTY INTERFACE_INCLUDE_DIRECTORIES
    $ENV{HI3559_SDK_ROOT}/amp/a7_linux/mpp/include
)