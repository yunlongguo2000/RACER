# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from plan_env/ChunkData.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ChunkData(genpy.Message):
  _md5sum = "fb59f4568c081139a74132003cbc6f30"
  _type = "plan_env/ChunkData"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 from_drone_id
int32 to_drone_id
int32 chunk_drone_id

uint32[] voxel_adrs
uint8[] voxel_occ_
uint32 idx

# Simulate swarm communication
uint32 latest_idx
float64 pos_x
float64 pos_y
float64 pos_z"""
  __slots__ = ['from_drone_id','to_drone_id','chunk_drone_id','voxel_adrs','voxel_occ_','idx','latest_idx','pos_x','pos_y','pos_z']
  _slot_types = ['int32','int32','int32','uint32[]','uint8[]','uint32','uint32','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       from_drone_id,to_drone_id,chunk_drone_id,voxel_adrs,voxel_occ_,idx,latest_idx,pos_x,pos_y,pos_z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ChunkData, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.from_drone_id is None:
        self.from_drone_id = 0
      if self.to_drone_id is None:
        self.to_drone_id = 0
      if self.chunk_drone_id is None:
        self.chunk_drone_id = 0
      if self.voxel_adrs is None:
        self.voxel_adrs = []
      if self.voxel_occ_ is None:
        self.voxel_occ_ = b''
      if self.idx is None:
        self.idx = 0
      if self.latest_idx is None:
        self.latest_idx = 0
      if self.pos_x is None:
        self.pos_x = 0.
      if self.pos_y is None:
        self.pos_y = 0.
      if self.pos_z is None:
        self.pos_z = 0.
    else:
      self.from_drone_id = 0
      self.to_drone_id = 0
      self.chunk_drone_id = 0
      self.voxel_adrs = []
      self.voxel_occ_ = b''
      self.idx = 0
      self.latest_idx = 0
      self.pos_x = 0.
      self.pos_y = 0.
      self.pos_z = 0.

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
      _x = self
      buff.write(_get_struct_3i().pack(_x.from_drone_id, _x.to_drone_id, _x.chunk_drone_id))
      length = len(self.voxel_adrs)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.voxel_adrs))
      _x = self.voxel_occ_
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I3d().pack(_x.idx, _x.latest_idx, _x.pos_x, _x.pos_y, _x.pos_z))
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
      end = 0
      _x = self
      start = end
      end += 12
      (_x.from_drone_id, _x.to_drone_id, _x.chunk_drone_id,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.voxel_adrs = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.voxel_occ_ = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.idx, _x.latest_idx, _x.pos_x, _x.pos_y, _x.pos_z,) = _get_struct_2I3d().unpack(str[start:end])
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
      _x = self
      buff.write(_get_struct_3i().pack(_x.from_drone_id, _x.to_drone_id, _x.chunk_drone_id))
      length = len(self.voxel_adrs)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.voxel_adrs.tostring())
      _x = self.voxel_occ_
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I3d().pack(_x.idx, _x.latest_idx, _x.pos_x, _x.pos_y, _x.pos_z))
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
      end = 0
      _x = self
      start = end
      end += 12
      (_x.from_drone_id, _x.to_drone_id, _x.chunk_drone_id,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.voxel_adrs = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.voxel_occ_ = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.idx, _x.latest_idx, _x.pos_x, _x.pos_y, _x.pos_z,) = _get_struct_2I3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I3d = None
def _get_struct_2I3d():
    global _struct_2I3d
    if _struct_2I3d is None:
        _struct_2I3d = struct.Struct("<2I3d")
    return _struct_2I3d
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i
