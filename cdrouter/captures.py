#
# Copyright (c) 2017 by QA Cafe.
# All Rights Reserved.
#

"""Module for accessing CDRouter Captures."""

import io

from requests_toolbelt.downloadutils import stream
from marshmallow import Schema, fields, post_load

class Section(object):
    """Model for CDRouter Capture Sections.

    :param value: (optional) Section value as a string.
    """
    def __init__(self, **kwargs):
        self.value = kwargs.get('value', None)

class SectionSchema(Schema):
    value = fields.Str()

    @post_load
    def post_load(self, data):
        return Section(**data)

class Structure(object):
    """Model for CDRouter Capture Structures.

    :param sections: (optional) :class:`captures.Section <captures.Section>` list
    """
    def __init__(self, **kwargs):
        self.sections = kwargs.get('sections', None)

class StructureSchema(Schema):
    sections = fields.Nested(SectionSchema, many=True)

    @post_load
    def post_load(self, data):
        return Structure(**data)

class SummaryPacket(object):
    """Model for CDRouter Capture Summary Packets.

    :param sections: (optional) :class:`captures.Section <captures.Section>` list
    """
    def __init__(self, **kwargs):
        self.sections = kwargs.get('sections', None)

class SummaryPacketSchema(Schema):
    sections = fields.Nested(SectionSchema, many=True)

    @post_load
    def post_load(self, data):
        return SummaryPacket(**data)

class Summary(object):
    """Model for CDRouter Capture Summaries.

    :param structure: (optional) :class:`captures.Structure <captures.Structure>` object
    :param summaries: (optional) :class:`captures.SummaryPacket <captures.SummaryPacket>` list
    """
    def __init__(self, **kwargs):
        self.structure = kwargs.get('structure', None)
        self.summaries = kwargs.get('summaries', None)

class SummarySchema(Schema):
    structure = fields.Nested(StructureSchema)
    summaries = fields.Nested(SummaryPacketSchema, many=True)

    @post_load
    def post_load(self, data):
        return Summary(**data)

class Field(object):
    """Model for CDRouter Capture Fields.

    :param name: (optional) Field name as string.
    :param show_name: (optional) Either `true` or `false` as string.
    :param hide: (optional) Either `true` or `false` as string.
    :param size: (optional) Field size as string.
    :param pos: (optional) Field position as string.
    :param show: (optional) Either `true` or `false` as string.
    :param fields: (optional) :class:`captures.Field <captures.Field>` list
    :param protos: (optional) :class:`captures.Proto <captures.Proto>` list
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.show_name = kwargs.get('show_name', None)
        self.hide = kwargs.get('hide', None)
        self.size = kwargs.get('size', None)
        self.pos = kwargs.get('pos', None)
        self.show = kwargs.get('show', None)
        self.fields = kwargs.get('fields', None)
        self.protos = kwargs.get('protos', None)

class FieldSchema(Schema):
    name = fields.Str()
    show_name = fields.Str()
    hide = fields.Str()
    size = fields.Str()
    pos = fields.Str()
    show = fields.Str()
    _fields = fields.Nested('self', attribute='fields', load_from='fields', dump_to='fields', many=True)
    protos = fields.Nested('ProtoSchema', many=True)

    @post_load
    def post_load(self, data):
        return Field(**data)

class Proto(object):
    """Model for CDRouter Capture Proto.

    :param name: (optional) Field name as string.
    :param pos: (optional) Field position as string.
    :param show: (optional) Either `true` or `false` as string.
    :param show_name: (optional) Either `true` or `false` as string.
    :param value: (optional) Field value as string.
    :param size: (optional) Field size as string.
    :param fields: (optional) :class:`captures.Field <captures.Field>` list
    :param protos: (optional) :class:`captures.Proto <captures.Proto>` list
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.pos = kwargs.get('pos', None)
        self.show = kwargs.get('show', None)
        self.show_name = kwargs.get('show_name', None)
        self.value = kwargs.get('value', None)
        self.size = kwargs.get('size', None)
        self.fields = kwargs.get('fields', None)
        self.protos = kwargs.get('protos', None)

class ProtoSchema(Schema):
    name = fields.Str()
    pos = fields.Str()
    show = fields.Str()
    show_name = fields.Str()
    value = fields.Str()
    size = fields.Str()
    # _fields = fields.Nested(FieldSchema, attribute='fields', load_from='fields', dump_to='fields', many=True)
    # protos = fields.Nested('self', many=True)

    @post_load
    def post_load(self, data):
        return Proto(**data)

class Packet(object):
    """Model for CDRouter Capture Packet.

    :param protos: (optional) :class:`captures.Proto <captures.Proto>` list
    """
    def __init__(self, **kwargs):
        self.protos = kwargs.get('protos', None)

class PacketSchema(Schema):
    protos = fields.Nested(ProtoSchema, many=True)

    @post_load
    def post_load(self, data):
        return Packet(**data)

class Decode(object):
    """Model for CDRouter Capture Decode.

    :param packets: (optional) :class:`captures.Packet <captures.Packet>` list
    """
    def __init__(self, **kwargs):
        self.packets = kwargs.get('packets', None)

class DecodeSchema(Schema):
    packets = fields.Nested(PacketSchema, many=True)

    @post_load
    def post_load(self, data):
        return Decode(**data)

class ASCIIByte(object):
    """Model for CDRouter Capture ASCII bytes.

    :param byte: (optional) Byte value as string.
    :param pos: (optional) Byte position as int.
    """
    def __init__(self, **kwargs):
        self.byte = kwargs.get('byte', None)
        self.pos = kwargs.get('pos', None)

class ASCIIByteSchema(Schema):
    byte = fields.Str()
    pos = fields.Int()

    @post_load
    def post_load(self, data):
        return ASCIIByte(**data)

class ASCIILine(object):
    """Model for CDRouter Capture ASCII lines.

    :param raw: (optional) Raw line as string.
    :param offset: (optional) Line offset as string.
    :param ascii: (optional) :class:`captures.ASCIIByte <captures.ASCIIByte>` list
    :param hex: (optional) :class:`captures.ASCIIByte <captures.ASCIIByte>` list
    """
    def __init__(self, **kwargs):
        self.raw = kwargs.get('raw', None)
        self.offset = kwargs.get('offset', None)
        self.ascii = kwargs.get('ascii', None)
        self.hex = kwargs.get('hex', None)

class ASCIILineSchema(Schema):
    raw = fields.Str()
    offset = fields.Str()
    ascii = fields.Nested(ASCIIByteSchema, many=True)
    hex = fields.Nested(ASCIIByteSchema, many=True)

    @post_load
    def post_load(self, data):
        return ASCIILine(**data)

class ASCIIFrame(object):
    """Model for CDRouter Capture ASCII frame.

    :param name: (optional) Frame name as string.
    :param lines: (optional) :class:`captures.ASCIILine <captures.ASCIILine>` list
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.lines = kwargs.get('lines', None)

class ASCIIFrameSchema(Schema):
    name = fields.Str(missing=None)
    lines = fields.Nested(ASCIILineSchema, many=True)

    @post_load
    def post_load(self, data):
        return ASCIIFrame(**data)

class ASCII(object):
    """Model for CDRouter Capture ASCII.

    :param frame: (optional) :class:`captures.ASCIIFrame <captures.ASCIIFrame>` list
    :param reassembled: (optional) :class:`captures.ASCIIFrame <captures.ASCIIFrame>` list
    """
    def __init__(self, **kwargs):
        self.frame = kwargs.get('frame', None)
        self.reassembled = kwargs.get('reassembled', None)

class ASCIISchema(Schema):
    frame = fields.Nested(ASCIIFrameSchema, missing=None)
    reassembled = fields.Nested(ASCIIFrameSchema, missing=None)

    @post_load
    def post_load(self, data):
        return ASCII(**data)

class Capture(object):
    """Model for CDRouter Captures.

    :param id: (optional) Result ID as string.
    :param seq: (optional) TestResult sequence ID as string.
    :param interface: (optional) Interface name as string.
    :param filename: (optional) Path to capture file as string.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.seq = kwargs.get('seq', None)
        self.interface = kwargs.get('interface', None)
        self.filename = kwargs.get('filename', None)

class CaptureSchema(Schema):
    id = fields.Str()
    seq = fields.Str()
    interface = fields.Str()
    filename = fields.Str()

    @post_load
    def post_load(self, data):
        return Capture(**data)

class CloudShark(object):
    """Model for CDRouter CloudShark uploads.

    :param url: (optional) CloudShark URL as a string.
    """
    def __init__(self, **kwargs):
        self.url = kwargs.get('url', None)

class CloudSharkSchema(Schema):
    url = fields.Str()

    @post_load
    def post_load(self, data):
        return CloudShark(**data)

class CapturesService(object):
    """Service for accessing CDRouter Captures."""

    RESOURCE = 'captures'
    BASE = RESOURCE + '/'

    def __init__(self, service):
        self.service = service

    def _base(self, id, seq): # pylint: disable=invalid-name,redefined-builtin
        return 'results/'+str(id)+'/tests/'+str(seq)+self.BASE

    def list(self, id, seq): # pylint: disable=invalid-name,redefined-builtin
        """Get a list of captures.

        :param id: Result ID as string.
        :param seq: TestResult sequence ID as string.
        :return: :class:`captures.Capture <captures.Capture>` list
        """
        schema = CaptureSchema(exclude=('id', 'seq'))
        resp = self.service.list(self._base(id, seq), filter)
        return self.service.decode(schema, resp, many=True)

    def get(self, id, seq, intf): # pylint: disable=invalid-name,redefined-builtin
        """Get a capture.

        :param id: Result ID as string.
        :param seq: TestResult sequence ID as string.
        :param intf: Interface name as string.
        :return: :class:`captures.Capture <captures.Capture>` object
        :rtype: captures.Capture
        """
        schema = CaptureSchema()
        resp = self.service.get_id(self._base(id, seq), intf)
        return self.service.decode(schema, resp)

    def download(self, id, seq, intf, inline=False): # pylint: disable=invalid-name,redefined-builtin
        """Download a capture as a PCAP file.

        :param id: Result ID as string.
        :param seq: TestResult sequence ID as string.
        :param intf: Interface name as string.
        :param inline: (optional) Use inline version of capture file.
        :return: :class:`io.BytesIO <io.BytesIO>` object
        :rtype: io.BytesIO
        """
        resp = self.service.get_id(self._base(id, seq), intf, params={'format': format, 'inline': inline}, stream=True)
        resp.raise_for_status()
        b = io.BytesIO()
        stream.stream_response_to_file(resp, path=b)
        b.seek(0)
        return (b, self.service.filename(resp))

    def summary(self, id, seq, intf, filter=None, inline=False): # pylint: disable=invalid-name,redefined-builtin
        """Get a capture's summary.

        :param id: Result ID as string.
        :param seq: TestResult sequence ID as string.
        :param intf: Interface name as string.
        :param filter: (optional) PCAP filter to apply as string.
        :param inline: (optional) Use inline version of capture file.
        :return: :class:`captures.Summary <captures.Summary>` object
        :rtype: captures.Summary
        """
        schema = SummarySchema()
        resp = self.service.get(self._base(id, seq)+str(intf)+'/summary/',
                                params={'filter': filter, 'inline': inline})
        return self.service.decode(schema, resp)

    def decode(self, id, seq, intf, filter=None, frame=None, inline=False): # pylint: disable=invalid-name,redefined-builtin
        """Get a capture's decode.

        :param id: Result ID as string.
        :param seq: TestResult sequence ID as string.
        :param intf: Interface name as string.
        :param filter: (optional) PCAP filter to apply as string.
        :param frame: (optional) Frame number to decode.
        :param inline: (optional) Use inline version of capture file.
        :return: :class:`captures.Decode <captures.Decode>` object
        :rtype: captures.Decode
        """
        schema = DecodeSchema()
        resp = self.service.get(self._base(id, seq)+str(intf)+'/decode/',
                                params={'filter': filter, 'frame': frame, 'inline': inline})
        return self.service.decode(schema, resp)

    def ascii(self, id, seq, intf, filter=None, frame=None, inline=False): # pylint: disable=invalid-name,redefined-builtin
        """Get a capture's ASCII (hex dump).

        :param id: Result ID as string.
        :param seq: TestResult sequence ID as string.
        :param intf: Interface name as string.
        :param filter: (optional) PCAP filter to apply as string.
        :param frame: (optional) Frame number to decode.
        :param inline: (optional) Use inline version of capture file.
        :return: :class:`captures.ASCII <captures.ASCII>` object
        :rtype: captures.ASCII
        """
        schema = ASCIISchema()
        resp = self.service.get(self._base(id, seq)+str(intf)+'/ascii/',
                                params={'filter': filter, 'frame': frame, 'inline': inline})
        return self.service.decode(schema, resp)

    def send_to_cloudshark(self, id, seq, intf, inline=False): # pylint: disable=invalid-name,redefined-builtin
        """Send a capture to a CloudShark Appliance. Both
        cloudshark_appliance_url and cloudshark_appliance_token must
        be properly configured via system preferences.

        :param id: Result ID as string.
        :param seq: TestResult sequence ID as string.
        :param intf: Interface name as string.
        :param inline: (optional) Use inline version of capture file.
        :return: :class:`captures.CloudShark <captures.CloudShark>` object
        :rtype: captures.CloudShark
        """
        schema = CloudSharkSchema()
        resp = self.service.post(self._base(id, seq)+str(intf)+'/cloudshark/', params={'inline': inline})
        return self.service.decode(schema, resp)
