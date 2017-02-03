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

