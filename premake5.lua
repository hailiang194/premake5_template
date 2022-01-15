workspace "HelloWorld"
  configurations { "Debug", "Release" }

project "HelloWorld"
  kind "ConsoleApp"
  language "C++"
  targetdir "bin/%{cfg.buildcfg}"

  files { "./HelloPremake/**.h", "./HelloPremake/**.cpp" }

  filter "configurations:Debug"
    defines { "DEBUG" }
    symbols "On"

  filter "configurations:Release"
    defines { "NDEBUG" }
    optimize "On"
