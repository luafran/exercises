#include <QCoreApplication>
#include <QSslConfiguration>
#include "Downloader.h"

Downloader::Downloader(const QString& url, const QString& path) : m_url(url), m_path(path)
{

   //m_eventLoop = new QEventLoop();
}

Downloader::~Downloader()
{
    //if (m_eventLoop)
    //    delete m_eventLoop;
}        

void Downloader::start()
{
    QUrl url(m_url);
    url.setUserName(QString("tcce"));
    url.setPassword(QString("intel123"));

    
      QString filename = saveFileName(url);
	   m_output.setFileName(filename);
	   if (!m_output.open(QIODevice::WriteOnly))
	   {
		  qDebug() << "Could not open output file for writing";
          QCoreApplication::instance()->quit();
	   }
	   
	   connect(&m_nam, SIGNAL(sslErrors(QNetworkReply*, const QList<QSslError>&)), this, SLOT(onSslErrors(QNetworkReply*, const QList<QSslError>&)));

	   QNetworkRequest request(url);
    
    QList<QSslCertificate> certs;
    //QStringList nameFilter(QLatin1String("*.crt"));
    //QDirIterator it(QLatin1String("/etc/ssl/certs/"), nameFilter, QDir::Files, QDirIterator::FollowSymlinks | QDirIterator::Subdirectories);
    QStringList nameFilter(QLatin1String("*.crt"));
    QDirIterator it(QLatin1String("/home/dev/certs_sergio/"), nameFilter, QDir::Files, QDirIterator::FollowSymlinks | QDirIterator::Subdirectories);
    while (it.hasNext()) {
        QFile file(it.next());
        if (file.open(QIODevice::ReadOnly | QIODevice::Text))
            certs += QSslCertificate::fromData(file.readAll(), QSsl::Pem);
    }

    foreach (QSslCertificate cert, certs) {
        qDebug() << "Cert Organization: " << cert.subjectInfo(QSslCertificate::Organization);
        qDebug() << "Cert CommonName: " << cert.subjectInfo(QSslCertificate::CommonName);
        qDebug();
    }
    
    QSslConfiguration sslConfig = QSslConfiguration::defaultConfiguration();
    sslConfig.setCaCertificates(certs);
    request.setSslConfiguration(sslConfig);
	   m_reply = m_nam.get(request);

		connect(m_reply, SIGNAL(finished()), SLOT(onFinishSlot()));
		connect(m_reply, SIGNAL(readyRead()), SLOT(onReadyRead()));
	   
    //QCoreApplication::instance()->quit();

}

void Downloader::onFinishSlot()
{
	if (m_reply == 0)
		return;

		m_output.close();
		
		if (!m_reply->error())
		{
		   qDebug() << "File successfully downloaded.";
		}
	   else
		{
		   qDebug() << "Download failed: " << m_reply->errorString();
		   m_output.remove();
        }

    QCoreApplication::instance()->quit(); 
}

void Downloader::onReadyRead()
{
	if ((m_output.write(m_reply->readAll())) == -1)
	{
      qDebug() << "Could not write to destination file.";
      return;
   }
}

void Downloader::onSslErrors(QNetworkReply* reply, const QList<QSslError>& errors)
{
   qDebug() << "The following SSL errors were encountered:";
   foreach (const QSslError &error, errors)
   {
      qDebug() << qPrintable(error.errorString());
   }

   //reply->ignoreSslErrors();
}

QString Downloader::saveFileName(const QUrl &url)
{
   QString path = url.path();
	QString baseName = QFileInfo(path).fileName();
   if (baseName.isEmpty())
      baseName = "download";

   QString dirName(m_path);
   if (dirName.isEmpty())
      dirName = "./";

   QString fileName = dirName + '/' + baseName;

   if (QFile::exists(fileName))
   {
   }

   return fileName;
}

