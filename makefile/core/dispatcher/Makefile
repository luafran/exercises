
BUILD = ../../build

include $(BUILD)/Makefile.pre

####### Project specific configuration

TARGET_LIBRARY = libdispatcher
#DESTDIR = $(ROOT)/build_output/lib
#OBJDIR  = ./obj

SRC = Dispatcher.cpp DispatcherImpl.cpp LocalMgr.cpp RemoteMgr.cpp TopicSubTable.cpp TopicPeerTable.cpp

#DEFINES         = -DDEBUG
#CXXFLAGS        = -pipe -g -fPIC $(DEFINES)
#CXXFLAGS        += $(DEFINES)
INCDIRS_TP      = $(BOOST_ROOT)/include
INCDIRS_LOCAL   = . ../include $(ROOT)/util/include
INCDIRS         = $(INCDIRS_TP) $(INCDIRS_LOCAL)

LFLAGS          = 
LIBPATH         = -L$(BOOST_ROOT)/lib
#LIBS            = -lcoreutil -llogger -lboost_thread -lboost_serialization -lpthread -lrt
#SUBLIBS         = ../../build_output/lib/libcoreutil.a ../../build_output/lib/liblogger.a

include $(BUILD)/Makefile.post

