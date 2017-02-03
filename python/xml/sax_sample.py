import sys
from xml.sax import make_parser, handler
from collections import defaultdict


class StationHandler(handler.ContentHandler):

    def __init__(self, out = sys.stdout):
        handler.ContentHandler.__init__(self)

        self._map = {"Station_Name": "Name", "LATITUDE": "Latitude", "LONGITUDE": "Longitude"}
        self._out = out

        self._text = ""
        self._parent = None
        self._station = defaultdict(dict)

    # ContentHandler methods
    
    def startElement(self, name, attrs):
        if name == "StationPrices":
            self._parent = name

        self._text = ""

    def endElement(self, name):
        if self._parent == "StationPrices":
            if name == "StationPrices":
                self._out.write("%s\n" % self._station)
                self._out.write("\n");
                self._parent = None
            elif name.endswith("_Price"):
                self._station['price'][name.split("_")[0]] = self._text
            elif name in self._map:
                self._station[self._map[name]] = self._text

    def characters(self, content):
        self._text = self._text + content

parser = make_parser()
parser.setContentHandler(StationHandler())
parser.parse(sys.argv[1])
