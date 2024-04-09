# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from plan_env/ChunkStamps.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import plan_env.msg

class ChunkStamps(genpy.Message):
  _md5sum = "4649dd6de5a06d0faa920a6802067e3f"
  _type = "plan_env/ChunkStamps"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
int32 from_drone_id
IdxList[] idx_lists
float64 time
================================================================================
MSG: plan_env/IdxList
int32[] ids"""
  __slots__ = ['from_drone_id','idx_lists','time']
  _slot_types = ['int32','plan_env/IdxList[]','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       from_drone_id,idx_lists,time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ChunkStamps, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.from_drone_id is None:
        self.from_drone_id = 0
      if self.idx_lists is None:
        self.idx_lists = []
      if self.time is None:
        self.time = 0.
    else:
      self.from_drone_id = 0
      self.idx_lists = []
      self.time = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.from_drone_id
      buff.write(_get_struct_i().pack(_x))
      length = len(self.idx_lists)
      buff.write(_struct_I.pack(length))
      for val1 in self.idx_lists:
        length = len(val1.ids)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(struct.Struct(pattern).pack(*val1.ids))
      _x = self.time
      buff.write(_get_struct_d().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.idx_lists is None:
        self.idx_lists = None
      end = 0
      start = end
      end += 4
      (self.from_drone_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.idx_lists = []
      for i in range(0, length):
        val1 = plan_env.msg.IdxList()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.ids = s.unpack(str[start:end])
        self.idx_lists.append(val1)
      start = end
      end += 8
      (self.time,) = _get_struct_d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.from_drone_id
      buff.write(_get_struct_i().pack(_x))
      length = len(self.idx_lists)
      buff.write(_struct_I.pack(length))
      for val1 in self.idx_lists:
        length = len(val1.ids)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(val1.ids.tostring())
      _x = self.time
      buff.write(_get_struct_d().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.idx_lists is None:
        self.idx_lists = None
      end = 0
      start = end
      end += 4
      (self.from_drone_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.idx_lists = []
      for i in range(0, length):
        val1 = plan_env.msg.IdxList()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.ids = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
        self.idx_lists.append(val1)
      start = end
      end += 8
      (self.time,) = _get_struct_d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i