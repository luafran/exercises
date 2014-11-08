#include <QCoreApplication>
#include <QString>
#include <QDebug>
#include "Downloader.h"

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);

    const QString url(argv[1]);
    const QString path(argv[2]);
    qDebug() << "url: " << url;
    qDebug() << "path: " << path;
    Downloader d(url, path);
    d.start();
    app.exec();
}

