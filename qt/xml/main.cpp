#include <QCoreApplication>
#include <QString>
#include <QDebug>
#include <QFile>
#include <QDomDocument>
#include <iostream>

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);

   QDomDocument doc("mydocument");
   QFile file("sample.xml");
   if (!file.open(QIODevice::ReadOnly))
   {
      std::cout << "Can not open file" << std::endl;
      return 1;
   }
   
   if (!doc.setContent(&file))
   {
      file.close();
      std::cout << "Can not set content" << std::endl;
      return 1;
   }
   
   file.close();
   
   return 0;
}

