##################################################
# file: NotificationService_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      /usr/bin/wsdl2py -b NotificationManagementService/NotificationService.wsdl
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from NotificationService_types import *
from ZSI.ServiceContainer import ServiceSOAPBinding

# Messages  
NotificationService_GetMessages_InputMessage = GED("http://Intel.ServicesManager", "GetMessages").pyclass

NotificationService_GetMessages_OutputMessage = GED("http://Intel.ServicesManager", "GetMessagesResponse").pyclass

NotificationService_SendMessages_InputMessage = GED("http://Intel.ServicesManager", "SendMessages").pyclass

NotificationService_SendMessages_OutputMessage = GED("http://Intel.ServicesManager", "SendMessagesResponse").pyclass

NotificationService_SendMessageSync_InputMessage = GED("http://Intel.ServicesManager", "SendMessageSync").pyclass

NotificationService_SendMessageSync_OutputMessage = GED("http://Intel.ServicesManager", "SendMessageSyncResponse").pyclass


# Service Skeletons
class NotificationService(ServiceSOAPBinding):
    soapAction = {}
    root = {}

    def __init__(self, post='/NotificationManagementServiceSite/Service.svc', **kw):
        ServiceSOAPBinding.__init__(self, post)

    def soap_GetMessages(self, ps, **kw):
        request = ps.Parse(NotificationService_GetMessages_InputMessage.typecode)
        return request,NotificationService_GetMessages_OutputMessage()

    soapAction['http://Intel.ServicesManager/NotificationService/GetMessages'] = 'soap_GetMessages'
    root[(NotificationService_GetMessages_InputMessage.typecode.nspname,NotificationService_GetMessages_InputMessage.typecode.pname)] = 'soap_GetMessages'

    def soap_SendMessages(self, ps, **kw):
        request = ps.Parse(NotificationService_SendMessages_InputMessage.typecode)
        return request,NotificationService_SendMessages_OutputMessage()

    soapAction['http://Intel.ServicesManager/NotificationService/SendMessages'] = 'soap_SendMessages'
    root[(NotificationService_SendMessages_InputMessage.typecode.nspname,NotificationService_SendMessages_InputMessage.typecode.pname)] = 'soap_SendMessages'

    def soap_SendMessageSync(self, ps, **kw):
        request = ps.Parse(NotificationService_SendMessageSync_InputMessage.typecode)
        return request,NotificationService_SendMessageSync_OutputMessage()

    soapAction['http://Intel.ServicesManager/NotificationService/SendMessageSync'] = 'soap_SendMessageSync'
    root[(NotificationService_SendMessageSync_InputMessage.typecode.nspname,NotificationService_SendMessageSync_InputMessage.typecode.pname)] = 'soap_SendMessageSync'

