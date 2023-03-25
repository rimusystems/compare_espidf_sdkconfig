# Compare an sdkconfig file to defaults

## Introduction
The ESP-IDF SDKConfig file is a configuration file used by the ESP-IDF (Espressif IoT Development Framework) to specify various configuration options for a project.

The purpose of the SDKConfig file is to provide a convenient way to configure the behavior of the ESP-IDF libraries and components used in a project. It contains a set of configuration options, each of which can be set to either a default value or a custom value. These configuration options can control things like which libraries and components are included in a project, which hardware peripherals are used, and how the code is optimized.

The SDKConfig file can be edited manually using a text editor, or it can be edited using the make menuconfig command in the ESP-IDF build system. The make menuconfig command provides a graphical interface for editing the SDKConfig file and selecting various configuration options.

Overall, the purpose of the SDKConfig file is to allow developers to easily customize and configure their ESP-IDF projects to meet their specific requirements, without having to manually modify the source code of the libraries and components used in the project.

## Purpose

## Script
This script takes two command line arguments: the path to the SDKConfig file and the path to the default SDKConfig file. It loads the default values from the default SDKConfig file and stores them in a dictionary. It then reads the contents of the SDKConfig file, compares each value to its default setting, and stores any non-default values in a dictionary. The script then prints the non-default values to the console.

To use this script, save it to a file (e.g. "compare_sdkconfig.py") in the same directory as your SDKConfig files, and run it from the command line using the following command:

`python compare_sdkconfig.py path/to/sdkconfig path/to/default_sdkconfig`

Replace "path/to/sdkconfig" and "path/to/default_sdkconfig" with the actual paths to your SDKConfig files. The script will output a list of any non-default values in the SDKConfig file, based on the default values in the default SDKConfig file.

```
>python compare_sdkconfig.py sdkconfig sdkconfig_default
CONFIG_ESPTOOLPY_FLASHSIZE: "4MB" (Default="2MB")
CONFIG_PARTITION_TABLE_CUSTOM: y (Default=n)
CONFIG_PARTITION_TABLE_CUSTOM_FILENAME: "min_spiffs.csv" (Default="partitions.csv")
CONFIG_PARTITION_TABLE_FILENAME: "min_spiffs.csv" (Default="partitions_singleapp.csv")
CONFIG_ESP_TLS_SERVER: y (Default=n)
CONFIG_ESP_HTTP_CLIENT_ENABLE_BASIC_AUTH: y (Default=n)
CONFIG_ESP_HTTP_CLIENT_ENABLE_DIGEST_AUTH: y (Default=n)
CONFIG_HTTPD_MAX_REQ_HDR_LEN: 4096 (Default=512)
CONFIG_HTTPD_MAX_URI_LEN: 1024 (Default=512)
CONFIG_HTTPD_WS_SUPPORT: y (Default=n)
CONFIG_ESP_HTTPS_SERVER_ENABLE: y (Default=n)
CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ: 240 (Default=160)
CONFIG_ESP_MAIN_TASK_STACK_SIZE: 7168 (Default=3584)
CONFIG_LOG_MAXIMUM_LEVEL_DEBUG: y (Default=n)
CONFIG_LOG_MAXIMUM_LEVEL: 4 (Default=3)
CONFIG_LOG_TIMESTAMP_SOURCE_SYSTEM: y (Default=n)
CONFIG_LWIP_MAX_SOCKETS: 16 (Default=10)
CONFIG_ESP32_DEFAULT_CPU_FREQ_MHZ: 240 (Default=160)
CONFIG_MAIN_TASK_STACK_SIZE: 7168 (Default=3584)
```
