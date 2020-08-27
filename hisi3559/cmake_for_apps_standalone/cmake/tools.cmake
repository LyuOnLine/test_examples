macro(simple_imported_target target_name type prefix)
    if( ${type} STREQUAL "STATIC" )
        set(__libname ${prefix}/lib${target_name}.a)
    elseif( ${type} STREQUAL "SHARED")
        set(__libname ${prefix}/lib${target_name}.so)
    else()
        message(FATAL_ERROR "Not supported type: ${type}")
    endif()
    add_library(${target_name} UNKNOWN IMPORTED)
    set_target_properties(${target_name} PROPERTIES
        IMPORTED_LOCATION ${__libname}
        IMPORTED_LINK_INTERFACE_MULTIPLICITY 10
        LINK_INTERFACE_MULTIPLICITY 10
    )
endmacro()