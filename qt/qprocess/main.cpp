#include <QCoreApplication>
#include <QString>
#include <QStringList>
#include <QProcess>
#include <iostream>

int main(int argc, char **argv)
{
   std::string fileName("/usr/bin/xterm");
   std::string args("-T Test -fg green");
   std::string workDir(".");
   
   std::cout << "fileName = " << fileName << ", args = " << args << ", workDir = " << workDir << std::endl;

   // Split arguments
   QStringList argList = QString(args.c_str()).split(" ", QString::SkipEmptyParts);
   foreach (QString arg, argList)
   {
      std::cout << "arg = [" << arg.trimmed().toStdString() << "]\n";
   }

   qint64 pid;
   if (!QProcess::startDetached(QString(fileName.c_str()), argList, QString(workDir.c_str()), &pid))
   {
      std::cout << "Could not start detached process" << std::endl;

      return 1;
   }

   return 0;
}

