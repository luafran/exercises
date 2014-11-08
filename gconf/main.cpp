/*
INTEL CONFIDENTIAL
Copyright 2009 Intel Corporation All Rights Reserved.

The source code contained or described herein and all documents related to the 
source code ("Material") are owned by Intel Corporation or its suppliers or 
licensors. Title to the Material remains with Intel Corporation or its 
suppliers and licensors. The Material contains trade secrets and proprietary 
and confidential information of Intel or its suppliers and licensors. The 
Material is protected by worldwide copyright and trade secret laws and treaty 
provisions. No part of the Material may be used, copied, reproduced, modified, 
published, uploaded, posted, transmitted, distributed, or disclosed in any way 
without Intels prior express written permission.

No license under any patent, copyright, trade secret or other intellectual 
property right is granted to or conferred upon you by disclosure or delivery of
the Materials, either expressly, by implication, inducement, estoppel or 
otherwise. Any license under such intellectual property rights must be express 
and approved by Intel in writing.
*/

#include <gconf/gconf.h>
#include <gconf/gconf-client.h>
#include <stdio.h>

int main(int argc, char** argv)
{
   GConfEngine* conf = gconf_engine_get_default();
         
   gchar* config_system_path = gconf_engine_get_string(conf, "/apps/intel_services_manager/11111111-1111-1111-111111111111/System/config_system_path", NULL);
   gchar* host = gconf_engine_get_string(conf, "/system/http_proxy/host", NULL);
   gint port   = gconf_engine_get_int(conf,    "/system/http_proxy/port", NULL);
   gboolean enabled  = gconf_engine_get_bool(conf,   "/system/http_proxy/use_http_proxy", NULL);

   printf("PROXY SETTINGS\n");
   printf("config_system_path: %s\n", config_system_path ? config_system_path : "");
   printf("host   : %s\n", host ? host : "");
   printf("port   : %i\n", port);
   printf("enabled: %i\n", enabled);

   gconf_engine_unref(conf);

   return 0;
}

