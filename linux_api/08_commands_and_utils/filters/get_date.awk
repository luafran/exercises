BEGIN { inside_module = 0;}

{
   if ($0 ~ /<module>/)
   {
      inside_module = 1;
   }

   if ($0 ~ /<\/module>/)
   {
      inside_module = 0;
   }
   
   if (inside_module == 1)
   {
      if ($0 ~ /<MAC>/)
      {
         mac_line = $0;
      }

      if ($0 ~ /<Date>2008-08-02T00:44:16/)
      {
         print mac_line;
      }
   }
}

END {}

