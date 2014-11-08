#include <QString>
#include <QSslCertificate>
#include <QRegExp>
#include <QList>
#include <QDebug>
#include <QStringList>
#include <QDirIterator>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QSslError>
#include <QEventLoop>
#include <QSslError>
#include <QSslError>
#include <QObject>

class Downloader : public QObject
{
	Q_OBJECT

public:
    Downloader(const QString& url, const QString& path);
    ~Downloader();
    
    void start();

public slots:
    void onFinishSlot();
    void onReadyRead();
    void onSslErrors(QNetworkReply* reply, const QList<QSslError>& errors);

private:
    QString saveFileName(const QUrl &url);

    QString m_url;
    QString m_path;
    QFile m_output;
    QNetworkReply* m_reply;
    QNetworkAccessManager m_nam;
    QEventLoop* m_eventLoop;
};


